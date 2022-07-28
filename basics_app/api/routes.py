from flask import Blueprint, request, jsonify, render_template
from basics_app.forms import addRecipe
from basics_app.helpers import token_required
from basics_app.models import db, User, recipe_schema, recipes_schema, Recipe

api = Blueprint('api', __name__, url_prefix = '/api')
# api_key = "e29ffbb6685f4b6bae241bd6d5cc4e35"

@api.route('/getdata')
@token_required
def getdata(current_user_token):
    return{'some':'value'}

# Add (Create) recipe in RestAPI
@api.route('/recipes', methods = ['POST'])
@token_required
def add_recipe(current_user_token):
    add_form = addRecipe()
    if request.method == 'POST' and add_form.validate_on_submit():
        # if add_form.add_recipe.data:
            print('passing info')
            id = request.json['id']
            name = request.json['name']
            title = request.json['title']
            image = request.json['image']
            sourceUrl = request.json['sourceUrl']
            user_token = current_user_token.token

    recipe = Recipe(id, name, title, image, sourceUrl, user_token = user_token)

    db.session.add(recipe)
    db.session.commit()

    response = recipe_schema.dump(recipe)
    return render_template('profile.html', reponse=jsonify(response) )
    # return jsonify(response)

# retrieve all recipes 
@api.route('/recipes', methods = ['GET'])
@token_required
def get_recipes(current_user_token):
    user = current_user_token.token
    recipes = Recipe.query.filter_by(user_token = user).all()
    response = recipes_schema.dump(recipes)
    return render_template('profile.html', response = response)


@api.route('/recipes/<id>', methods=['DELETE'])
@token_required
def delete_recipe(current_user_token, id):
    recipe = Recipe.query.get(id)
    db.session.delete(recipe)
    db.session.commit()
    response = recipe_schema.dump(recipe)
    return jsonify(response)

# need a delete button