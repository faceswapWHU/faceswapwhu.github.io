import base64
import os
import sys
import random
from datetime import datetime

from flask import (
    Blueprint, request, jsonify, current_app, send_file
)
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_mail import Message

from . import db, create_app
from .model import Img, User

sys.path.append('flaskr')
# print(sys.path)
from utils.store_image import store_base64_to_image

import subprocess

bp = Blueprint('face', __name__, url_prefix='/face')


def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def finished_email(user_id):
    user = User.query.filter_by(id=user_id).first()
    email = user.email
    # 发送邮件逻辑
    msg = Message('视频转换。',
                  sender='597248489@qq.com',
                  recipients=[email],
                  body='视频转换完成')
    mail = current_app.config['mail']
    mail.send(msg)

    return 0


###待实现，需修改后缀名判断（似乎没影响）等
@bp.route('/gen_img', methods=['POST'])
@jwt_required()
def gen_img():
    current_user = get_jwt_identity()
    # DEBUG
    user_id = current_user.get('user_id')
    user = User.query.filter_by(id=user_id).first()
    # 检测余额
    times = user.times
    if not times > 0:
        return jsonify({'error': 'Not enough times'}), 406
    times = times - 1
    User.times = times

    data = request.json
    srcfile = data.get('src')
    tarfile = data.get('tar')
    src_string = srcfile[srcfile.find(',') + 1:]
    # DEBUG
    if src_string:
        print('src_string is not NULL')
    tar_string = tarfile[tarfile.find(',') + 1:]
    if src_string and tar_string:
        store_base64_to_image(src_string, is_source=True)
        store_base64_to_image(tar_string, is_source=False)

        # change to /face-magic/facefusion dir to run model
        os.chdir('facefusion')
        run_command = ['python', 'run.py', '-s', 'source.png', '-t', 'target.png', '-o', 'output', '--headless']
        with subprocess.Popen(run_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) as proc:
            for line in proc.stdout:
                print(line, end='')

            for line in proc.stderr:
                print(line, end='')

        proc.wait()

        # rename the output
        mv_command = 'mv output/* output.png'
        # use shell to ensure that the wildcard is expanded correctly
        with subprocess.Popen(mv_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                              shell=True) as proc:
            for line in proc.stdout:
                print(line, end='')

            for line in proc.stderr:
                print(line, end='')

        proc.wait()

        with open('output.png', 'rb') as data:
            out_string = base64.b64encode(data.read())
        out_string_b = out_string.decode('utf-8')

        os.chdir('../..')
        result = f'data:image/png;base64,{out_string_b}'
    else:
        result = tarfile
    user_id = current_user.get('user_id')
    new_img = Img(uid=user_id, name=str(user_id) + ".png", content=result, created_time=datetime.now())
    db.session.add(new_img)
    db.session.commit()
    return jsonify({'image': result})


'''
###待实现
@bp.route('/download', methods=['GET'])
def downloadimg():
    # 查询数据库，获取最新生成的图片内容
    cur = db.execute('SELECT content FROM pics WHERE uid = ? ORDER BY id DESC LIMIT 1', (g.user['id'],))
    row = cur.fetchone()

    if row:
        # 解码 base64 编码的图片数据
        img_data = base64.b64decode(row['content'])

        # 创建一个内存文件对象
        img_stream = io.BytesIO(img_data)

        # 返回图像作为文件下载
        return send_file(img_stream, attachment_filename='generated_image.png', as_attachment=True)
    else:
        return '未找到可下载的图片！'


#待实现
@bp.route('/gen_video', methods=['GET'])
def gen_video():
    pass
'''


# 上传视频到数据库
@bp.route('/upload_video', methods=['POST'])
@jwt_required()
def upload_video():
    current_user = get_jwt_identity()
    video = request.files['video']
    if video.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    if video and video.filename.endswith('.mp4'):
        filename = 'src.mp4'

        cur_folder = 'video/user_' + str(current_user.get('user_id')) + '/'
        folder = os.path.join(current_app.config['BASEDIR'], cur_folder)

        if not os.path.exists(folder):
            os.makedirs(folder)
        file_path = folder + filename
        video.save(file_path)

        return jsonify({'message': 'File uploaded successfully'}), 200

    return jsonify({'error': 'Only MP4 files are allowed'}), 400


video_pipeline_is_finished = False

@bp.route('/gen_video', methods=['POST'])
@jwt_required()
def gen_video():
    current_user = get_jwt_identity()
    # DEBUG
    print(current_user)
    tarImg = request.json.get('tar')
    user_id = current_user.get('user_id')
    #视频在/flaskr/video/user_id/src.mp4
    #结果储存到/flaskr/video/user_id/result.mp4
    video_src_string = tarImg[tarImg.find(',') + 1:]
    # DEBUG
    if video_src_string:
        print('video source image is not NULL')
        store_base64_to_image(video_src_string, is_source=True, is_video=True)

    import subprocess
    import threading

    def run_subprocess():
        # Run your subprocess
        working_dir = 'facefusion'
        source_path = 'video_source.png' 
        target_path = f'../flaskr/video/user_{user_id}/src.mp4' 
        output_path = f'../flaskr/video/user_{user_id}/result.mp4'
        command = f'python run.py -s {source_path} -t {target_path} -o {output_path} --headless' 
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=working_dir)
        stdout, stderr = process.communicate()
        
        print(stdout.decode().strip())
        print(stderr.decode().strip())

        # Notify when the subprocess finishes
        if process.returncode == 0:
            global video_pipeline_is_finished 
            video_pipeline_is_finished = True
            print("Subprocess finished successfully.")
            app = create_app()
            with app.app_context():
                finished_email(user_id)
        else:
            print(f"Subprocess finished with errors. Return code: {process.returncode}")
            print(f"Error: {stderr.decode()}")

    # pwd for DEBUG
    with subprocess.Popen('pwd', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True) as proc:
        for line in proc.stdout:
            print(line, end='')

        for line in proc.stderr:
            print(line, end='')

    proc.wait()

    # Create a thread to run the subprocess in the background
    subprocess_thread = threading.Thread(target=run_subprocess)
    subprocess_thread.start()


    # You can continue doing other things in the main thread
    print("Main thread is doing other work...")
    
    # pwd for DEBUG
    with subprocess.Popen('pwd', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True) as proc:
        for line in proc.stdout:
            print(line, end='')

        for line in proc.stderr:
            print(line, end='')

    proc.wait()

    # Optionally, wait for the subprocess to finish if you need to
    #subprocess_thread.join()
    #print("Main thread: Subprocess has completed.")
    return jsonify({'message': 'Video swap started'}), 200


@bp.route('/download_video', methods=['GET'])
@jwt_required()
def download_video():
    current_user = get_jwt_identity()
    file_name = 'result.mp4'
    cur_folder = 'video/user_' + str(current_user.get('user_id')) + '/'
    folder = os.path.join(current_app.config['BASEDIR'], cur_folder)
    file_path = f"{folder}{file_name}"
    if not os.path.exists(file_path):
        return {"error": "Video file not found"}, 404
    response = send_file(file_path, as_attachment=True)
    return response
