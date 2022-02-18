from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, Optional


class MessageForm(FlaskForm):
    """ Form for adding/editing messages """

    text = TextAreaField('text', validators=[DataRequired()])


class UserAddForm(FlaskForm):
    """ Form for adding users """

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    image_url = StringField('Image URL', validators=[Optional()])


class LoginForm(FlaskForm):
    """ Login form """

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])

class UserEditForm(FlaskForm):
    """ Form for editing user profile information """

    username = StringField('Username', validators=[DataRequired()])
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    image_url = StringField('Image URL', validators=[Optional()])
    header_image_url = StringField('Header Image URL', validators=[Optional()])
    bio = TextAreaField('Bio', validators=[Optional()])
    password = PasswordField('Enter Current Password', validators=[DataRequired(), Length(min=6)])
