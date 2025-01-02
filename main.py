from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return "<h1>Home Page</h1>"

@app.route("/contact")
def contact():
    return "<h1>Contact Page</h1>"






if __name__ == '__main__':
    app.run(debug=True)