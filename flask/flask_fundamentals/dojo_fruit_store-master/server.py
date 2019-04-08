from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])   #This is where we get the info from the template and pass to the results page

def checkout():
    print(request.form)
    strawberry_count = int(request.form['strawberry'])
    rasberry_count = int(request.form['raspberry'])
    apple_count = int(request.form['apple'])
    fruit_count= strawberry_count + rasberry_count + apple_count
    first_name_f=request.form['first_name']
    last_name_f=request.form['last_name']
    order_time=datetime.now().strftime('%Y-%m-%d')
    student_id=request.form['student_id']
    print("at ", (order_time))
    print("charging " + first_name_f + last_name_f + "  for  " + str(fruit_count))

    return render_template("checkout.html", fname_on_template=first_name_f,
        lname_on_template=last_name_f, strawberry_count_template=strawberry_count, 
        rasberry_count_template=rasberry_count , apple_count_template = apple_count,
        fruit_count_template=fruit_count, order_time_template=order_time,
        student_id_template = student_id)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    