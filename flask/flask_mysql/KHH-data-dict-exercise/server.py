from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection

SCHEMA_NAME = "khhpracticelearn041519"

app = Flask(__name__)
app.secret_key ='asdfeeffefa' 'keep it secret, keep it safe' # set a secret key for security purposes



# Database name:  user_assignment
# Table name:  user_table
# Field names:
# id | fname   | lname | email            | created_at          | updated_at

@app.route('/formex', methods=["GET"])   #  /users - GET - method should return a template that displays all the users in the table
def formex():

    # mysql = connectToMySQL("user_assignment")
    # all_users = mysql.query_db("SELECT * FROM user_table;")
    # print("*"*80)
    # print("this is list of all users, all columsn", all_users)


    all_users = [ 
    {'sender_id': 1, 'receiver_id': 8,'fname': 'Andrew', 'lname': 'Lee', 'email': 'alee@gmail.com', 'message_content': 'blah blah 11111 11111 11111 1111', 'messageID': 3}, 
    {'sender_id': 2, 'receiver_id': 8,'fname': 'Jay', 'lname': 'Patel', 'email': 'jpatel@gmail.com', 'message_content': 'blah blah 222 22222 11111 1111', 'messageID': 3}, 
    {'sender_id': 3, 'receiver_id': 6,'fname': 'Eduardo', 'lname': 'Baikaa', 'email': 'ebaik@gmail.com', 'message_content' : 'blah blah 11131', 'messageID': 2}, 
    {'sender_id': 4, 'receiver_id': 6,'fname': 'fred', 'lname': 'jonesa', 'email': 'bob@jones.com', 'message_content': 'blah blah 4444  4 4 4 4 ', 'messageID': 9}, 
    {'sender_id': 4, 'receiver_id': 5,'fname': 'fred', 'lname': 'jones', 'email': 'bob@jones.com', 'message_content': 'blah blah 5   5 5 5 5 51', 'messageID': 3}, 
    {'sender_id': 4, 'receiver_id': 5,'fname': 'bob', 'lname': 'jones', 'email': 'bob@jones.com', 'message_content': 'blah blah 1 666666  66661', 'messageID': 5}
    ]  

    print("all users first list item" + all_users[0])


    tester = 5

    #return render_template("/dict.html", return_users=all_users)
    return render_template("/formexample.html", somevalue=tester, return_users=all_users)







@app.route('/learnd', methods=["GET"])   #  /users - GET - method should return a template that displays all the users in the table
def learnd():

    # mysql = connectToMySQL("user_assignment")
    # all_users = mysql.query_db("SELECT * FROM user_table;")
    # print("*"*80)
    # print("this is list of all users, all columsn", all_users)

    all_users = [ 
    {'fname': 'Andrew', 'lname': 'Lee', 'email': 'alee@gmail.com'}, 
    {'fname': 'Jay', 'lname': 'Patel', 'email': 'jpatel@gmail.com'},  
    {'fname': 'Eduardo', 'lname': 'Baikaa', 'email': 'ebaik@gmail.com'},  
    {'fname': 'fred', 'lname': 'jonesa', 'email': 'bob@jones.com'},  
    {'fname': 'fred', 'lname': 'jones', 'email': 'bob@jones.com'}, 
    {'fname': 'bob', 'lname': 'jones', 'email': 'bob@jones.com'}, 
    {'fname': 'bob', 'lname': 'jones', 'email': 'bob@jones.com'}, 
    {'fname': 'bob', 'lname': 'jones', 'email': 'bob@jones.com'}, 
    {'fname': 'bobs', 'lname': 'namer', 'email': 'bob@jones.com'}, 
    {'fname': 'bob', 'lname': 'jon', 'email': 'bob@jones.com'}, 
    {'fname': 'bob2', 'lname': 'jones2', 'email': '2@no.com'}, 
    {'fname': 'bob3', 'lname': 'jones3', 'email': '3@3.com'},  
    {'fname': 'bob5', 'lname': 'jones5', 'email': '5@5.com'},  
    {'fname': 'shannon', 'lname': 'jones', 'email': 'no@yes.com'}]  


    return render_template("/dict.html", return_users=all_users)
    #return render_template("/dict.html")

@app.route('/sql', methods=["GET"])   #  /users - GET - method should return a template that displays all the users in the table
def sql():
    mysql = connectToMySQL(SCHEMA_NAME)
    query = "select * from users where email ='donald@duck.com';"

    print(query)

    result = mysql.query_db(query)

    print("below is result")
    print(result) #prints [{'user_id': 3, 'fname': 'Donald', 'lname': 'Duck', 'email': 'donald@duck.com', 'created_at': datetime.datetime(2019, 4, 15, 13, 33, 38)}]

    print("below is learning test")
    print(result[0]['email']) # prints donald@duck

    return redirect('/sql')

#Below is leftover samples...not used

#########################################
#############################################################

@app.route('/users', methods=["GET"])   #  /users - GET - method should return a template that displays all the users in the table
def all_user():

    mysql = connectToMySQL("user_assignment")
    all_users = mysql.query_db("SELECT * FROM user_table;")
    print("*"*80)
    print("this is list of all users, all columsn", all_users)


    return render_template("/readall.html", return_users=all_users)

####################################################################

@app.route('/users/<id>', methods=["GET"])     #	/users/<id> - GET - method should return a template that displays the specific user's information
def specific_user(id):
    print("id is:  " + id)

    #mysql = connectToMySQL("user_assignment")
    query = "SELECT * FROM user_table where id = %(pt)s"

    data = {
        "pt": id
    }

    mysql = connectToMySQL("user_assignment")
    one_user=mysql.query_db(query, data) 
   
    print("*"*80)
    print("this is one user, all collumns", one_user)


    return render_template("/readone.html", returning_one=one_user)

####################################################################

@app.route('/users/new', methods=["GET"]) #	/users/new- GET - method should return a template containing the form for adding a new user
def new_user():



    return render_template("/create.html")
            
####################################################################


@app.route('/users/create', methods=["POST"])     # 	/users/create - POST - method should add the user to the database, then redirect to /users/<id>
def create_user():

    #We arrive here when create.html form is submitted...then when finished, we go to see the result in the readone.html by going tothe /users/id...we can't just go to the html because we have server side work to do before displayng the page

    #This uses insert into, so I will look at pets
    mysql = connectToMySQL("user_assignment")

    # coming from create.html will be fname, lname, email
    query = "INSERT INTO user_table (fname, lname, email, created_at, updated_at) VALUES(%(fname_bydata)s, %(lname_bydata)s, %(email_bydata)s,NOW(), NOW())"

    data = { 
        "fname_bydata": request.form["fname_submitted"],
        "lname_bydata": request.form["lname_submitted"],
        "email_bydata": request.form["email_submitted"],
    }

    mysql = connectToMySQL("user_assignment")
    new_user_id = mysql.query_db(query, data) 
    print("should be new user id: " , new_user_id)
    session['user_id'] = new_user_id

    return redirect("/users/" +str(new_user_id))

####################################################################

@app.route('/users/<id>/edit', methods=["GET"]) #  	/users/<id>/edit - GET - method should return a template that displays a form for editing the user with the id specified in the url
def edit_user(id):
    #mysql = connectToMySQL("user_assignment")
    query = "SELECT * FROM user_table where id = %(pt)s"

    data = {
        "pt": id
    }

    mysql = connectToMySQL("user_assignment")
    one_user=mysql.query_db(query, data) 
   
    print("*"*80)
    print("this is one user, all collumns", one_user)

    return render_template("/update.html", returning_one=one_user)

####################################################################

@app.route('/users/<id>/update', methods=["POST"])  # /users/<id>/update - POST - method should update the specific user in the database, then redirect to /users/<id>
def update_specific_user(id):
    mysql = connectToMySQL("user_assignment")
    query = "UPDATE user_table SET fname = %(fname_bydata)s, lname = %(lname_bydata)s, email = %(email_bydata)s, updated_at=NOW() WHERE id=%(id_bydata)s;"

    data = { 
        "id_bydata": int(id),
        "fname_bydata": request.form["fname_submitted"],
        "lname_bydata": request.form["lname_submitted"],
        "email_bydata": request.form["email_submitted"],
    }

    mysql = connectToMySQL("user_assignment")
    updated_user_id = mysql.query_db(query, data) 

    return redirect('/users/' + str(id))

####################################################################

@app.route('/users/<id>/destroy', methods=["GET"])  # /users/<id>/destroy - GET - method should delete the user with the specified id from the database, then redirect to /users
def delete_specific_user(id):

    mysql = connectToMySQL("user_assignment")

    query = " delete from user_table WHERE id=%(id_bydata)s;"

    data = { 
        "id_bydata": int(id),
    }

    mysql = connectToMySQL("user_assignment")
    mysql.query_db(query, data) 

    return redirect("/users")

####################################################################




if __name__ == "__main__":
    app.run(debug=True)