from flask import Blueprint, request, jsonify
from basics_app.helpers import token_required
from basics_app.models import db, User
import requests

api = Blueprint('api', __name__, url_prefix = '/api')

api_token = "e29ffbb6685f4b6bae241bd6d5cc4e35"
api_url_base = f'https://spoonacular.com/{api_token}/'

@api.route('/getdata')
@token_required
def getdata(current_user_token):
    r = requests.get(f"")


