from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email


class UserLoginForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    submit_button = SubmitField()

    
# class UserSignUpForm(FlaskForm):
#     first_name = StringField('First Name', validators = [DataRequired()])
#     last_name = StringField('Last Name', validators = [DataRequired()])
#     email = StringField('Email', validators = [DataRequired(), Email()])
#     password = PasswordField('Password', validators = [DataRequired()])
#     submit_button = SubmitField()


class SubmitForm(FlaskForm):
    search = StringField('search', validators=[DataRequired()])
    submit_button = SubmitField()


class AddContentForm(FlaskForm):
    submit_button = SubmitField('get recipe')
    submit_button = SubmitField('add recipe')