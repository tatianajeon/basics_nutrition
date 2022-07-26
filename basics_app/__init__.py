from flask import Flask
from .site.routes import site
from .api.routes import api
from .authentication.routes import auth
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import db as root_db, login_manager, ma
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from basics_app.helpers import JSONEncoder

app = Flask(__name__)

app.register_blueprint(site)
# app.register_blueprint(api)
app.register_blueprint(auth)

app.config.from_object(Config)

root_db.init_app(app)

migrate= Migrate(app, root_db)
login_manager.init_app(app)
login_manager.login_view = 'auth.signin'

ma.init_app(app)

app.json_encoder = JSONEncoder

CORS(app)



# NAME = "spoonacular"
# VERSION = "1.0.0"

# setup(
#     name=NAME,
#     version=VERSION,
#     description="spoonacular API",
#     author_email="mail@spoonacular.com",
#     url="",
#     keywords=["OpenAPI", "OpenAPI-Generator", "spoonacular API"],
#     install_requires=REQUIRES,
#     packages=find_packages(),
#     include_package_data=True,
#     long_description="""\
#     The spoonacular Nutrition, Recipe, and Food API allows you to access over 380,000 recipes, thousands of ingredients, 800,000 food products, and 100,000 menu items. Our food ontology and semantic recipe search engine makes it possible to search for recipes using natural language queries, such as \&quot;gluten free brownies without sugar\&quot; or \&quot;low fat vegan cupcakes.\&quot; You can automatically calculate the nutritional information for any recipe, analyze recipe costs, visualize ingredient lists, find recipes for what&#39;s in your fridge, find recipes based on special diets, nutritional requirements, or favorite ingredients, classify recipes into types and cuisines, convert ingredient amounts, or even compute an entire meal plan. With our powerful API, you can create many kinds of food and especially nutrition apps.  Special diets/dietary requirements currently available include: vegan, vegetarian, pescetarian, gluten free, grain free, dairy free, high protein, whole 30, low sodium, low carb, Paleo, ketogenic, FODMAP, and Primal.  # noqa: E501
#     """
# )