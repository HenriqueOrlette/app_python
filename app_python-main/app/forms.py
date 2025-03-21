from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired()]) #Não é útil (melhor e-mail)
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me!')
    submit = SubmitField ('Sign in')
