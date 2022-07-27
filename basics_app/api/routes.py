from turtle import title
from unicodedata import name
from flask import Blueprint, request, jsonify, render_template
from basics_app.helpers import token_required
from basics_app.models import db, User, recipe_schema, recipes_schema, Recipe
import requests
# import spoonacular as sp
# from basics_app.forms import SubmitForm

api = Blueprint('api', __name__, url_prefix = '/api')
api_key = "e29ffbb6685f4b6bae241bd6d5cc4e35"

@api.route('/getdata')
@token_required
def getdata(current_user_token):
    return{'some':'value'}


# Add (Create) recipe to RestAPI
@api.route('/recipes', methods = ['POST'])
@token_required
def add_recipe(current_user_token):
    
    id = request.json['id']
    name = request.json['name']
    title = request.json['title']
    image = request.json['image']
    sourceUrl = request.json['sourceUrl']
    user_token = current_user_token.token

    # print(f"test: {current_user_token.token}")

    recipe = Recipe(id, name, title, image, sourceUrl, user_token = user_token)

    db.session.add(recipe)
    db.session.commit()

    response = recipe_schema.dump(recipe)

    return jsonify(response)


# retrieve all recipes 
@api.route('/recipes', methods = ['GET'])
@token_required
def get_recipes(current_user_token):
    user = current_user_token.token
    response = Recipe.query.filter_by(user_token = user).all()
    return jsonify(response)







# https://api.spoonacular.com/reciples/{id}/nutritionWidget.json?apiKey={api_token}

# https://api.spoonacular.com/recipes/complexSearch?query={name}&apiKey={api_key}&number=1