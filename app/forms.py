from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, RadioField, SubmitField, validators
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    first_name = StringField('First Name', 
                            validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField('Last Name', 
                            validators=[DataRequired(), Length(min=2, max=30)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    profile = RadioField('',choices=[(1,'High School Student'),(2, 'College Student'), (3, 'Parent or Adviser')], coerce=int)
    optIn = BooleanField('I would like to receive the quarterly FortunEd report')
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')   
    submit = SubmitField('Login')
