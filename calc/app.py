# Put your app in here.
from flask import Flask, request

from operations import add, sub, div, mult

app = Flask(__name__)

@app.route('/add')
def add_nums():

    """Adds a and b"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    result = add(a, b)

    return f"{a} + {b} = {result}" 

@app.route('/sub')
def subtract_nums():

    """Subtracts a and b"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    result = sub(a, b)

    return f"{a} - {b} = {result}" 

@app.route('/mult')
def mult_nums():

    """Multiplies a and b"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    result = mult(a, b)

    return f"{a} x {b} = {result}" 

@app.route('/div')
def div_nums():

    """"Divides a and b"""

    a = int(request.args["a"])
    b = int(request.args["b"])

    result = div(a, b)

    return f"{a} / {b} = {result}" 

@app.route('/math/<operation>')
def do_operation(operation):

    """Creating function to do given operation to given numbers a and b"""

    operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

    a = int(request.args["a"])
    b = int(request.args["b"])

    result = operators[operation](a, b)

    return str(result)
