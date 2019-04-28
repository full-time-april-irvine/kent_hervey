from flask import Flask, render_template, request, redirect, session, flash, url_for
from datetime import *
from getCatalogFrAPI import make_catalog

app = Flask(__name__)

# @app.route('/plancrop/success')
# def success():
#     catalog_result=make_catalog(95,98)
#     return render_template("success.html", returned_crops=catalog_result)

@app.route('/plancrop')
def dateEntry(): #renders the date entry html template
    print("beginning of plancrop route")
    return render_template("start.html")

 
@app.route('/plancrop/success', methods=['POST'])
def success():
    print("beginning of success route")
    today = datetime.now()
    returned_begin_date=request.form['returnedBeginDate']
    returned_begin_date_obj=datetime.strptime(returned_begin_date, '%Y-%m-%d')
    days_to_returned_begin_date =(returned_begin_date_obj - today).days+1
    output_begin_string1 = "Earliest first harvest date:  " + returned_begin_date + "  which is  " + str(days_to_returned_begin_date) + " days from now"

    returned_end_date=request.form['returnedEndDate']
    returned_end_date_obj=datetime.strptime(returned_end_date, '%Y-%m-%d')
    days_to_returned_end_date =(returned_end_date_obj - today).days+1
    output_begin_string2 = "Latest first harvest date:  " + returned_end_date + "  which is  " + str(days_to_returned_end_date) + " days from now"


    catalog_result=make_catalog(days_to_returned_begin_date,days_to_returned_end_date)
    return render_template("success.html", returned_crops=catalog_result, beginString=output_begin_string1, endString=output_begin_string2)
    #return output_begin_string


if __name__ == "__main__":
    app.run(debug=True)




