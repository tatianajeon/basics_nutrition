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


# @api.route('/recipes', methods = ['GET'])
# # @token_required

# def find_recipes(name):
#     r = requests.get(f"https://api.spoonacular.com/recipes/complexSearch?query={name}&apiKey={api_key}&number=1")

#     if r.status_code == 200:
#         data = r.json()

#         name = name
#         title = [title['results']['id'] for title in data['results']]
#         sourceUrl = [sourceUrl['results']['sourceUrl'] for sourceUrl in data['results']]
#         image = [image['results']['image'] for image in data['results']]
        
#         recipe = Recipe(name, title, sourceUrl, image)

#         response = recipe_schema.dump(recipe)
#         return jsonify(response)

#     else:
#         print(f"Error Status Code: {r.status_code}")


# @api.route('/myrecipes', methods = ['POST'])


    
# https://api.spoonacular.com/reciples/{id}/nutritionWidget.json?apiKey={api_token}

# https://api.spoonacular.com/recipes/complexSearch?query={name}&apiKey={api_key}&number=1