#this is the server file


from flask import Flask, render_template    #Import Flask to allow us to create our app
app = Flask(__name__)       #Create a new instance of the Flask class called "app"

@app.route("/play/<times>/<color>")             #the "@" decorator associateds this route with the function immediately follow
def hello_worlda(times,color):
    #Instead of returning a string, 
    #we'll return the result of a the render_template method, passing in the name of our HTML file
    print("in the hello function")
    print ("type is" ,type(times))
    print("times is  " + times + "and color is  " + color)
    return render_template('index.html', color=color, times=int(times))


@app.route("/play/<times>")             #the "@" decorator associateds this route with the function immediately follow
def hello_world(times):
    #Instead of returning a string, 
    #we'll return the result of a the render_template method, passing in the name of our HTML file
    print("in the hello function")
    print ("type is" ,type(times))
    return render_template('index.html', times=int(times), color = "red")


@app.route("/play/")             #the "@" decorator associateds this route with the function immediately follow
def hello_world2():
    #Instead of returning a string, 
    #we'll return the result of a the render_template method, passing in the name of our HTML file
    print("in the hello function")
    return render_template('index.html', times=int(3) , color = "red")


if __name__=="__main__":    # Ensure this file is being run directly and not from a different module
    app.run(debug=True)     # Run the app in debug mode.