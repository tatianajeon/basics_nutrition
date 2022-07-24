from flask import Blueprint, render_template
from flask_login.utils import login_required
from basics_app.models import User

site = Blueprint('site', __name__, template_folder = 'site_templates')

@site.route('/')
def home():
    return render_template('index.html',)

@site.route('/profile')
@login_required
def profile():
    # drones = Drone.query.all()
    # return render_template('profile.html', drones=drones)
    return render_template('profile.html')