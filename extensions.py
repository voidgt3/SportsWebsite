from flask import Flask, render_template, redirect, url_for, flash
from forms import AddProductFrom
from forms import SignUpForm, LogInForm
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Z7$gT4p&xK2@vN3#rH!wL8Qf'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///nike.db"
db = SQLAlchemy(app)



login_manager = LoginManager(app)
