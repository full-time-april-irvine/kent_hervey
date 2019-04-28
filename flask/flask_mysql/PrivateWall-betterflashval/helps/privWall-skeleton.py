#this is the server file

from flask import Flask, render_template, request, redirect, session, flash, url_for
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
import re	# the regex module

app = Flask(__name__)

app.secret_key ='asdfeeffefa' 'keep it secret, keep it safe' # set a secret key for security purposes

#There are four routes:  /   /wall  /register   /login  /logout   /wall (similar to success) also, maybe /messDelete   /messageSend
#               / is the root route and renders the registration/login page
#               /wall seems to be about rendering the messages.html page that could also be called the messages page
#                    the /wall route receives from other active routes because when they get their actions done, then they will go there, probably, particularly login and registration (since it has built in login for first time users)
#                     the /wall route needs information at its start, particularly it needs the user's ID so it can populate the messages, also since users don't send messages to themselves, it needs to the users id so as not to include on the Send side
#               /register seems to be needed to catch the forms sent from the register side of the reglogPW.html page (typically the index page)
#                            will redirect to the /wall route 
#               /login seems to be needed to catch the forms sent from the login side of the reglogPW.html page (typically the index page)
#                  /logout would do just that: log the user out, and send some place safe and useful...like the root route which then renders the reglogPW.html
#               
#there are two html pages that look different only by flash messages and personalization such as using users name and populated data fields
    #reglogPW.html is used for registration and login
    #messages.html is used for displaying messages belonging to the viewer
    #           is also used for sending messages to any other member



@app.route('/') # this route renders to reglogPW.html. It does not send any data to it,but might want to set some cookies for registration re-attempts
def index():

    return render_template("reglogPW.html") # This is the registration login form
 

@app.route('/register', methods=['POST'])  # this route shows up when the user clicks register and will send user to /wall, or if bad, then redirect to /
def register():

    if BAD:
        return redirect ("/")

    else: # input is good and we will write to database and show success page

        return redirect('/wall') 
 

@app.route('/login', methods=['POST'])  # this route shows up when the user clicks login and will send user to /wall, or if bad, then redirect to /
def login():

    if BAD:
        return redirect ("/")

    else: # input is good and we will write to database and show success page

        return redirect('/wall') 

@app.route('/wall') #this route is the result of a redirect...so it renders a template, but also the user can use 5000/wall as a bookmark as the entry place which will only work if they are still logged in
def wall():

    # check cookie to see if logged in

    # no cookie, then don't log in

    #use session to get id then go to database to pass name to display on success page

    return render_template("messages.html", name = name )


@app.route('/logout', methods=['GET'])  # this route is the result of the user clicking anchor tag labeled "logout"
def logout():

    #Clear cookies and do flash message displaying on reglogPW.html saying "You have been logged out"

    return redirect ("/")




if __name__ == "__main__":
    app.run(debug=True)