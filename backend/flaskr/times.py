from flask import (
    Blueprint, request, jsonify
)
from flask_jwt_extended import jwt_required, get_jwt_identity

from . import db
from .model import User

bp = Blueprint('times', __name__, url_prefix='/times')


@bp.route('/payment', methods=['POST'])
@jwt_required()
def payment():
    times = request.json.get('times')
    current_user = get_jwt_identity()
    if not times:
        charge_response = jsonify({'error': 'No times provided'}), 403
        return charge_response

    user = User.query.filter_by(id=current_user.get('user_id')).first()
    user.times = user.times + times

    db.session.commit()

    charge_response = jsonify({'message': 'Charge succeed'})
    return charge_response
    # Generate QR code
