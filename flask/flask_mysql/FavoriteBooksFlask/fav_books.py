from flask import Flask, render_template, request, redirect, session, flash, url_for
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
import re	# the regex module
from flask_bcrypt import Bcrypt 

import sys; 

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
SCHEMA_NAME = "favoritebooks"

app = Flask(__name__)

app.secret_key ='asdfeeffefa' 'keep it secret, keep it safe' # set a secret key for security purposes
bcrypt = Bcrypt(app)     # we are creating an object called bcrypt, 
                         # which is made by invoking the function Bcrypt with our app as an argument

#603-
#There routes:  /     /register  /login  /books - /addbook  /doFavorite/<bookID>   /books/<bookID> -   /updateDescription<bookID>      /unfavorite/<bookID>  /logout
#               / is the root route and renders the registration/login page
#               /register seems to be needed to catch the forms sent from the register side of the reglogPW.html page (typically the index page) 
#                       redirects to /books if success, or back to / if fail
#               /login seems to be needed to catch the forms sent from the login side of the reglogPW.html page (typically the index page)
#                       redirects to /books if success, or back to / if fail
#               /books   is about rendering the allBooks.html page....the success page   
#               /addbook is aobut adding a book to books table
#               /doFavorite/<bookID> receives form from allBooks.html and oneBook.html, performs a favorting action in favoites table database and redirects to /books
#               /books/<bookID> is about rendering the oneBook.html page....
#               /updateDescription<bookID> 
#               /unfavorite>/<bookID> receives form from oneBook.html, performs action in database and redirects to /books
#               /logout would do just that: log the user out, and send some place safe and useful...like the root route which then renders the reglogPW.html
#               
#there are three html pages that look different only by flash messages and personalization such as using users name and populated data fields
    #reglogFav.html  or index.html is used for registration and login WH users_new
    #allBooks.html  or books_index.html is used for displaying All books whether favorited or not  This is a success page  WH:  call it books_index
    #oneBook.html   or book_show displays single book  WH:  books_show



@app.route('/') 
def index():
    pass
    # This will render the login and registration page
    # return render_template("")

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



    return render_template("reglogFav.html") # This is the registration login form
 

@app.route('/register', methods=['POST'])  # this route shows up when the user clicks register and will send user to /wall, or if bad, then redirect to /
def register():

    dataNameEmail= {
        "fname_submitted": request.form['fname_submitted'],
        "lname_submitted": request.form['lname_submitted'],
        "email_submitted": request.form["email_submitted"]
    }
    session['form'] = dataNameEmail

    valid=True
    print("-"*80)
    print(dataNameEmail)
    print(session['form'])
    print("above should be catalog dateNameEmail followed by result of web form")

    if (len(request.form['fname_submitted']) < 2 or not request.form['fname_submitted'].isalpha()):
        valid=False
        flash("Name must be all alpha and at least 2 characters.", "register")


    if (len(request.form['lname_submitted']) < 2 or not request.form['lname_submitted'].isalpha()):
        valid=False
        flash("Last name must be all alpha and at least 2 characters.", "register")

    if not EMAIL_REGEX.match(request.form["email_submitted"]):    # test whether a field matches the pattern
        flash("Invalid email address!", "register")
        print("you should have entered something")

    if (len(request.form['pw_submitted']) < 8):
        flash("Password must be at least 7 characters.", "register")

    if (request.form['pw_submitted'] !=  request.form['pwconf_submitted']):
        flash("Confirmation password did not match.", "register")

    retrievedEmail =  request.form['email_submitted'] 

    print("retrievedEmail from webform ", retrievedEmail)

    mysql = connectToMySQL(SCHEMA_NAME)

    query = "select * from users where email=%(em)s;"

    print("query is  ", query)

    data = {
        "em": retrievedEmail
    }
    matching_users = mysql.query_db(query, data)

    print("data is:  ", data)
    print("next line prints matching_users: ")
    print(matching_users)

    print("next line should give length of matching_user...number of items in list")
    print(len(matching_users))

    if len(matching_users)>0: #alternate if len(matching_users)>0:   the other:  if len(matching_users)>0:  reason is that Python considers NONE to be false https://docs.python.org/2.4/lib/truth.html
        print("email already exists")
        print("*"*80)
        print("matching ", matching_users[0]['email'])
        print("*"*80)
        valid=False
        flash("Entered email already exists.  Mabybe you are already registered.  Else use another email address.", "register")

    print("valid is")
    print(valid)
    if(not valid):
        print("test")
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
    print("here"*80)
    return redirect('/books') 
 # end /register route

@app.route('/login', methods=['POST'])  # this route shows up when the user clicks login and will send user to /books, or if bad, then redirect to /
def login():
    print(request.form)
    #print(request.form[0])

    login_email=request.form['log_email_submitted']
    login_pw=request.form['log_pw_submitted']
    if login_pw=="": # validation prevents blank password, but if it were bcrypt returns an error, so at least for testing time...
        login_pw="1" #Just a non-blank character as defensive code

    hashed_login_pw=bcrypt.generate_password_hash(login_pw) 
    print("h"*80)
    print("email, pw, hashed pw  "  + login_email +  login_pw, hashed_login_pw) 

    # Check whether the email provided is associated with a user in the database
    # If it is, check whether the password matches what's saved in the database
    # input is good and we will write to database and show success page
    mysql = connectToMySQL(SCHEMA_NAME)
    query = "select email, pw_hash, id, fname from users where email=%(em)s;" #shortened from select * to select email
    print("query is  ", query)
    data = {
        "em": login_email
    }
    result = mysql.query_db(query, data)
    print("query returns result of match between email submitted in login and  user table:  ")
    print(result)

    if len(result)<1: # result is a list of dictionaries with each dictionary being a record from database.  length = 0 means list has no elements, so no match
        print("evil hacker with fake email")
        flash("You could not be logged in", "login")
        return redirect ("/")
    print("r"*70)
    print(type(result[0]))
    matched_hashed_pw=result[0]['pw_hash']
    print(type(matched_hashed_pw))
    print("matching hashed PW:  " +  str(result[0]['pw_hash']))
    print("variable matched_hashed_pw:  " + str(matched_hashed_pw))

    if bcrypt.check_password_hash(matched_hashed_pw,login_pw):
        print("we got a match")
        session['user_id'] = result[0]['id']
        print("so cookie id is: " + str(session['user_id']))
        flash("You were logged in", "login")
        session['session_fname'] = result[0]['fname'] #storing first name of logged in user for handy retrieval from html pages
        return redirect('/books') 
    else:
        print("evil hacker")
        flash("You could not be logged in", "login")

        return redirect ("/")
    # End /login route

@app.route('/books')
def books(): 
    #like a success route this route is the result of a redirect...so it renders a template, but also the user can use 5000/books as a bookmark as the entry place which will only work if they are still logged in
  # check cookie to see if logged in
    # no cookie, then not  logged in

    if 'user_id' not in session:
        print("key 'user_id' does NOT exist")
        flash("You must be logged in to enter this website", "login")

        return redirect ("/")
    else:
        print("!"*80)
        print('key user_id exists!')

        mysql = connectToMySQL(SCHEMA_NAME)
    
        query = """select books.id AS 'books_ID', books.title AS 'books_title', books.added_by_id AS 'book_added_by_id', favorites.fav_by_id AS 'who_faved_book', 
        users.fname AS 'fname who added', users.lname AS 'lname who added'
        from books
        join  users  ON books.added_by_id=users.id
        join favorites on favorites.book_id=books.id;"""

        print("query is  ", query)

        allBooks =mysql.query_db(query)

        print(allBooks)
        print("+"*76)


    return render_template("allBooks.html", allBooks=allBooks )
# end /books route


@app.route('/addbook', methods=['POST'])  
def addbook():

    #adds the book to books table
    #submitter is automatically added to favorites table for this book
    print("p"*80)
    print(" this should be the book title:  " + request.form['sentbooktitle'])
    print("this should be the book description:  " + request.form['sentbookdescription'])

    valid=True
    if (len(request.form['sentbooktitle']))<1:
        valid=False
        flash("Title must not be blank", "addfavbook")

    if (len(request.form['sentbookdescription']))<5:
        valid=False
        flash("Please include at least 5 characters in description", "addfavbook")

    if(not valid):
        print("test")
        return redirect('/books') 

    query = """insert into books (added_by_id, title, description ) VALUES (%(currentloggedidbydata)s, %(booktitlebydata)s, %(bookdescriptionbydata)s);"""

    data = {
        "currentloggedidbydata": session['user_id'],
        "booktitlebydata": request.form['sentbooktitle'],
        "bookdescriptionbydata": request.form['sentbookdescription']
    }
    print("q"*80)
    print(query)
    print(data)

    mysql = connectToMySQL(SCHEMA_NAME)
    new_book_id = mysql.query_db(query, data)

    ########

    query = """insert into favorites (book_id, fav_by_id) VALUES (%(newbookbydata)s, %(favedbyidbydata)s);"""

    data = {
        
        "newbookbydata": new_book_id,
        "favedbyidbydata": session['user_id']
    }

    print("9"*80)
    print(query)
    print(data)

    mysql = connectToMySQL(SCHEMA_NAME)
    new_fav_id = mysql.query_db(query, data)

    return redirect('/books') 
    # End /doFavorite route


@app.route('/doFavorite/<bookID>', methods=['GET'])  
def doFavorite(bookID):

    print("book to be favorited:  " , bookID)
    print("logged in user:  ", session['user_id'])

    query = """insert into favorites (book_id, fav_by_id) VALUES (%(newbookbydata)s, %(favedbyidbydata)s);"""

    data = {
        "newbookbydata": bookID,
        "favedbyidbydata": session['user_id']
    }

    print("9"*80)
    print(query)
    print(data)

    mysql = connectToMySQL(SCHEMA_NAME)
    new_fav_id = mysql.query_db(query, data)

    return redirect('/books') 
    # End /doFavorite route



@app.route('/books/<bookID>', methods=['POST'])  
def booksOne():
    pass



    

    return render_template(oneBook.html)
    # End /doFavorite route



    #return render_template("oneBook.html",  )
# end /books route



@app.route('/updateDescription<bookID>', methods=['POST'])  
def updateDesc():
    pass
    


@app.route('/unfavorite/<bookID>', methods=['POST'])  
def unFav():
    pass
    

    #return redirect ("/books")
    # End /doFavorite route



    #return redirect ("/books")
    # End /doFavorite route





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





if __name__ == "__main__":
    app.run(debug=True)