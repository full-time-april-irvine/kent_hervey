#this is the server file

from flask import Flask, render_template, request, redirect, session, flash, url_for
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
import re	# the regex module

app = Flask(__name__)

app.secret_key ='asdfeeffefa' 'keep it secret, keep it safe' # set a secret key for security purposes

#There are four routes:  /   /register  /login  /logout   /success
#there are two html pages that look different only by flash messages and personalization such as using users name and populated data fields
#reglog.html is used for 

# our index route will handle rendering our form

@app.route('/') # this route does not need to send anything to the reg-log.html page...at least not the first time
def index():

    return render_template("reglog.html") # This is the registration login form
 

@app.route('/register', methods=['POST'])  # this route shows up when the user clicks register and will send user to success, or if bad, then redirect
def register():

    if BAD:
        return redirect ("/")

    else: # input is good and we will write to database and show success page

        return redirect('/success') 
 

@app.route('/login', methods=['POST'])  # this route shows up when the user clicks login and will send user to success, or if bad, then redirect
def login():

    if BAD:
        return redirect ("/")

    else: # input is good and we will write to database and show success page

        return redirect('/success') 

@app.route('/success') #this route is the result of a redirect...so it renders a template, but also the user can use 5000/success as a bookmark as the entry place
def success():

    # check cookie to see if logged in

    # no cookie, then don't log in

    #use session to get id then go to database to pass name to display on success page

    return render_template("success-rl.html", name = name ) # This is the registration login form


@app.route('/logout', methods=['GET'])  # this route is the result of the user clicking anchor tag labeled "logout"
def logout():

    #Clear cookies and do flash message saying "You have been logged out"

    return redirect ("/")




if __name__ == "__main__":
    app.run(debug=True)