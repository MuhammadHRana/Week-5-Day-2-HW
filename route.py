from flask import Flask

app = Flask(__name__)

@app.route("/")
def hw():
    return "<p>This is the HW assignment for Muhammad</p>"

@app.route("/hello")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye_world():
    return "<p>Bye, World!</p>"


@app.route("/welcome")
def welcome_world():
    return "<p>Welcome, World!</p>"
