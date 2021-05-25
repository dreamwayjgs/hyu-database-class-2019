from flask import Flask, render_template, request
import json

from flask.json import dump


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/greet")
def greet():
    return json.dumps({"hello": "world"})


@app.route("/order", methods=["POST"])
def order():
    print(request.get_json())
    print(request)
    data = {"greet": "hello", "timestamp": "오늘"}
    print(type(data), data)
    dumped = json.dumps(data)
    print(type(dumped), dumped)
    loaded = json.loads(dumped)
    print(type(loaded), loaded)
    return "OK"


@app.route("/order", methods=["PUT"])
def xxx():
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
