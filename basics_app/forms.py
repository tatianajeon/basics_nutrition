from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class UserLoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField('Submit')
    first_name = StringField('First Name')
    last_name = StringField('Last Name')

class searchForm(FlaskForm):
    search = StringField('search', validators=[DataRequired()])
    search_button = SubmitField('Find')

class getRecipe(FlaskForm):
    get_recipe = SubmitField()

class addRecipe(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    image = StringField('image', validators=[DataRequired()])
    readyInMinutes = StringField('readyInMinutes', validators=[DataRequired()])
    sourceUrl = StringField('sourceUrl', validators=[DataRequired()])
    servingSize = StringField('servingSize', validators=[DataRequired()])
    submit_button = SubmitField()

class deleteRecipe(FlaskForm):
    title = StringField('title', validators=[DataRequired()])
    image = StringField('image', validators=[DataRequired()])
    readyInMinutes = StringField('readyInMinutes', validators=[DataRequired()])
    sourceUrl = StringField('sourceUrl', validators=[DataRequired()])
    servingSize = StringField('servingSize', validators=[DataRequired()])
    submit_button = SubmitField()