from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class UserLoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()

class searchForm(FlaskForm):
    search = StringField('search', validators=[DataRequired()])
    search_button = SubmitField()

class getRecipe(FlaskForm):
    get_recipe = SubmitField()

class addRecipe(FlaskForm):
    id = StringField()
    add_recipe = SubmitField()
        
# class UserSignUpForm(FlaskForm):
#     first_name = StringField('First Name', validators = [DataRequired()])
#     last_name = StringField('Last Name', validators = [DataRequired()])
#     email = StringField('Email', validators = [DataRequired(), Email()])
#     password = PasswordField('Password', validators = [DataRequired()])
#     submit_button = SubmitField()