from flask import Flask, render_template, request, redirect, session, flash, url_for
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
import re	# the regex module
from flask_bcrypt import Bcrypt 

import sys; 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
SCHEMA_NAME = "private_wall"

app = Flask(__name__)

app.secret_key ='asdfeeffefa' 'keep it secret, keep it safe' # set a secret key for security purposes
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
                         # which is made by invoking the function Bcrypt with our app as an argument

#There are four routes:  /   /wall  /register   /login  /logout   /wall (similar to success) also, maybe /messDelete   /messSend
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

    if "form" not in session: #this is about populating and retrieving registration field data.  Ex:  "fname_submitted" is value in first name field
        dataNameEmail= {
            "fname_submitted": "",
            "lname_submitted": "",
            "email_submitted":  ""
        }
        session['form'] = dataNameEmail

        print("-"*80)
        print(dataNameEmail)
        print(session['form'])



    return render_template("reglogPW.html") # This is the registration login form
 

@app.route('/register', methods=['POST'])  # this route shows up when the user clicks register and will send user to /wall, or if bad, then redirect to /
def register():



    dataNameEmail= {
        "fname_submitted": request.form['fname_submitted'],
        "lname_submitted": request.form['lname_submitted'],
        "email_submitted": request.form["email_submitted"]
    }
    session['form'] = dataNameEmail

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
 
    if (len(request.form['pw_submitted']) < 7):
        flash("password must be at least 7 characters", "register")
        return redirect ("/")

    if (request.form['pw_submitted'] !=  request.form['pwconf_submitted']):
        flash("confirmation password did not match", "register")
        return redirect ("/")

    retrievedEmail =  request.form['email_submitted'] 

    print("retrievedEmail ", retrievedEmail)

    mysql = connectToMySQL(SCHEMA_NAME)

    query = "select * from users where email=%(em)s;"


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

    query = "INSERT INTO users (fname, lname, email, pw_hash, created_at, updated_at) VALUES(%(fname_bydata)s, %(lname_bydata)s, %(email_bydata)s, %(pw_has_bydata)s, NOW(), NOW());"

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

    return redirect('/wall') 
 # end /register route

@app.route('/login', methods=['POST'])  # this route shows up when the user clicks login and will send user to /wall, or if bad, then redirect to /
def login():

    print(request.form)
    #print(request.form[0])

    login_email=request.form['log_email_submitted']
    login_pw=request.form['log_pw_submitted']
    if login_pw=="": # if password field is blank, then bcrypt returns an error, so at least for testing time...
        login_pw="55"

    hashed_login_pw=bcrypt.generate_password_hash(login_pw) 

    print("email, pw, hashed pw  "  + login_email +  login_pw, hashed_login_pw) 

    # Check whether the email provided is associated with a user in the database
    # If it is, check whether the password matches what's saved in the database
    # input is good and we will write to database and show success page
    mysql = connectToMySQL(SCHEMA_NAME)
    query = "select * from users where email=%(em)s;"
    print("query is  ", query)
    data = {
        "em": login_email
    }
    result = mysql.query_db(query, data)
    if len(result)<1:
        print("evil hacker with fake email")
        flash("You could not be logged in", "login")
        return redirect ("/")
    print("r"*70)
    print(type(result))
    matched_hashed_pw=result[0]['pw_hash']
    print(type(matched_hashed_pw))
    print("result with key and value: "  + str(result))
    print("matching hashed PW:  " +  str(result[0]['pw_hash']))
    print("variable matched_hashed_pw:  " + str(matched_hashed_pw))

    if bcrypt.check_password_hash(matched_hashed_pw,login_pw):
        print("we got a match")
        session['user_id'] = result[0]['id']
        print("so cookie id is: " + str(session['user_id']))
        flash("You were logged in", "login")
        session['session_fname'] = result[0]['fname'] #storing first name of logged in user for handy retrieval from html pages
        return redirect('/wall') 
    else:
        print("evil hacker")
        flash("You could not be logged in", "login")

        return redirect ("/")
    # End /login route

@app.route('/wall') #like a success route this route is the result of a redirect...so it renders a template, but also the user can use 5000/wall as a bookmark as the entry place which will only work if they are still logged in
def wall():
    # check cookie to see if logged in
    # no cookie, then not  logged in

    if 'user_id' not in session:
        print("key 'user_id' does NOT exist")
        flash("You must be logged in to enter this website", "login")

        return redirect ("/")
    else:
        print('key user_id exists!')

        #Need to prepopulate the web page so it displays properly.
        #What needs populating?

        ### 1st   first the Send Messages side is expecting a dictionary called the_users and fields: fname which is recipient's namme
        #  user.id which is recipient's id needed for sending the message

        mysql = connectToMySQL(SCHEMA_NAME)

        # != user id elimates logged in user from sending to himself
        query = "select fname, users.id from users where users.id != %(ui)s order by fname asc;"

        print("query is  ", query)

        data = {
            "ui": str(session['user_id'])
        }
        the_users = mysql.query_db(query, data)
        #matching_users = mysql.query_db(query)
        print(the_users)

        #Ninja Bonus to display number of messages logged in user has sent
        mysql = connectToMySQL(SCHEMA_NAME)
        query = "select sender_id from messages WHERE sender_id=%(ui)s;"

        print("query is  ", query)

        data = {
            "ui": str(session['user_id']) #logged in user id
        }
        
        sentCount = mysql.query_db(query, data)
        numberUserSent=len(sentCount)        
        print(sentCount)
        print("+"*76)







        ###2nd Prepopulate the RX messages side

        mysql = connectToMySQL(SCHEMA_NAME)
        #query = "select message_content, users.fname, messages.created_at, messages.id from messages JOIN users on messages.sender_id =users.id where messages.sender_id != %(ui)s order by users.fname asc;"
        query = "select message_content, users.fname, messages.created_at, messages.id from messages JOIN users on messages.sender_id =users.id where messages.receiver_id = %(ui)s order by users.fname asc;"

        print("RX messages query is  ", query)

        data = {
            "ui": str(session['user_id'])
        }
        send_users = mysql.query_db(query, data)
        print("send users result:  "  + str(send_users) + "note that eliminated sender id is:  "  + str(session['user_id']))

        numberRXmess=len(send_users)
        print(numberRXmess)

    # all_users = [ 
    # {'sender_id': 1, 'receiver_id': 8,'fname': 'Andrew', 'lname': 'Lee', 'email': 'alee@gmail.com', 'message_content': 'blah blah 11111 11111 11111 1111', 'messageID': 3}, 
    # {'sender_id': 2, 'receiver_id': 8,'fname': 'Jay', 'lname': 'Patel', 'email': 'jpatel@gmail.com', 'message_content': 'blah blah 222 22222 11111 1111', 'messageID': 3,},
    #  {'sender_id': 2, 'receiver_id': 8,'fname': 'Jay', 'lname': 'Patel', 'email': 'jpatel@gmail.com', 'message_content': 'blah blah 222 22222 11111 1111', 'messageID': 5}
    # ]  

    return render_template("messages.html", return_users = the_users, the_senders=send_users, numberRXmess=numberRXmess, sentCount=numberUserSent )
# end /wall route

@app.route('/messSend', methods=['POST'])  # this route's purpose is to send the indicated message, then return back to the /wall route to re-render messages.html
def messSend():
    print("entering message send")
    #What must be done:
    #Make sure the route has access to what is needed for the send.  That should be:  receiver id, sender id, and message content..so how to get those:
    #  sender id is the logged in user so that is available from a session cookie
    #  receiver id is available from the form submitted, so via hidden tag and via request.form
    #  message content is also available from form submitted so request.form
    #then....build INSERT query tht inserts the new message in the message table.  What does the message table need?
    #  sender id, and receiver id and message content...then the two date fields supplied with NOW()


    mysql = connectToMySQL(SCHEMA_NAME)

    query = "INSERT INTO messages (sender_id, receiver_id, message_content, created_at, updated_at) VALUES(%(sbyd)s, %(rbyd)s, %(messbyd)s,  NOW(), NOW());"

    data = { 
        "sbyd": str(session['user_id']),
        "rbyd": request.form['recipientID'],
        "messbyd": request.form['sentMessageContent'],
    }

    print("data is:  " + str(data))

    new_message_id = mysql.query_db(query, data) 
    #new_message_id = mysql.query_db(query) 

    print ("message id of the newly sent message  " + str(new_message_id) )


    return redirect ("/wall")
    # End /messSend route


@app.route('/logout', methods=['GET'])  # this route is the result of the user clicking anchor tag labeled "logout"
def logout():

    #Clear cookies and do flash message displaying on reglogPW.html saying "You have been logged out"

    print("are we in logout?")
    #Clear cookies and do flash message saying "You have been logged out"
    session.pop('user_id')
    session.pop('session_fname')
    flash("You have been logged out", "logout")
    return redirect ("/")
# end logout route


@app.route('/messDelete/<messID>', methods=['GET'])  # GET because URL this route shows up when the user clicks login and will send user to /wall, or if bad, then redirect to /
def messDelete(messID): #deletes message from database's message table with messages.id=messID
    print("addddsdf")
    print("we want to delete message:  " + str(messID))

#Sensei bonus would go here to confirm message receiver matches login ID.  If not, then he says send to web page/another route, but could just do flash message after logging out

    mysql = connectToMySQL(SCHEMA_NAME)


    query = "select receiver_id from messages  where messages.id = %(ui)s ;"
    data = {
        "ui": str(messID)
    }
    messIDcheck = mysql.query_db(query, data)

    if session['user_id'] != messIDcheck:
        flash("You tried to delete somebody else's message...very bad", "success")
        return redirect ("/wall")

    mysql = connectToMySQL(SCHEMA_NAME)
    query = " delete from messages WHERE id=%(id_bydata)s;"
    data = { 
        "id_bydata": int(messID), 
    }
    mysql.query_db(query, data)

    return redirect('/wall') 


if __name__ == "__main__":
    app.run(debug=True)