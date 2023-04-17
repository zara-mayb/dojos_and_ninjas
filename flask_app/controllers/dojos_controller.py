from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo

@app.route("/dojos/", methods = ["GET"])
def dojos():
    return render_template("dojos.html", dojos = Dojo.get_all())

@app.route("/dojos/add", methods = ["POST"])
def add():
    add_dojo = {
        "name": request.form["name"]
    } 
    Dojo.save(add_dojo)
    return redirect("/dojos")

@app.route ("/ninjas")
def add_ninja_form():
    dojos = Dojo.get_all()
    return render_template("new_ninja.html", dojos = dojos)

@app.route("/dojos/show/<int:id>")
def show(id):
    data = {
        "id": id
    }
    ninjas = Dojo.get_ninjas_one_dojo(data)
    return render_template("show.html", ninjas = ninjas)
