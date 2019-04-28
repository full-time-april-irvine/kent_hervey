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

#603-
#There routes:  /     /register  /login  /books -  /books/<bookID> -  /addFav/<bookID>      /unfavorite/<bookID>  /updateDescription<bookID> /logout
#               / is the root route and renders the registration/login page
#               /register seems to be needed to catch the forms sent from the register side of the reglogPW.html page (typically the index page) 
#                       redirects to /books if success, or back to / if fail
#               /login seems to be needed to catch the forms sent from the login side of the reglogPW.html page (typically the index page)
#                       redirects to /books if success, or back to / if fail
#               /books   is about rendering the allBooks.html page....the success page   
#               /books/<bookID> is about rendering the oneBook.html page....
#               /addFav/<bookID> receives form from allBooks.html and oneBook.html, performs action in database and redirects to /books
#               /unfavorite>/<bookID> receives form from oneBook.html, performs action in database and redirects to /books
#                  /logout would do just that: log the user out, and send some place safe and useful...like the root route which then renders the reglogPW.html
#               
#there are three html pages that look different only by flash messages and personalization such as using users name and populated data fields
    #reglogPW.html  or index.html is used for registration and login WH users_new
    #allBooks.html  or books_index.html is used for displaying All books whether favorited or not  This is a success page  WH:  call it books_index
    #oneBook.html   or book_show displays single book  WH:  books_show



@app.route('/') 
def index():
    pass
    # This will render the login and registration page
    # return render_template("")


    #return render_template("allBooks.html") # This is the registration login form
 

@app.route('/register', methods=['POST'])  # this route shows up when the user clicks register and will send user to /wall, or if bad, then redirect to /
def register():
    pass

    #return redirect ('/')


    #return redirect('/books') 
 # end /register route

@app.route('/login', methods=['POST'])  # this route shows up when the user clicks login and will send user to /books, or if bad, then redirect to /
def login():
    pass

   


        #return redirect('/books') 
    #else:

        #flash("You could not be logged in", "login")

       # return redirect ("/")
    # End /login route

@app.route('/books')
def books(): 
    #like a success route this route is the result of a redirect...so it renders a template, but also the user can use 5000/books as a bookmark as the entry place which will only work if they are still logged in
    pass

  
     

    #return render_template("allBooks.html",  )
# end /books route

@app.route('/books/<bookID>')
def booksOne():
    pass
  
     

    #return render_template("oneBook.html",  )
# end /books route





@app.route('/addFav/<bookID>', methods=['POST'])  
def addFav():
    pass
    

    #return redirect ("/books")
    # End /addFav route

@app.route('/unfavorite/<bookID>', methods=['POST'])  
def unFav():
    pass
    

    #return redirect ("/books")
    # End /addFav route

@app.route('/updateDescription<bookID>', methods=['POST'])  
def updateDesc():
    pass
    

    #return redirect ("/books")
    # End /addFav route





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