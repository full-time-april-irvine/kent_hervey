#this is the server file

from flask import Flask, render_template, request, redirect, session, flash, url_for
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
import re	# the regex module


app = Flask(__name__)

app.secret_key ='asdfeeffefa' 'keep it secret, keep it safe' # set a secret key for security purposes

# our index route will handle rendering our form

@app.route('/') # this route does not need to send anything to the survey form
def index():

    return render_template("index.html")
 


@app.route('/users', methods=['POST'])  # this page will send user to success, or re-do
def create_user():

    email_from_form = request.form['email']  #validity:  use regex to match


    #print(name_from_form, location_from_form, language_from_form, comment_from_form)




    # create a regular expression object that we'll use later   
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

    if not EMAIL_REGEX.match(email_from_form):    # test whether a field matches the pattern
        flash("Invalid email address!")
        print("you should have entered something")
        return redirect ("/")
    else:  





        mysql = connectToMySQL("emai_val")

        query = "INSERT INTO email_table (email, created_at) VALUES(%(email_bydata)s, NOW())"

        data = { 
        "email_bydata": email_from_form,

        }

        connectToMySQL("emai_val")
        mysql.query_db(query, data)

        flash("Data added")

        mysql = connectToMySQL("emai_val")
        all_users = mysql.query_db("SELECT * FROM email_table;")


        return render_template("success.html" , email_on_template=email_from_form, return_users=all_users)
#, email_on_template=email_from_form      , all_users


if __name__ == "__main__":
    app.run(debug=True)