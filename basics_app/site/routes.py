from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login.utils import login_required
from flask_login import current_user
from sqlalchemy import values
from basics_app.forms import addRecipe, searchForm, getRecipe, deleteRecipe
from basics_app.models import User, Recipe, recipe_schema, recipes_schema
from basics_app.helpers import save_recipe, delete_recipe, token_required
import requests

site = Blueprint('site', __name__, template_folder = 'site_templates', url_prefix = '/')

@site.route('/')
def home():
    return render_template('index.html')

# @site.route('/getdata')
# @token_required
# def getdata(current_user_token):
#     return{'some':'value'}

# bring in recipes from API
@site.route('/search', methods = ['POST', 'GET'])
@login_required
def search():
    api_key = "e29ffbb6685f4b6bae241bd6d5cc4e35"
    search_form = searchForm()
    add_form = addRecipe()
    data = jsonify(request.form).json
    
    if request.method =='POST':
        if search_form.validate_on_submit():
            ingredient = search_form.search.data
            print(ingredient)
            r = requests.get(f"https://api.spoonacular.com/recipes/search?apiKey={api_key}&number=9&query={ingredient}")
            if r.status_code == 200:
                data = r.json()
                data = data['results']

        if add_form.validate_on_submit():
            save_recipe()
            flash('Recipe successfully saved into Profile')
            ingredient = search_form.search.data
            print('reloading page')
            r = requests.get(f"https://api.spoonacular.com/recipes/search?apiKey={api_key}&number=9&query={ingredient}")
            if r.status_code == 200:
                data = r.json()
                data = data['results']
    
    return render_template('search.html', search_form=search_form, add_form=add_form, data=data, imglink = "https://spoonacular.com/recipeImages/")


# save recipe to profile
# @site.route('/search', methods = ['GET','POST'])
# @login_required
# def save():
#     add_form = addRecipe()

#     if request.method == 'POST' and add_form.validate_on_submit():
#         save_recipe()
#         flash('Recipe saved to your profile')
#         return redirect(url_for('site.profile'))
    



# delete recipe
@site.route('/profile', methods =['GET', 'POST'])
@login_required
def profile():
    delete_form = deleteRecipe()

    if request.method =='POST' and delete_form.validate_on_submit():
        print('processing delete button')
        delete_recipe()

    owner = current_user.token
    recipes = Recipe.query.all()
    response = recipes_schema.dump(recipes)

    # if response: 
    #     print(response[0]['title'])
    #     for recipe in response:
    #         print(recipe['title'])

    return render_template('profile.html', response = response, delete_form = delete_form )
















# @site.route('profile')
# @token_required
# def profile(current_user_token):
#     user = current_user_token.token
#     return render_template('profile.html', user=user)


# @site.route('/profile', methods = ['GET'])
# @login_required
# def profile():
#     recipe = Recipe.query.all()
#     return render_template('profile.html', recipe = recipe)