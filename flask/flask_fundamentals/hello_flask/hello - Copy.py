#this is the server file


from flask import Flask    #Import Flask to allow us to create our app
app = Flask(__name__)       #Create a new instance of the Flask class called "app"
@app.route('/')             #the "@" decorator associateds this route with the function immediately follow
def hello_world():          
    return 'Hello World!'   # REturn the string 'Hello World!' as a response

@app.route("/bbb")
def hello_person():
    return "Hello NOelle"

@app.route('/success')
def success():
    return "success"

@app.route("/<name>")
def hello_person2(name):
    print("in person2")
    print("name is  ", name)
    return "Hello Another person whose name is  " + name


if __name__=="__main__":    # Ensure this file is being run directly and not from a different module
    app.run(debug=True)     # Run the app in debug mode.