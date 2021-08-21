from flask import Flask, render_template, url_for

app = Flask(__name__)

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
def hello():
    return render_template('home.html', posts=posts, title="Blog Home")


@app.route("/about")
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
