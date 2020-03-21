from flask import Flask, render_template, request
# import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return("<h1>you are so beautiful</h1>")

# @app.route("/")
# def index():
#     headline = "made by vungo"
#     return render_template("index.html", headline = headline)
#
# @app.route("/<string:name>")
# def troll(name):
#     return(f"<h1>you are so beautiful, {name}</h1>")
#
# @app.route("/bye")
# def bye():
#     headline = "bye"
#     return render_template("index.html", headline = headline)
#
# @app.route("/isnewyear")
# def isnewyear():
#     now = datetime.datetime.now()
#     new_year = now.month == 1 and now.day == 1
#     return render_template("is_new_year.html", new_year = new_year)
#
# @app.route("/loop")
# def loop():
#     names = ['Vu', 'Tien', 'The']
#     return render_template("loop.html", names = names)
#
# @app.route("/more")
# def more():
#     return render_template("more.html")
#
# @app.route("/hello", methods = ["GET", "POST"])
# def hello():
#     if request.method == "GET":
#         return "please submit information in homepage first"
#     else:
#         name = request.form.get("name")
#         return render_template("hello.html", name = name)
