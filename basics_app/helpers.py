from functools import wraps
import secrets
from json import JSONEncoder
from flask import request, jsonify, json, Blueprint, flash
from basics_app.models import RecipeSchema, db, User, Recipe, recipe_schema, recipes_schema
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
    # saved_recipes = Recipe.query.all()

    lst = Recipe.query.all()
    response = recipes_schema.dump(lst)

    for recipe in response: 
        if add_recipe.title == recipe['title']: 
            print(f'{add_recipe.title} has already been saved to your profile!')
            return

    else:
        print(f'adding {add_recipe.title}')
        flash('this is a flash message')
        db.session.add(add_recipe)
        db.session.commit()

    return add_recipe


def delete_recipe():
    print('hello delete function')
    delete_form = deleteRecipe()
    title = delete_form.title.data
    print(f"trying to delete {title}")

    Recipe.query.filter_by(title=title).delete()
    db.session.commit()
    
    lst = Recipe.query.all()
    response = recipes_schema.dump(lst)
    print(response)

    # for recipe in response: 
    #     to_delete = recipe['title']
    #     if title == to_delete:
    #         db.session.delete(to_delete)
    #         db.session.commit()

    print(f'{title} has been deleted from your profile')
    
    return title




    