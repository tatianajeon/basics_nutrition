from flask import Blueprint, render_template, request, flash, jsonify
from flask_login.utils import login_required
from flask_login import current_user
from sqlalchemy import values
from basics_app.forms import addRecipe, searchForm, deleteRecipe
from basics_app.models import Recipe, recipes_schema
from basics_app.helpers import save_recipe, delete_recipe
import requests

site = Blueprint('site', __name__, template_folder = 'site_templates', url_prefix = '/')

@site.route('/')
def home():
    return render_template('index.html')

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
            r = requests.get(f"https://api.spoonacular.com/recipes/search?apiKey={api_key}&number=20&query={ingredient}")
            if r.status_code == 200:
                data = r.json()
                data = data['results']

        if add_form.validate_on_submit():
            save_recipe() 
            ingredient = search_form.search.data
            print('reloading page')
            flash('Recipe successfully saved', 'save-success')
            r = requests.get(f"https://api.spoonacular.com/recipes/search?apiKey={api_key}&number=20&query={ingredient}")
            if r.status_code == 200:
                data = r.json()
                data = data['results']


    return render_template('search.html', search_form=search_form, add_form=add_form, data=data, imglink = "https://spoonacular.com/recipeImages/")


# delete recipe
@site.route('/profile', methods =['GET', 'POST'])
@login_required
def profile():
    print("hello this is the profile section")
    delete_form = deleteRecipe()
    title = delete_form.title.data

    if request.method =='POST':
        print("I know you pressed the button")
        print(title)
        delete_recipe()

    lst = Recipe.query.all()
    response = recipes_schema.dump(lst)

    if response: 
        print(response[0]['title'])
        for recipe in response:
            print(recipe['title'])

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