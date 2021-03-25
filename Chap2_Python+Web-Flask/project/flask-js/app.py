from flask import Flask, render_template, request  # pip install flask
from flask_login import LoginManager, UserMixin
from datetime import datetime
from flask_login.utils import login_user
from dataclasses import dataclass


@dataclass
class User(UserMixin):
    id: str
    password: str


app = Flask(__name__)
app.config["SECRET_KEY"] = "시크릿키"
login_manager = LoginManager()


@app.route("/")
def index():
    return "hello world"


@app.route("/clock")
def clock():
    t = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", time=t)


@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login_post():
    print("POST 요청")
    user = User("anonymous", "password")
    login_user(user)
    print(user.is_active)
    return render_template("login.html")


@app.route("/board", methods=["GET"])
def board():
    return render_template("board.html")


@app.route("/board", methods=["POST"])
def board_post():
    body = request.get_json()
    print("POST REQUEST", type(body), body)
    return "Saved!"


if __name__ == "__main__":
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        print(user_id)
        user = User("anonymous", "password")
        return user

    app.run(host="0.0.0.0", debug=True)
