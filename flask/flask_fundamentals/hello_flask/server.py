#this is the server file


from flask import Flask    #Import Flask to allow us to create our app
                            #Flask is the class
app = Flask(__name__)       #Create a new instance of the Flask class called "app"
                            #files name is "main"
@app.route('/')             #the "@" decorator associateds this route with the function immediately follow
def hello_world():          
    return 'Hello World!'   # REturn the string 'Hello World!' as a response

@app.route("/dojo")
def hello_dojo():
    return "Dojo"

@app.route("/say/<name>")
def hello_person2(name):
    print("in person2")
    print("name is  ", name)
    return "Hi " + name.capitalize() + "!"

@app.route("/repeat/<num_repeats>/<to_repeat>")
def repeat_me(num_repeats,to_repeat):
    int_repeats = int(num_repeats)
    output_string =""
    for i in range(0, int_repeats, 1):
        output_string +=to_repeat

    return "Hi " + output_string



if __name__=="__main__":    # Ensure this file is being run directly and not from a different module
    app.run(debug=True)     # Run the app in debug mode.