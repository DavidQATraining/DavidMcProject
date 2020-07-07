from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


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
            Length(min=4, max=100)
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

    lasfive = StringField(
        'Last Five',
        validators=[
            DataRequired(),
            Length(min=4, max=300)
        ]
    )

    submit = SubmitField('Make a post')