#this is the server file

from flask import Flask, render_template, request, redirect, session, flash, url_for
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection



app = Flask(__name__)

app.secret_key ='asdfeeffefa' 'keep it secret, keep it safe' # set a secret key for security purposes

# our index route will handle rendering our form

@app.route('/') # this route does not need to send anything to the survey form
def index():


    return render_template("dojo_forms.html")
 


@app.route('/users', methods=['POST'])  # this page will send user to success, or re-do
def create_user():

    name_from_form = request.form['name']  #validity:  must be at least one char
    location_from_form = request.form.get("DojoLocation") #validity:  must be at least one char.  Note:  this is a dropdown, so that helps
    language_from_form = request.form.get("FavLanguage")  #validity:  must be at least one char.  Note:  this is a dropdown, so that helps
    comment_from_form = request.form['comment_space']  # must be at least 5 char...because...come on

    print(name_from_form, location_from_form, language_from_form, comment_from_form)

    is_valid = True
    if len(name_from_form) <1:
        is_valid = False
        flash("Please enter something")

    if len(location_from_form) <1:
        is_valid = False
        flash("Please enter something")

    if len(language_from_form) <1:
        is_valid = False
        flash("Please enter something")

    if len(comment_from_form) <5:
        is_valid = False
        flash("Please enter some comments.  At least 5 characters.")

    if not is_valid:
        print("you should have entered something")
        return redirect ("/")
    else:  
        print("something")

    mysql = connectToMySQL("dojo_survey_validation")

    query = "INSERT INTO dojo_survey_users (name, location, fav_language, comments, updated_at) VALUES(%(name_bydata)s, %(location_bydata)s, %(language_bydata)s, %(comments_bydata)s, NOW())"

    data = { 
        "name_bydata": name_from_form,
        "location_bydata": location_from_form,
        "language_bydata"   : language_from_form,
        "comments_bydata"   : comment_from_form,
    }

    connectToMySQL("dojo_survey_validation")
    mysql.query_db(query, data)

    flash("Data added")

    return render_template("result.html", name_on_template=name_from_form, 
    location_on_template=location_from_form,
    language_on_template=language_from_form,
    comment_on_template=comment_from_form
    )



if __name__ == "__main__":
    app.run(debug=True)