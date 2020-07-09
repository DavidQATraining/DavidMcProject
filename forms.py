from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired()
        ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    f_name = StringField(
        'First name',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    l_name = StringField(
        'Last name',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
        ]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Sign Up')


class FightersForm(FlaskForm):
    f_name = StringField(
        'First name',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    l_name = StringField(
        'Last name',
        validators=[
            DataRequired(),
            Length(min=1, max=30)
        ]
    )

    age = StringField(
        'Age',
        validators=[
            DataRequired(),
            Length(min=2, max=100)
        ]
    )

    weightclass = StringField(
        'Weightclass',
        validators=[
            DataRequired(),
            Length(min=4, max=300)
        ]
    )

    record = StringField(
        'Record',
        validators=[
            DataRequired(),
            Length(min=4, max=300)
        ]
    )

    lastfive = StringField(
        'Last Five',
        validators=[
            DataRequired(),
            Length(min=4, max=300)
        ]
    )

    submit = SubmitField('Add a fighter')
