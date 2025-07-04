"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from api.models import db, Users


api = Blueprint('api', __name__)
CORS(api)# Allow CORS requests to this API


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    response_body = { "message": "Hello! I'm a message that came from the backend"}
    return response_body, 200


@api.route ('/users' , methods=['POST' , 'GET'])
def users():
    reponse_body = {}
    if request.method == 'GET':
        reponse_body['message'] = 'listado de usuarios'
        return reponse_body, 200