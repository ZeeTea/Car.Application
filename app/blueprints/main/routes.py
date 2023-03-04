from app.forms import Car_Form
from . import bp as main_bp
from flask import render_template, flash, redirect

@main_bp.route('/')
def index():
    cdn={
        'Homepage': ('Car')
    }
    return render_template('index.jinja', cdn=cdn, title='Home')

@main_bp.route('/about')
def about():

    return render_template('about.jinja')

@main_bp.route('/blog')
def blog():

    return render_template('blog.jinja')

@main_bp.route('/car')
def cars():
    form = Car_Form()
    if form.validate_on_submit():
        flash(f'{form.username} successful!')
        return redirect('/')
    return render_template('car.jinja', form=form)
