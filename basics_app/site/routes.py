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
import webbrowser

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
    get_form = getRecipe()
    add_form = addRecipe()
    data = jsonify(request.form).json
    recipeLinks = jsonify(request.form).json
    
    if request.method == 'POST' and search_form.validate_on_submit():
        name = search_form.search.data
        print(name)
        r = requests.get(f"https://api.spoonacular.com/recipes/search?apiKey={api_key}&number=10&query={name}")
        if r.status_code == 200:
            data = r.json()
            data = data['results']

            for i in range(len(data)):
                recipeLinks = data[i]['sourceUrl']
                print(recipeLinks)

    if request.method == 'GET' and get_form.validate_on_submit():

                return get_recipe(recipeLinks)


    return render_template('search.html', search_form=search_form, get_form = get_form, add_form=add_form, data=data)


def get_recipe(recipeLinks):
    for recipeLink in recipeLinks:
        return render_template('getform.html') and redirect(url_for(recipeLink))
                


# store recipe in user account
@site.route('/profile' )
@login_required
def profile():
    recipes = Recipe.query.all()
    return render_template('profile.html', recipes = recipes)