from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection

app = Flask(__name__)

#Database name:  user_assignment
#Table name:  user_table
#Field names:
#id | fname   | lname | email            | created_at          | updated_at



@app.route('/users/new', methods=["GET"]) #	/users/new- GET - method should return a template containing the form for adding a new user
def new_user():
    mysql = connectToMySQL("create_read_pets")
    #all_pets = mysql.query_db("SELECT * FROM pets;")
    print("*"*80)
    #print("this is all the pets", all_pets)

    return render_template("create.html")
            
####################################################################

@app.route('/users/create', methods=["{POST}"])     # 	/users/create - POST - method should add the user to the database, then redirect to /users/<id>
def create_user():

    return redirect("users/<id>")

####################################################################

@app.route('/users/<id>', methods=["{GET}"])     #	/users/<id> - GET - method should return a template that displays the specific user's information
def specific_user():

    return render_template("readone.html")

####################################################################

@app.route('/users', methods=["{GET}"])   #  /users - GET - method should return a template that displays all the users in the table
def all_user():

    return render_template("readall.html")

####################################################################

@app.route('/users/<id>/edit', methods=["{GET}"]) #  	/users/<id>/edit - GET - method should return a template that displays a form for editing the user with the id specified in the url
def edit_user():

    return render_template("update.html")

####################################################################

@app.route('/users/<id>/update', methods=["{POST}"])  # /users/<id>/update - POST - method should update the specific user in the database, then redirect to /users/<id>
def update_specific_user():

    return redirect("users/<id>")

####################################################################

@app.route('/users/<id>/destroy', methods=["{GET}"])  # /users/<id>/destroy - GET - method should delete the user with the specified id from the database, then redirect to /users
def delete_specific_user():

    return redirect("users")

####################################################################
####################################################################

@app.route("/create", methods=["POST"])
def create():
    mysql = connectToMySQL("create_read_pets")

    query = "INSERT INTO pets (name, type, created_at, updated_at) VALUES(%(pn)s, %(pt)s, NOW(), NOW())"

    data = { 
        "pn": request.form["pet_name_submitted"],
        "pt": request.form["type_submitted"],
    }

    mysql = connectToMySQL("create_read_pets")
    mysql.query_db(query, data)

    return redirect("/")


















if __name__ == "__main__":
    app.run(debug=True)