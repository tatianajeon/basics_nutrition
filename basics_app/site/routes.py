from crypt import methods
from tokenize import String
from typing import Any
from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, jsonify, json
from flask_login.utils import login_required
from basics_app.helpers import token_required
from sqlalchemy import values
from basics_app.api.routes import add_recipe
from basics_app.forms import addRecipe, searchForm, getRecipe
from basics_app.models import User, Recipe
import requests

site = Blueprint('site', __name__, template_folder = 'site_templates', url_prefix = '/')
api_key = "e29ffbb6685f4b6bae241bd6d5cc4e35"

@site.route('/')
def home():
    return render_template('index.html')


# bring in recipes from API
@site.route('/search', methods = ['GET', 'POST'])
@login_required
def search():
    api_key = "e29ffbb6685f4b6bae241bd6d5cc4e35"
    search_form = searchForm()
    add_form = addRecipe()
    data = jsonify(request.form).json
    
    if request.method == 'POST' and search_form.validate_on_submit():
        name = search_form.search.data
        print(name)
        r = requests.get(f"https://api.spoonacular.com/recipes/search?apiKey={api_key}&number=9&query={name}")
        if r.status_code == 200:
            data = r.json()
            data = data['results']
            # for i in range(len(data)):
            #     img = data[i]['image']
            #     rr = requests.get(f"https://spoonacular.com/recipeImages/{img}")
            #     apiImg = rr.json()


    if add_form.validate_on_submit():
        print('nothing happens')

    return render_template('search.html', search_form=search_form, data=data, add_form=add_form, imglink = "https://spoonacular.com/recipeImages/")


# display recipe in user account
@site.route('/profile', methods = ['GET'])
@login_required
def profile():
    response = Recipe.query.all()
    return render_template('profile.html', response = response)





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