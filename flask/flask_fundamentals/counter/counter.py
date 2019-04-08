#this is the server file

from flask import Flask, render_template, request, redirect, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes



@app.route('/')
def display_visits():
    new_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    booster = 1
    if 'site_count' in session:
        print('key exists!')
        session['site_count'] = session['site_count'] +booster
    else:
        print("key 'site_count' does NOT exist")
        session['site_count'] = booster

    return render_template("count_visits_to_me.html", pass_time=new_time, numVisits=session['site_count'])


@app.route('/destroy')
def create_user():
    print("Got Post Info")
    if 'site_count' in session:
        print('key exists!')
        session.pop('site_count')	
    return redirect('/')




if __name__ == "__main__":
    app.run(debug=True)