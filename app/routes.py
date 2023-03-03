from flask import render_template, flash, redirect
from app import app
from app.forms import RegisterForm, SignInForm, Car_Form
from app.models import User

@app.route('/')
def index():
    cdn={
        'Homepage': ('Car')
    }
    return render_template('index.jinja', cdn=cdn, title='Home')

@app.route('/login')
def login():
    form = SignInForm()
    if form.validate_on_submit():
        flash(f'{form.username} successfully signed in!')
        return redirect('/')
    return render_template('login.jinja', form = SignInForm())

@app.route('/register')
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username= form.username.data
        email= form.email.data
        password= form.password.data

        u = User(username=username,email=email,password_hash=password)
        user_match = User.query.filter_by(username=username).first()
        if not user_match:
            u.commit()
            flash(f'Request to register {form.username} successful')
            return redirect('/')
        flash(f'Username{username} already exists, try again')
        return redirect('/sign_up')
    return render_template('register.jinja', form=form)

@app.route('/about')
def about():

    return render_template('about.jinja')

@app.route('/blog')
def blog():

    return render_template('blog.jinja')

@app.route('/car')
def cars():
    form = Car_Form()
    if form.validate_on_submit():
        flash(f'{form.username} successfully signed in!')
        return redirect('/')
    return render_template('car.jinja', form=form)
