from flask import (
    Blueprint, request, jsonify
)
from flask_jwt_extended import jwt_required, get_jwt_identity

from . import db
from .model import User

bp = Blueprint('user_profile', __name__, url_prefix='/user')


@bp.route('/setAvatar', methods=(['POST']))
@jwt_required()
def set_avatar():
    current_user = get_jwt_identity()
    data = request.json
    user = User.query.filter_by(id=current_user.get('user_id')).first()
    if not user:
        set_response = jsonify({'error': 'No such user'})
        set_response = set_response, 403
        return set_response

    avatar = data.get('avatar')
    avatar = avatar.split(',')[1]
    user.avatar = avatar
    db.session.commit()

    set_response = jsonify({'message': 'Set avatar succeed'})
    return set_response


@bp.route('/setUsername', methods=(['POST']))
@jwt_required()
def set_name():
    current_user = get_jwt_identity()
    data = request.json
    user = User.query.filter_by(id=current_user.get('user_id')).first()

    if not user:
        set_response = jsonify({'error': 'No such user'})
        set_response = set_response, 403
        return set_response

    name = data.get('username')
    cur_user = User.query.filter_by(username=name).first()
    if cur_user:
        set_response = jsonify({'error': 'Username existed'})
        set_response = set_response, 600
        return set_response
    user.username = name
    db.session.commit()

    set_response = jsonify({'message': 'Set username succeed'})
    return set_response


@bp.route('/setEmail', methods=(['POST']))
@jwt_required()
def set_email():
    current_user = get_jwt_identity()
    data = request.json
    user = User.query.filter_by(id=current_user.get('user_id')).first()
    if not user:
        set_response = jsonify({'error': 'No such user'})
        set_response = set_response, 403
        return set_response

    email = data.get('email')
    cur_user = User.query.filter_by(email=email).first()
    if cur_user:
        set_response = jsonify({'error': 'Email existed'})
        set_response = set_response, 600
        return set_response
    user.email = email
    db.session.commit()

    set_response = jsonify({'message': 'Set email succeed'})
    return set_response


@bp.route('/setSig', methods=(['POST']))
@jwt_required()
def set_signature():
    current_user = get_jwt_identity()
    data = request.json
    user = User.query.filter_by(id=current_user.get('user_id')).first()
    if not user:
        set_response = jsonify({'error': 'No such user'})
        set_response = set_response, 403
        return set_response

    signature = data.get('signature')

    user.signature = signature
    db.session.commit()

    set_response = jsonify({'message': 'Set signature succeed'})
    return set_response


@bp.route('/setPassword', methods=(['POST']))
@jwt_required()
def set_password():
    current_user = get_jwt_identity()
    data = request.json
    user = User.query.filter_by(id=current_user.get('user_id')).first()
    if not user:
        set_response = jsonify({'error': 'No such user'})
        set_response = set_response, 403
        return set_response

    newPassword = data.get('password')

    user.password = newPassword
    db.session.commit()

    set_response = jsonify({'message': 'Set password succeed'})
    return set_response
