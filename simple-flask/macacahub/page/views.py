from flask import Blueprint, request

blueprint = Blueprint("page", __name__)


@blueprint.route("/")
def index():
    return "Hello MacacaHub!! meow~"


@blueprint.route("/magic")
def magic():
    a = request.args.get("a", 0)
    b = request.args.get("b", 0)
    c = int(a) + int(b)
    return str(c)
