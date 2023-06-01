from flask import Flask, Blueprint, render_template, request, jsonify, redirect, url_for
ButtonPressed = 0 

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name="Joe", age=21)

@views.route("/json")
def get_json():
    return jsonify({'name': 'tim', 'coolness': 10})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))

@views.route("/sign-up/", methods=["GET","POST","DIALOG"])
def sign_up():
    return render_template("signup.html")

@views.route("/", methods=['POST'])
def get_form():
    username = request.form['sign_up']
    print(username)
    if not username == None:
        signed_up = True
    else:
        signed_up = False
    return render_template("index.html")

@views.route("/profile")
def profile():
        return render_template("profile.html",)
