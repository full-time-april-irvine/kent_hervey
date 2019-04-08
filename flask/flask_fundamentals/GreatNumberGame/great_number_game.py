#this is the server file

from flask import Flask, render_template, request, redirect, session
import random

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

@app.route('/', methods=['GET'])
def first_time():
    #get random number and store in session cookie for safe keeping

    print("2"*60)
    print("you are in the get route")
    print("2"*60)
    session.clear()	
    session['generated_number'] = getNumber()

    return render_template("gamepage.html") #we don't need to send the random number to the game page.  It only needs to know low, high, or correct


@app.route('/', methods=['POST'])
def calulate_results():
    print("you are in the post route")
    #get random number and store in session cookie for safe keeping

    #if we have an active guess, then compare system number/random number with active guess and determine high, low, correct
    #How can we tell if we have an active guess? By checking the previous web page...the referrer, or by setting a flag if came from the game page....or start the guess at -1000 and until it greater than 1 we know we have no inactive guess.  Also, except for the first time we will always have an active guess because that is the only way to get to the site

    received_guess = int((request.form['send_guess']))
    correct_number = int(session['generated_number'])
    print("cn",type(correct_number), " for ", correct_number) 
    guess_over_correct = received_guess - correct_number
    print("1"*60)
    print("received guess is:  " + str(received_guess), "And it is this much more than the correct number:  ", str(guess_over_correct))
    print("1"*60)
    #user_message = "your guess was this much over the correct numberr:  ", str(guess_over_correct, last_guess=received_guess))

    if (guess_over_correct>0):
        user_message="TOO HIGH"
    elif (guess_over_correct==0):
        user_message= "YOU ARE RIGHT.  The number is:  " + str(correct_number)
    else:    
        user_message="TOO LOW"

    print (user_message)
    print ("last guess is : ",  received_guess)
    return render_template("gamepage.html", sent_hilo=user_message, last_guess=received_guess) #we don't need to send the random number to the game page.  It only needs to know low, high, or correct

def getNumber():
    return random.randrange(97) +2



def hiLowRight():
    print("you guessed  ",   request.form['send_guess'] )





print("this is my random number:  ", getNumber())

if __name__ == "__main__":
    app.run(debug=True)