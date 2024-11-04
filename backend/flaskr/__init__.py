import os
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        JWT_SECRET_KEY='dev',
        # 邮件配置
        MAIL_SERVER='smtp.qq.com',  # 邮件服务器地址，这个不需要改
        MAIL_PORT=587,  # 邮件服务器端口，这个不需要改
        MAIL_USERNAME='2758224213@qq.com',
        MAIL_PASSWORD='ykgyfkndkdaobdhe',
        MAIL_USE_TLS=True,  # 启用 TLS
        MAIL_DEFAULT_SENDER='2758224213@qq.com',  # 设置默认用来发送邮件的邮箱，建议和MAIL_USERNAME保持一致
        # mysql设置
        SQLALCHEMY_DATABASE_URI=('postgresql:'
                                 '//FaceMagicDB_owner:j2Bypqen8vsA@ep-tight-dawn-a15dyfk2.ap-southeast-1.aws.neon.tech/FaceMagicDB?sslmode=require'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        BASEDIR=os.path.abspath(os.path.dirname(__file__))
    )
    cors = CORS(app, resources={r"/*": {
        "origins": [
            "*"
        ],
        "methods": [
            "GET",
            "POST",
            "PUT",
            "OPTIONS"
        ],
        "allow_headers": [
            "Content-Type",
            "Authorization"
        ],
        "expose_headers": [
            "Content-Length",
            "X-My-Custom-Header"
        ],
        "supports_credentials": True
    }})

    jwt = JWTManager(app)
    mail = Mail(app)
    app.app_context().push()

    # 用于生成加密签名的序列化器
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    app.config['serializer'] = serializer
    app.config['mail'] = mail

    db.init_app(app)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path, exist_ok=True)
    except OSError as e:
        print(f"OSError occurred: {e}")

    with app.app_context():
        from .model import User
        db.create_all()
    from . import auth
    app.register_blueprint(auth.bp)
    from . import face
    app.register_blueprint(face.bp)
    from . import user_profile
    app.register_blueprint(user_profile.bp)
    from . import issues
    app.register_blueprint(issues.bp)
    from . import times
    app.register_blueprint(times.bp)

    return app
