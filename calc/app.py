# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

# @app.route("/post/<int:id>")
# def find_post(id):
#     post = POSTS.get(id, "Post not found")
#     return f"<p>{post}</P>"


@app.route("/add")
def sum():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a, b)
    return str(result)


@app.route("/sub")
def res():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a, b)
    return str(result)


@app.route("/mult")
def mul():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a, b)
    return str(result)


@app.route("/div")
def di():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a, b)
    return str(result)


# <==========FURTHER STUDY==========>

operations = {
    "add": add,
    "sub": sub,
    "div": div,
    "mult": mult,
}


@app.route("/math/<oper>")
def operation(oper):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operations[oper](a, b)
    return str(result)
