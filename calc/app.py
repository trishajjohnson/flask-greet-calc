# Put your app in here.
from flask import Flask, request

from operations import add, sub, div, mult

app = Flask(__name__)

# @app.route('/add')

# # Original solution
# # def add_nums():
# def do_add():

#     """Adds a and b"""

#     a = int(request.args.get("a"))
#     # a = int(request.args["a"])
#     b = int(request.args.get("b"))
#     # b = int(request.args["b"])
#     result = add(a, b)

#     return str(result) 
#     # return f"{a} + {b} = {result}" 

# @app.route('/subtract')
# def subtract_nums():

#     # original solution framework
#     """Subtracts a and b"""

#     # Instead of a = int(request.args.get("a")

#     a = int(request.args["a"])
#     b = int(request.args["b"])

#     # Instead of turning result into string
#     result = sub(a, b)

#     return result
#     # Originally returned a f-string instead of "return = result"
#     # return f"{a} - {b} = {result}" 

# @app.route('/multiply')
# def mult_nums():

#     """Multiplies a and b"""

#     a = int(request.args["a"])
#     b = int(request.args["b"])
#     result = mult(a, b)

#     return str(result) 
#     # return f"{a} x {b} = {result}" 

# @app.route('/divide')
# def div_nums():

#     """"Divides a and b"""

#     a = int(request.args["a"])
#     b = int(request.args["b"])
#     result = div(a, b)

#     return str(result)
#     # return f"{a} / {b} = {result}" 

# Original Solution

# @app.route('/<operation>')
# def do_operation(operation):
    # """Creating function to do given operation to given numbers a and b"""

#     a = int(request.args.get("a"))
#     b = int(request.args.get("b"))

#     result = operation(a, b)

#     return result

operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)