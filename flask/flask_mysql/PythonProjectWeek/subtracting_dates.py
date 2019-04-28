#first question, but I will make it second:  how does date come in from form field


from datetime import *
# today = date.today()
# print("today is:  " + str(today))
# future = date(2019,5,20)
# print (future)
# elapsed_days =future-today
# print(elapsed_days)

# print("*"*80)

# birthday = datetime(2019,2,19)
# print(birthday.year)
# diff = datetime.now() - birthday
# print(str(diff))



from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/datecheck')
def datecheck():
    return render_template("/index.html")

@app.route('/checkthedate', methods=['POST'])
def checkthedate():
    today = datetime.now()

    returned_begin_date=request.form['returnedBeginDate']
    returned_begin_date_obj=datetime.strptime(returned_begin_date, '%Y-%m-%d')
    days_to_returned_begin_date =(returned_begin_date_obj - today).days+1
    output_begin_string = "You entered " + returned_begin_date + "  which is " + str(days_to_returned_begin_date) + " days from now"






    return render_template("/index.html", begin=output_begin_string)



# As you can see, the conversion was successful!

# You can see that the forward slash "/" has been used to separate the various elements of the string. This tells the strptime method what format our date is in, which in our case "/" is used as a separator.

# But what if the day/month/year was separated by a "-"? Here is how you'd handle that:

# from datetime import datetime

# str = '9-15-18'  
# date_object = datetime.strptime(str, '%m-%d-%y')

# print(date_object)  
# Output:

# 2018-09-15 00:00:00  
# And again, thanks to the format specifier the strptime method was able to parse our date and convert it to a date object.


# @app.route('/checkthedate', methods=['POST'])
# def checkthedate():
#     dateBack=request.form['returnedDate']
#     print(request.form['returnedDate'])
#     print("%"*80)
#     print("print the date from form:  ")
#     print(dateBack)
#     date_object=datetime.strptime(dateBack, '%Y-%m-%d')
#     print("date from form converted to object:  ")
#     print(date_object)
#     future = date(2019,5,20)
#     future =  date_object
#     today = datetime.now()
#     print(today)
#     #future = date(2019,5,20)
#     days_to_future =(future-today).days
#     print(days_to_future)







if __name__=="__main__":
    app.run(debug=True)