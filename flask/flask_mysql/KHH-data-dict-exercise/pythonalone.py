from flask import Flask, render_template, request, redirect, session
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection


SCHEMA_NAME = "khhpracticelearn041519"
    
    
all_users = [ 
{'sender_id': 1, 'receiver_id': 8,'fname': 'Andrew', 'lname': 'Lee', 'email': 'alee@gmail.com', 'message_content': 'blah blah 11111 11111 11111 1111', 'messageID': 3}, 
{'sender_id': 2, 'receiver_id': 8,'fname': 'Jay', 'lname': 'Patel', 'email': 'jpatel@gmail.com', 'message_content': 'blah blah 222 22222 11111 1111', 'messageID': 3}, 
{'sender_id': 3, 'receiver_id': 6,'fname': 'Eduardo', 'lname': 'Baikaa', 'email': 'ebaik@gmail.com', 'message_content' : 'blah blah 11131', 'messageID': 2}, 
{'sender_id': 4, 'receiver_id': 6,'fname': 'fred', 'lname': 'jonesa', 'email': 'bob@jones.com', 'message_content': 'blah blah 4444  4 4 4 4 ', 'messageID': 9}, 
{'sender_id': 4, 'receiver_id': 5,'fname': 'fred', 'lname': 'jones', 'email': 'bob@jones.com', 'message_content': 'blah blah 5   5 5 5 5 51', 'messageID': 3}, 
{'sender_id': 4, 'receiver_id': 5,'fname': 'bob', 'lname': 'jones', 'email': 'bob@jones.com', 'message_content': 'blah blah 1 666666  66661', 'messageID': 5}
]  



print("all users first list item")
print(all_users[0])

print("all users first list item, first item in dictionary")
print(all_users[0]['fname'])

for i in all_users: 
    print("email from each item in list:  ",   i['email']) 

for i in range(len(all_users)): 
    print("using range....email from each item in list:  ",   all_users[i]['email']) 

one_dict = {'sender_id': 1, 'receiver_id': 8,'fname': 'Andrew', 'lname': 'Lee', 'email': 'alee@gmail.com'}
for spam in one_dict:
    print("spam is  " + spam)

for spammedValues in one_dict.values():
    print("values are: " + str(spammedValues))  

###############################################

#One from database

mysql = connectToMySQL(SCHEMA_NAME)
query = "select * from users where email =donald@duck.com"

result = mysql.query_db(query)


#testString = result[0]

testString = "bad"

print("below is testString")
print(testString)