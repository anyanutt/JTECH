from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    Name = StringField('Name',
                validators=[DataRequired(), Length(min=2, max=20)])
    batteryID = StringField('batteryID',
                validators=[DataRequired(), Length(min=2, max=20)])
    Date      = StringField('Date',
                validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField('Sign Up')


class AdminForm(FlaskForm):
    email = StringField('Email',
                    validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Submit')
