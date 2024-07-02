
from flask import  render_template, redirect, url_for, flash
from forms import SignUpForm, LogInForm, AddCardForm, AddProductFrom
from flask_sqlalchemy import SQLAlchemy
import os
from extensions import app, db
from flask_login import login_user, logout_user, login_required, current_user
from model import Product, Card, User,  Category

@app.route('/')
def home():
    return render_template("index.html", products =Product.query.all(), cards = Card.query.all())

@app.route("/product/<int:product_id>")
def product(product_id):
    product = Product.query.get(product_id)

    if not product:
        return render_template("404.html", id=product_id)
    

    return render_template("product.html", product=product)

@app.route('/login', methods = ['POST', 'GET'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        user = User.query.filter(User.username == form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)

        return redirect("/")
    return render_template("login.html", form=form)

@app.route('/signup', methods = ['POST', 'GET'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        new_user = User (email = form.email.data,
                         username = form.username.data,
                           password = form.password.data,
                             )
        
        db.session.add(new_user)
        db.session.commit()

        return redirect("/")
    return render_template('signup.html', form=form)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/basketball/<int:category_id>')
@app.route('/basketball')
def basketball(category_id = None):
    if category_id:
        products = Category.query.get(category_id).products
    else:
        products = Product.query.all()
    return render_template("basketball.html", products = products)



@app.route("/add_product", methods = ['POST', 'GET'])
#@login_required
def add_product():
    if current_user.role != "admin": 
        return redirect("/")
    form = AddProductFrom()
    if form.validate_on_submit():
        #image = form.image.data
        #file_path = os.path.join(app.root_path, "static", "images", image.filename)
        new_product = Product   (name = form.name.data, 
                                image_url = form.image_url.data,
                                price = form.price.data, 
                                text = form.text.data,
                                category_id = form.category_id.data
                                )
        
        db.session.add(new_product)
        db.session.commit()

        #image.save(os.path.join(app.root_path, file_path))
        #print((os.path.join(app.root_path, "static", "images", image.filename)))
    return render_template('add_product.html', form=form)

@app.route("/add_card", methods = ['POST', 'GET'])
def add_card():
    form = AddCardForm()
    if form.validate_on_submit():
        image = form.image.data
        file_path = os.path.join( "static", "images", image.filename)
        new_card = Card(header=form.header.data, image_url=file_path, textcard=form.cardtext.data,)
    
        db.session.add(new_card)
        db.session.commit()

        image.save(os.path.join(app.root_path,  file_path))
        print((os.path.join(app.root_path, "static", "images", image.filename)))
    return render_template("add_card.html", form=form)

@app.route("/delete_card/<int:botmcard_id>")
def delete_card(botmcard_id):
    card = Card.query.get(botmcard_id)

    if not card:
        return render_template("404.html")
    db.session.delete(card)
    db.session.commit()
    
    return redirect("/")

@app.route("/edit_product/<int:product_id>", methods=['GET', 'POST'])
def edit_product(product_id):
    product = Product.query.get(product_id)
    
    if not product:
        return render_template("404.html")

    form = AddProductFrom(name=product.name, text=product.text, image_url=product.image_url, price=product.price,)
    
    if form.validate_on_submit():
        product.name = form.name.data
        product.price = form.price.data
        product.text = form.text.data
        product.image_url = form.image_url.data
        
        db.session.commit()
        return redirect("/")
    
    return render_template("add_product.html", form=form)

    
@app.route("/delete_product/<int:product_id>")
def delete_product(product_id):
    product = Product.query.get(product_id)

    if not product:
        return render_template("404.html")
    
    db.session.delete(product)
    db.session.commit()
    
    return redirect("/")
        
@app.route("/delete_account/<int:user_id>")
def delete_account(user_id):
    user = User.query.get(user_id)

    if not user:
        return render_template("404.html")
    
    db.session.delete(user)
    db.session.commit()
    
    return redirect("/")

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")


@app.route("/success")
def success():
    return render_template("success.html")

@app.route('/football/<int:category_id>')
@app.route("/football")
def football(category_id = None):
    if category_id:
        products = Category.query.get(category_id).products
    else:
        products = Product.query.all()
    return render_template("football.html", products = products)