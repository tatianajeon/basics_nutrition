from crypt import methods
from tokenize import String
from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, jsonify, json
from flask_login.utils import login_required
from basics_app.models import recipe_schema, Recipe
# from basics_app.models import User
from basics_app.forms import SubmitForm, AddContentForm
import requests


site = Blueprint('site', __name__, template_folder = 'site_templates')
api_key = "e29ffbb6685f4b6bae241bd6d5cc4e35"

@site.route('/')
def home():
    return render_template('index.html')


# bring in recipes from API
@site.route('/search', methods = ['POST', 'GET'])
@login_required
def search():
    form = SubmitForm()
    
    if request.method == 'POST' and form.validate_on_submit():
        name = form.search.data
        print(name)
        # r = requests.get(f"https://api.spoonacular.com/recipes/search?apiKey={api_key}&number=10&query={name}")

        # if r.status_code == 200:
        #     data = r.json()
        # else: 
        #     return requests.get(f"https://http.dog/{r.status_code}.jpg")

    return render_template('search.html', form=form, )
    

# store recipe in user account
# @site.route('/profile', methods = ['POST', 'GET'])
# @login_required
# def profile():
#     recipes = Recipe.query.all()
#     return render_template('profile.html', recipes = recipes)