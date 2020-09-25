from flask import Flask, render_template  # pip install flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return "hello world"


@app.route("/clock")
def clock():
    t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", time=t)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

