import base64
import random
from flask import (
    Blueprint, g, request, session, current_app, jsonify
)
from PIL import Image
import io
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask_mail import Message
from datetime import timedelta
from .model import User
from . import db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    get_user = User.query.filter_by(username=username).first()
    if get_user:
        register_response = jsonify({'error': 'User already existed'})
        register_response = register_response, 401
        return register_response
    buffered = io.BytesIO()
    image = Image.open('flaskr/static/avatar/default.png')
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')
    new_user = User(username=username, password=password, avatar=img_str, is_admin=0, times=10)

    db.session.add(new_user)
    db.session.commit()

    register_response = jsonify({'message': 'Register successful'})

    return register_response


@bp.route('/login', methods=(['POST']))
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()

    if not user or not user.password == password:
        login_response = jsonify({'error': 'Invalid username or password'})
        login_response = login_response, 401
        return login_response

    session.clear()
    session['user_id'] = user.id
    obtuser = {'user_id': user.id}
    access_token = create_access_token(identity=obtuser, expires_delta=timedelta(hours=24))
    login_response = jsonify(access_token=access_token)

    return login_response


@bp.route('/get_userinfo', methods=(['GET']))
@jwt_required()
def get_userinfo():
    current_user = get_jwt_identity()
    user = User.query.filter_by(id=current_user.get('user_id')).first()
    get_userinfo_response = jsonify({
        "username": user.username,
        "times": user.times,
        "avatar": user.avatar,
        "email": user.email,
        "signature": user.signature
    })

    return get_userinfo_response


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.filter_by(id=user_id).first()


@bp.route('/logout')
def logout():
    session.clear()


@bp.route('/send_reset_code', methods=['POST'])
def send_reset_code():
    email = request.json.get('email')
    user = User.query.filter_by(email=email).first()
    if not user:
        reset_response = jsonify({'error': 'Wrong email'})
        reset_response = reset_response, 404
        return reset_response

        # 生成六位随机数作为验证码
    reset_code = ''.join(random.choices('0123456789', k=6))
    user.reset_code = reset_code
    db.session.commit()

    # 发送邮件逻辑
    msg = Message('Reset Password Code',
                  sender='597248489@qq.com',
                  recipients=[email],
                  body=f'Your reset code is: {reset_code}')
    mail = current_app.config['mail']
    mail.send(msg)

    send_reset_code_response = jsonify({'message': 'Reset code sent to your email'})
    send_reset_code_response = send_reset_code_response, 200
    return send_reset_code_response


@bp.route('/reset_password', methods=['POST'])
def reset_password():
    email = request.json.get('email')
    code = request.json.get('code')
    user = User.query.filter_by(email=email).first()
    if not user or user.reset_code != code:
        reset_password_response = jsonify({'error': 'Invalid code or email'}), 406
        return reset_password_response

    # 假设验证通过，重置密码
    user.password = '123456'  # 注意：实际中应使用哈希存储密码
    user.reset_code = None  # 清除验证码
    db.session.commit()

    reset_password_response = jsonify({'Message': 'Reset successful'})
    return reset_password_response
