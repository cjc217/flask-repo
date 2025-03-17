from flask import render_template
from app import app


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
        }
    ]
    contact = {
        'email': 'charlieclark17@gmail.com'
    }
    return render_template(
        'index.html', title='Home', user=user, posts=posts, contact=contact)
