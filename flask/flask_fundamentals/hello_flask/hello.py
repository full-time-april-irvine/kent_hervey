#this is the server file


from flask import Flask, render_template    #Import Flask to allow us to create our app
app = Flask(__name__)       #Create a new instance of the Flask class called "app"
@app.route('/')             #the "@" decorator associateds this route with the function immediately follow
def hello_world():
    #Instead of returning a string, 
    #we'll return the result of a the render_template method, passing in the name of our HTML file
    print("in the hello function")
    return render_template('index.html', prhase = "hello", times=5)

@app.route("/<name>")
def hello_person(name):
    print("*"*80)
    print("in hello_person function")
    print(name)
 
    return render_template ("name.html", some_name = name)


if __name__=="__main__":    # Ensure this file is being run directly and not from a different module
    app.run(debug=True)     # Run the app in debug mode.