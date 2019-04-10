from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection

app = Flask(__name__)


@app.route('/')
def index():
    mysql = connectToMySQL("create_read_pets")
    all_pets = mysql.query_db("SELECT * FROM pets;")
    print("*"*80)
    print("this is all the pets", all_pets)
    return render_template("create_read.html", all_pets=all_pets)
            

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