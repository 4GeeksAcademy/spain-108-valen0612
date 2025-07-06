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


@api.route ('/users' , methods=['GET' , 'POST'])
def users():
    response_body = {}
    if request.method == 'GET':
        response_body['message'] = 'listado de usuarios'
        return response_body, 200
    if request.method == 'POST':
        response_body['message'] = 'usuario nuevo creado'
        return response_body, 201


@api.route('/users/<int:users_id>' , methods = ['DELETE'])
def deleate_users(users_id):
    response_body ={}
    response_body['message'] = f'usuario eliminado {users_id}'
    return response_body, 200

    
@api.route ('/posts' , methods=['GET' , 'POST'])
def post():
    response_body = {}
    if request.method == 'GET':
       response_body['message'] = 'listado de publicaciones'
       return response_body, 200
    if request.method == 'POST':
        response_body['message'] = 'creacion nueva publicacion'
        return response_body,201
    
    
@api.route('/posts/<int:posts_id>' , methods = ['DELETE'])
def delete_post(posts_id):
    response_body ={}
    response_body['message'] = f'publicacion eliminada con id{posts_id}'
    return response_body, 200

@api.route('/coments' , methods = ['GET' , 'POST'])
def coments():
    response_body ={}
    if request.method =='GET':
        response_body['message'] = 'cometarios'
        return response_body, 200
    
    if request.method == 'POST':
        response_body['message'] = 'nuevo comentario creado'
        return response_body, 201

@api.route('/coments/<int:coment_id>' , methods=['DELETE'])
def delete_coment(coment_id):
    response_body = {}
    response_body['message'] = f'comentario eliminado{coment_id}'
    return response_body, 200

@api.route('/characters' , methods =['GET'])
def characters():
    response_body = {}
    response_body['message'] = 'listado de personajes'
    return response_body, 200

@api.route('/characters/<int:charcter_id>' , methods=['GET'])
def get_character(character_id):
    response_body={}
    response_body['message'] = f'persona con ID {character_id}'
    return response_body, 200

@api.route('/characters/<int:character_id>', methods=['DELETE'])
def delete_character(character_id):
    response_body = {}
    response_body['message'] = f'personaje eliminado con ID {character_id}'
    return response_body, 200

@api.route('/planets', methods=['GET'])
def get_planets():
    response_body = {}
    response_body['message'] = 'Aquí iría el listado de planetas'
    return response_body, 200


@api.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    response_body = {}
    response_body['message'] = f'Aquí se mostraría el planeta con ID {planet_id}'
    return response_body, 200

@api.route('/planets/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    response_body = {}
    response_body['message'] = f'planeta eliminado con ID {planet_id}'
    return response_body, 200