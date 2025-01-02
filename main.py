from flask import Flask
from flask import render_template

app = Flask(__name__)

posts = [
    {
        'author': 'Vinay Hegde',
        'title': 'My First Blog',
        'content': 'Some Content',
        'date_posted': 'January 02, 2025'
    },
    {
        'author': 'test',
        'title': 'test blog',
        'content': 'other Content',
        'date_posted': 'January 02, 2025'
    }
]


@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')






if __name__ == '__main__':
    app.run(debug=True)