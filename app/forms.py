from flask_wtf import FlaskForm
from wtfforms import Stringfield, PasswordField, BooleanField, SubmitField
from wtfforms.validators import DataRequired

class LoginForm(FlaskForm):

    username = Stringfield('Username', validators=DataRequired()) #Não é útil (melhor e-mail)
    password = PasswordField('Password', validators=DataRequired())
    remember_me = BooleanField('Remember me!')
    submit = SubmitField ('Sign in')
