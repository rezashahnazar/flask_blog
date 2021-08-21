from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ['FL_SECRET_KEY']
# Use python shell secrets.token_hex(length) to generate

posts = [
    {
        'author': 'Reza Shahnazar',
        'title': 'Blog post 1',
        'content': 'Content of post 1',
        'date': 'Mordad 30 1400'
    },
    {
        'author': 'Ali Karimi',
        'title': 'Blog post 2',
        'content': 'Content of post 222',
        'date': 'Mordad 31 1400'
    }
]


@app.route("/")
def home():
    return render_template('home.html', posts=posts, title="Blog Home")


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)
