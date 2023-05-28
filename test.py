from flask import Flask, request, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/register', methods =["GET","POST"])           
def takeInput():
    if request.method == "POST":
        firstname = request.form.get("fname")
        lastname = request.form.get("lname")
        return "Your first name is " + firstname + "Your last name is " + lastname
    return render_template("questions.html")

app.run(debug = True)