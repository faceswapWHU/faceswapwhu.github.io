from datetime import datetime
from . import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Integer, nullable=False)
    times = db.Column(db.Integer, nullable=False)
    avatar = db.Column(db.Text, nullable=True)
    email = db.Column(db.String(255), unique=True, nullable=True)
    signature = db.Column(db.String(255), nullable=True)
    reset_code = db.Column(db.String(6), nullable=True)


class Img(db.Model):
    __tablename__ = 'image'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    name = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_time = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 定义外键关系
    user = db.relationship('User', backref='images')


class Issue(db.Model):
    __tablename__ = 'issue'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_time = db.Column(db.TIMESTAMP)
    dealed = db.Column(db.Integer, nullable=True)
    callname = db.Column(db.String(255), nullable=False)

    # 定义与User模型的关系
    user = db.relationship('User', backref=db.backref('issues', lazy=True))


class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    mime_type = db.Column(db.String(100), nullable=False)
    video_data = db.Column(db.LargeBinary, nullable=True)  # 对应longblob
    created_at = db.Column(db.TIMESTAMP)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'),
                    nullable=True)  # 这里使用nullable=True，因为SQL语句中是NULL DEFAULT NULL

    # 定义与User模型的关系
    user = db.relationship('User', backref=db.backref('videos', lazy=True), foreign_keys=[uid])
