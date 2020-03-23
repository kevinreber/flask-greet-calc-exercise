from flask import Flask

app = Flask(__name__)


@app.route("/welcome")
def welcome():
    """Welcome screen"""
    return "<h1>Welcome!</h1>"


@app.route("/welcome/home")
def welcome_home():
    """Welcome home"""
    return "<h1>Welcome Home!</h1>"


@app.route("/welcome/back")
def welcome_back():
    """Welcome back"""
    return "<h1>Welcome Back!</h1>"
