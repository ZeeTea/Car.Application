from . import bp as auth_bp
from app.forms import RegisterForm, SignInForm
from main.models import User
from flask import render_template, redirect, flash

@auth_bp.route('/login')
def login():
    form = SignInForm()
    if form.validate_on_submit():
        flash(f'{form.username} successfully signed in!')
        return redirect('/')
    return render_template('login.jinja', form=form)

@auth_bp.route('/register')
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username= form.username.data
        first_name= form.first_name.data
        last_name= form.last_name.data
        email= form.email.data
        password= form.password.data

        u = User(username=username,first_name=first_name,last_name=last_name,email=email,password_hash=password)
        user_match = User.query.filter_by(username=username).first()
        if not user_match:
            u.commit()
            flash(f'Request to register {form.username} successful')
            return redirect('/')
        flash(f'Username{username} already exists, try again')
        return redirect('/sign_up')
    return render_template('register.jinja', form=form)
