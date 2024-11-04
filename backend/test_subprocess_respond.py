import os
import sys
sys.path.append('flaskr')
print(sys.path)

from utils.store_image import store_base64_to_image
import base64


with open('test.jpg', 'rb') as data:
    s = base64.b64encode(data.read())

video_src_string = s.decode('utf-8')


# DEBUG
if video_src_string:
    print('video source image is not NULL')
    store_base64_to_image(video_src_string, is_source=True, is_video=True)

user_id = 1

import subprocess
import threading

# 指示视频是否处理完成的flag
video_pipeline_is_finished = False

def run_subprocess():
    # Run your subprocess
    os.chdir('facefusion')
    source_path = 'video_source.png' 
    target_path = f'../flaskr/video/{user_id}/src.mp4' 
    output_path = f'../flaskr/video/{user_id}/result.mp4'
    command = f'python run.py -s {source_path} -t {target_path} -o {output_path} --headless' 
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    stdout, stderr = process.communicate()
    print(stdout.decode().strip())
    print(stderr.decode().strip())
    
    # Notify when the subprocess finishes
    if process.returncode == 0:
        global video_pipeline_is_finished 
        video_pipeline_is_finished = True
        print("Subprocess finished successfully.")
    else:
        print(f"Subprocess finished with errors. Return code: {process.returncode}")
        print(f"Error: {stderr.decode()}")

# Create a thread to run the subprocess in the background
subprocess_thread = threading.Thread(target=run_subprocess)
subprocess_thread.start()

# You can continue doing other things in the main thread
print("Main thread is doing other work...")

# pwd for DEBUG
with subprocess.Popen('pwd', stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
                      shell=True) as proc:
    for line in proc.stdout:
        print(line, end='')

    for line in proc.stderr:
        print(line, end='')

proc.wait()
