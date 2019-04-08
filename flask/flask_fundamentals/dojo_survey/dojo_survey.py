#this is the server file

from flask import Flask, render_template, request, redirect
app = Flask(__name__)

# our index route will handle rendering our form

@app.route('/')
def index():
    return render_template("dojo_forms.html")



@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    name_from_form = request.form['name']
    location_from_form = request.form.get("DojoLocation")
    print(location_from_form)
    print("and ")
    print(request.form.get("DojoLocation"))

    language_from_form = request.form.get("FavLanguage")
    comment_from_form = request.form['comment_space']
    print


    return render_template("result.html", name_on_template=name_from_form, 
    location_on_template=location_from_form,
    language_on_template=language_from_form,
    comment_on_template=comment_from_form
    )



if __name__ == "__main__":
    app.run(debug=True)