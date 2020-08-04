from flask import Flask, redirect, render_template, request
from helpers.student_query import select, insert


app = Flask(__name__)


@app.route("/")
def index():
    rows = select()
    return render_template("index.html", rows=rows)


@app.route("/enroll", methods=["POST"])
def enroll():
    name = request.form.get("name")
    email = request.form.get("email")
    password = request.form.get("password")
    insert(name, email, password)
    return redirect("/")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
