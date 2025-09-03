from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {
        'username': 'Charlie',
        'age': 24,
        }
    posts = [
        {
            'author': {'username': 'Charlie'},
            'body': '''I'm learning to code a website!''',
        },

        {
            'author': {'username': 'Jeff'},
            'body': 'My name Jeff',
        },
        {
            'author': {'username': 'Sponge Bob'},
            'body': 'I love Krabby Patties!'
        }
    ]
    contact = {
        'email': 'charlieclark17@gmail.com'
    }
    return render_template(
        'index.html', title='Home', user=user, posts=posts, contact=contact)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
