from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def add_input():
    """Add a and b parameters"""
    # Convert string to numbers
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = add(a, b)

    return f"<h1>{result}</h1>"


@app.route('/sub')
def sub_input():
    """Subtract a and b parameters"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a, b)

    return f"<h1>{result}</h1>"


@app.route('/mult')
def mult_input():
    """Multiply a and b parameters"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a, b)

    return f"<h1>{result}</h1>"


@app.route('/div')
def div_input():
    """Divide a and b parameters"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = div(a, b)

    return f"<h1>{result}</h1>"

# FURTHER STUDY


MATH = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}


@app.route('/math/<operator>')
def do_math(operator):
    """Do math to a and b parameters"""
    a = int(request.args['a'])
    b = int(request.args['b'])

    math = MATH[operator]
    result = math(a, b)

    return f"<h1>{result}</h1>"
