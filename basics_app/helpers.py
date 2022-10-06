from functools import wraps
import secrets
from json import JSONEncoder
from flask import request, jsonify, json, Blueprint
from basics_app.models import db, User, Recipe
from basics_app.forms import addRecipe, deleteRecipe
from flask_login import current_user
import decimal

def token_required(our_flask_function):
    @wraps(our_flask_function)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token'].split(' ')[1]
            print(token)
        if not token: 
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            current_user_token = User.query.filter_by(token = token).first()
            print(current_user_token)
            if not current_user_token or current_user_token.token != token:
               return jsonify({'message':'Something\'s not right here...'})

        except:
            owner = User.query.filter_by(token = token).first()

            if token != owner.token and secrets.compare_digest(token, owner.token):
                return jsonify({'message': 'Something\'s not right here...'})
        return our_flask_function(current_user_token, *args, **kwargs)
    return decorated

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return super(JSONEncoder, self).default(obj)



def save_recipe():
    form = addRecipe()

    title = form.title.data
    readyInMinutes = form.readyInMinutes.data
    servingSize = form.servingSize.data
    sourceUrl = form.sourceUrl.data
    image = form.image.data
    user_token = current_user.token
    
    add_recipe = Recipe(title, readyInMinutes, servingSize, sourceUrl, image, user_token = user_token)
    saved_recipes = Recipe.query.all()

    if add_recipe.title in saved_recipes: 
        print(f'{add_recipe.title} has already been saved to your profile!')
    
    else:
        print(f'adding {add_recipe.title}')
        db.session.add(add_recipe)
        db.session.commit()
    
    return saved_recipes


def delete_recipe():
    delete_form = deleteRecipe()
    title = delete_form.title.data
    
    to_delete = Recipe.query.get(title)
    db.session.delete(to_delete)
    db.session.commit()
    print(f'{title} has been deleted from your profile')
    
    return to_delete