from crypt import methods
from tokenize import String
from typing import Any
from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, jsonify, json
from flask_login.utils import login_required
from sqlalchemy import values
from basics_app.api.routes import add_recipe
from basics_app.forms import addRecipe, searchForm, getRecipe
from basics_app.models import Recipe
import requests

site = Blueprint('site', __name__, template_folder = 'site_templates')
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
    # get_form = getRecipe()
    add_form = addRecipe()
    data = jsonify(request.form).json
    # apiImg = jsonify(request.form).json
    # recipeLinks = jsonify(request.form).json
    
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

            # for i in range(len(data)):
            #     recipeLinks = data[i]['sourceUrl']
            #     print(recipeLinks)

    # if request.method == 'GET' and get_form.validate_on_submit():

    #             print('hello this is not needed')

    # if request.method == 'POST' and add_form.validate_on_submit():
    #     return add_recipe(data['results'])

    return render_template('search.html', search_form=search_form, add_form=add_form, data=data, imglink = "https://spoonacular.com/recipeImages/")


# def get_recipe(recipeLinks):
#     for recipeLink in recipeLinks:
#         return render_template('getform.html') and redirect(url_for(recipeLink))



# store recipe in user account
@site.route('/profile', methods = ['GET'])
@login_required
def profile():
    # add_form = addRecipe()
    # recipes =jsonify(request.form).json
    # if request.method == 'GET' and add_form.validate_on_submit():
    #     recipes = Recipe.query.all()
        return render_template('profile.html')