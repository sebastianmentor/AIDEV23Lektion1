import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, flash, redirect, url_for
from models import Person, ListOfPersons, anstallda, anstallda_id, våra_anställda




app = Flask(__name__)

load_dotenv()

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route("/")
def home_page():
    return render_template("index.html")

@app.route("/about")
def about():
    anställda = 11
    global våra_anställda
    return render_template("about.html", antal = anställda, våra_anställda=våra_anställda)

@app.route("/employees")
def employees():
    global anstallda

    return render_template("employees.html", employees=anstallda)
@app.route("/employee/<emp_id>")
def employee(emp_id):
    global anstallda
    if emp_id in anstallda:
        anstalld = anstallda[emp_id]
        finns_anställd = True
    else:
        finns_anställd = False
        anstalld = {}

    return render_template('employee.html', emp=anstalld, finns = finns_anställd)

@app.route("/question", methods=['GET', 'POST'])
def question():
    if request.method == "POST":
        fråga = request.form.get("question")
        if not fråga:
            flash('Du ställde inte någon fråga!')
    else:
        fråga = request.args.get("q", "No question asked")

    return render_template("question.html", fråga = fråga)

@app.route("/addemployee", methods=['GET','POST'])
def addemployee():
    if request.method == "POST":
        namn = request.form.get("namn")
        ålder = request.form.get("ålder")
        roll = request.form.get("roll")
        erfarenhet = request.form.get("erfarenhet")
        
        global anstallda
        global anstallda_id
        anstallda[anstallda_id] = {
        "namn": namn,
        "alder": ålder,
        "roll": roll,
        "erfarenhet_år": erfarenhet
    }
        anstallda_id += 1
        flash('Ny anställd tillagd!')
    return render_template("add.html")

@app.route("/addperson")
def addperson():
    name = request.args.get('name')
    age = request.args.get('age')
    length = request.args.get('length')

    if name and age and length:
        ListOfPersons._list.append(Person(name,age, length))        
        return redirect(url_for("home_page"))
    return "ERROR"

@app.route('/listpersons')
def listpersons():
    lista_av_personer = ListOfPersons.get_list()
    return render_template('listpersons.html', l = lista_av_personer)

if __name__ == '__main__':
    app.run(debug=True)