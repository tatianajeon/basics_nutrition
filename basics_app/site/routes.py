from crypt import methods
from tokenize import String
from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, jsonify, json
from flask_login.utils import login_required
# from basics_app.models import recipe_schema, Recipe
# from basics_app.models import User
from basics_app.forms import SubmitForm
import requests


site = Blueprint('site', __name__, template_folder = 'site_templates')
api_key = "e29ffbb6685f4b6bae241bd6d5cc4e35"

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/search', methods = ['POST', 'GET'])
@login_required
def search():
    form = SubmitForm()
    api_key = "e29ffbb6685f4b6bae241bd6d5cc4e35"
        
    if request.method == 'POST' and form.validate_on_submit():
        name = form.search.data
        r = requests.get(f"https://api.spoonacular.com/recipes/search?apiKey={api_key}&number=10&query={name}")
            
        if r.status_code == 200:
            data = r.json()
            
            # picture = data['results'][0]['image']
            # r = requests.get(f"https://spoonacular.com/recipeImages/{picture}")
            # picture = r.json()


            # # title = [title['results']['id'] for title in data['results']]
            # # sourceUrl = [sourceUrl['results']['sourceUrl'] for sourceUrl in data['results']]
            # # image = [image['results']['image'] for image in data['results']]
            
            # # recipes = Recipe(name, title, sourceUrl, image)
            # # response = recipe_schema.dump(recipes)
            # # from insomnia 

            # return jsonify(response)

        else: 
            return requests.get(f"https://http.dog/{r.status_code}.jpg")

    return render_template('search.html', form = form, data = data['results'])
    

    






# image_base_URL = 'https://spoonacular.com/recipeImages/'