from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FloatField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_wtf.file import FileField


class AddProductFrom(FlaskForm):
    name = StringField("Product Name", validators=[DataRequired()])
    price = FloatField("Product Price",  validators=[DataRequired()])
    image_url = StringField("Image Url")
    image = FileField("Product image")
    text = StringField("Description")
    category_id = IntegerField("Category id")

    submit = SubmitField("Submit")

class AddCardForm(FlaskForm):
    header = StringField("Header", validators=[DataRequired()])
    cardtext = StringField("Text", validators=[DataRequired()])
    image_url = StringField("Image Url")
    image = FileField("Product image")
    
    submit = SubmitField("Submit")
class SignUpForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])

    submit = SubmitField("Just Do It")

class LogInForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])

    submit = SubmitField("Just Do It")