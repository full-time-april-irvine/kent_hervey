#this is the server file

from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


@app.route('/', methods=['get']) #per instructions:  Have the root route render this [the wireframe] page..an that is about all it does
def start():

    new_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S%f')

    if 'total_gold' not in session:
        session['total_gold'] = 0
    if 'activity_list' not in session:
        session['activity_list'] = []

    return render_template("ninjagold.html", activity_results=session['activity_list'], gold_count=session['total_gold']) #these extra values are just for testing and will move to the other route



@app.route('/process_money', methods=['POST'])  #per video, html form key-values will be sent to this route per instructions:  Have the "/process_money" POST route increase/decrease the user's gold by an appropriate amount and redirect to the root route.  I think this means the html page's form sends its results to this /process money route
def process_money():
    new_time=datetime.now().strftime('%Y-%m-%d %H:%M:%S%f')
    location_visited=request.form['locationclick'] #possible values:  farm, cave, house, casino
    print("location visited:  " + location_visited)
    if (location_visited=="farm"):
        new_gold=random.randint(10,20)
        new_activity_text="<p class=""won_activities"" >Earned "+ str(new_gold) + " golds from the farm! (" + new_time + ")</p>"
    elif (location_visited=="cave"):
        new_gold=random.randint(5,10)
        new_activity_text="<p class=""won_activities"" >Earned "+ str(new_gold) + " golds from the cave! (" + new_time + ")</p>"
    elif (location_visited=="house"):
        new_gold=random.randint(2,5)
        new_activity_text="<p class=""won_activities"" >Earned "+ str(new_gold) + " golds from the house! (" + new_time + ")</p>"
    else:
        new_gold=random.randint(-50,50)
        if (new_gold>0):
            new_activity_text="<p class=""won_activities"" >Entered a casino and won "+ str(new_gold) + " golds ! (" + new_time + ")</p>"
        elif (new_gold == 0):
            new_activity_text="<p class=""won_activities"" >Entered a casino and won "+ str(1) + " golds  ! (" + new_time + ")</p>"
        else:
            new_activity_text="<p class=""lost_activities"" >Entered a casino and lost "+ str(new_gold*-1) + " golds  Ouch! (" + new_time + ")</p>"

    print("new activity string:  " + new_activity_text)

    session['total_gold'] = str(int(session['total_gold']) + new_gold)
    #session['activity_list'] = [new_activity_text,new_activity_text,'erer','4545t']
    session['activity_list'].insert(0,new_activity_text)
    print(session['activity_list'])

    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)





