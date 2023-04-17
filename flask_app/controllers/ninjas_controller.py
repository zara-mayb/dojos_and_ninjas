from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninja

@app.route ("/ninjas_add", methods = ["POST"])
def add_ninja():
    new_ninja = {
        "dojo_id": request.form["dojo_id"],
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"]
    }
    Ninja.save(new_ninja)
    return redirect("/ninjas")