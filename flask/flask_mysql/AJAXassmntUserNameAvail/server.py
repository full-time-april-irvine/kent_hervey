#this is the server file

from flask import Flask, render_template, request, redirect, session, flash, url_for
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
import re	# the regex module
from flask_bcrypt import Bcrypt 

import sys; 


SCHEMA_NAME="ajaxwall"

app = Flask(__name__)


  
@app.route('/') # this route does not need to send anything to the reg-log.html page...at least not the first time
def index():


    return render_template("register.html") # This is the registration login form
 

@app.route('/register', methods=['POST'])  # this route shows up when the user clicks register and will send user to success, or if bad, then redirect
def register():


    dataNameEmail= {
        "fname_submitted": request.form['username_form']

    }


    print("-"*80)
    print(dataNameEmail)
    print(session['form'])

    if (len(request.form['fname_submitted']) < 2 or not request.form['fname_submitted'].isalpha()):
        flash("name must be all alpha and at least 2 characters\n and check subsequent data entry fields", "register")
        return redirect ("/")

    if (len(request.form['lname_submitted']) < 2 or not request.form['lname_submitted'].isalpha()):
        flash("last name must be all alpha and at least 2 characters\n and check subsequent data entry fields", "register")
        return redirect ("/")

    if not EMAIL_REGEX.match(request.form["email_submitted"]):    # test whether a field matches the pattern
        flash("Invalid email address!\n and check subsequent data entry fields", "register")
        print("you should have entered something")
        return redirect ("/")
 
    if (len(request.form['pw_submitted']) < 8):
        flash("password must be at least 8 characters", "register")
        return redirect ("/")

    if (request.form['pw_submitted'] !=  request.form['pwconf_submitted']):
        flash("confirmation password did not match", "register")
        return redirect ("/")

    retrievedEmail =  request.form['email_submitted'] 

    print("retrievedEmail ", retrievedEmail)

    mysql = connectToMySQL(SCHEMA_NAME)
    #query = "SELECT * from validatedusers;"
    #query = "select * from validated_users where email='%(em)s';"
    query = "select * from validated_users where email=%(em)s;"
    #query = "SELECT * FROM validated_users WHERE email =" + retrievedEmail 

    print("query is  ", query)

    print("email should be:  " + request.form['email_submitted'])

    data = {
        "em": retrievedEmail
    }
    matching_users = mysql.query_db(query, data)
    #matching_users = mysql.query_db(query)

    print("data is:  ", data)


    #all_users = mysql.query_db(query)
    print("*"*80)
    print("all users ", matching_users)
    print("*"*80)

    if not matching_users:
        print("no email match")
    print("next line should give length of matching_users")
    print(len(matching_users))

    lengthMatchingUsers =len(matching_users)
    print("next line should give length of matching_users")
    print(lengthMatchingUsers)

    if lengthMatchingUsers>0:
        print("email already exists")
        flash("Entered email already exists.  Mabybe you are already registered.  Else, use another email address", "register")
        return redirect ("/")

    pw_hash = bcrypt.generate_password_hash(request.form['pw_submitted'])  
    print("hashed password is: ", pw_hash) 


    # input is good and we will write to database and show success page--Don't need or have an else because all invalids have already resulted in returns
 
    mysql = connectToMySQL(SCHEMA_NAME)

    query = "INSERT INTO validated_users (fname, lname, email, pw_hash, created_at, updated_at) VALUES(%(fname_bydata)s, %(lname_bydata)s, %(email_bydata)s, %(pw_has_bydata)s, NOW(), NOW())"

    data = { 
        "fname_bydata": request.form["fname_submitted"],
        "lname_bydata": request.form["lname_submitted"],
        "email_bydata": request.form["email_submitted"],
        "pw_has_bydata": pw_hash
    }

    new_user_id = mysql.query_db(query, data) 
    session['user_id'] = new_user_id
    session['session_fname'] = request.form["fname_submitted"]

    print ("session stored user id is now:  " + str(session['user_id']) + "and name is: " + session['session_fname'])

    flash("You have been successfully registered", "success")
    #Also should remove session cookie holding name and email from html form
    #    as in:  
    session.pop('form')  #but it can be done at top of success page

    return redirect('/success') 
# End registration

#######################
#################
@app.route("/username", methods=['POST'])
def username():
    found = False
    SCHEMA_NAME="ajaxwall"
    print("schema is:  " + SCHEMA_NAME)
    mysql = connectToMySQL(SCHEMA_NAME)        # connect to the database
    query = "SELECT username from users WHERE users.username = %(user)s;"
    data = { 'user': request.form['username'] }
    result = mysql.query_db(query, data)
    if result:
         found = True
    return render_template('partials/username.html', found=found)  # render a partial and return it


@app.route('/success')
def success():

    # check cookie to see if logged in
    # no cookie, then not  logged in

    if 'user_id' not in session:
        print("key 'user_id' does NOT exist")
        flash("You must be logged in to enter this website", "login")

        return redirect ("/")
    else:
        print('key user_id exists!')



    #use session to get id then go to database to pass name to display on success page
    return render_template("success-rl.html" ) # This is the registration login form







if __name__ == "__main__":
    app.run(debug=True)