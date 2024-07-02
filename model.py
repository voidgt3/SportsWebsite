from extensions import db, app, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from seed import *

class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    products = db.relationship('Product', back_populates='category')

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image_url = db.Column(db.String)
    price = db.Column(db.Float)
    text = db.Column(db.String)

    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship("Category", back_populates="products")

class Card(db.Model):
    __tablename__ = "cards"
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String)
    image_url = db.Column(db.String)
    textcard = db.Column(db.String)

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    username = db.Column(db.String)
    role = db.Column(db.String)

    def __init__(self, password, username, email, role="user"):
        self.password = generate_password_hash(password)
        self.username = username
        self.email = email
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        admin = User(email="admin@gmail.com", role="admin", password="admin1234", username="admin")
        db.session.add(admin)
        db.session.commit()

        for category in categories:
            new_category = Category()
            new_category.name = category["name"]
            db.session.add(new_category)
            db.session.commit()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)
