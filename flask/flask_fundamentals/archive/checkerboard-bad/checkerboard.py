#this is the server file


from flask import Flask, render_template    #Import Flask to allow us to create our app
app = Flask(__name__)       #Create a new instance of the Flask class called "app"

@app.route("/<rows_cols>")             #the "@" decorator associateds this route with the function immediately follow
def checkerboard(rows_cols):
    #Instead of returning a string, 
    #we'll return the result of a the render_template method, passing in the name of our HTML file
    print("in the checkerboard function")
    print ("type is" ,type(rows_cols))
    return render_template('checkerboard.html', rows_cols=int(rows_cols), color = "pink")

if __name__=="__main__":    # Ensure this file is being run directly and not from a different module
    app.run(debug=True)     # Run the app in debug mode.