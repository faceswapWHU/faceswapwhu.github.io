import datetime
from flask import (
    Blueprint, flash, g, request, jsonify, current_app
)
from flask_jwt_extended import jwt_required, get_jwt_identity

from .model import Issue
from . import db

bp = Blueprint('issues', __name__, url_prefix='/issues')


#待修改表
@bp.route('/new', methods=['POST'])
@jwt_required()
def new_issue():
    email = request.json.get('email')
    body = request.json.get('body')
    callname = request.json.get('callname')
    current_user = get_jwt_identity()
    newIssue = Issue(uid=current_user.get('user_id'), email=email, content=body, created_time=datetime.datetime.now(),
                     dealed=0, callname=callname)
    db.session.add(newIssue)
    db.session.commit()
    issue_response = jsonify({'message': 'Issue created'})
    return issue_response
