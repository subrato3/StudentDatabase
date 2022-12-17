from flask import Flask, redirect, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///student.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.String(15), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    mobile = db.Column(db.Integer, nullable=False)

    def __repr__(self) -> str:
        return f"{self.id} - {self.name}"


@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        dob = request.form["dob"]
        address = request.form["address"]
        mobile = request.form["mobile"]
        student = Student(name=name, surname=surname, dob=dob, address=address, mobile=mobile)
        db.session.add(student)
        db.session.commit()

    allStudent = Student.query.all()
    return render_template("index.html", allStudent=allStudent)


@app.route("/show")
def products():
    allStudent = Student.query.all()
    print(allStudent)


@app.route("/update/<int:id>", methods=["GET", "POST"])
def update(id):
    if request.method == "POST":
        name = request.form["name"]
        surname = request.form["surname"]
        dob = request.form["dob"]
        address = request.form["address"]
        mobile = request.form["mobile"]
        Student = Student.query.filter_by(id=id).first()
        Student.name = name
        Student.surname = surname
        Student.dob = dob
        Student.address = address
        Student.mobile = mobile
        db.session.add(student)
        db.session.commit()
        return redirect("/")

    student = Student.query.filter_by(id=id).first()
    return render_template("update.html", student=student)


@app.route("/delete/<int:id>")
def delete(id):
    student = Student.query.filter_by(id=id).first()
    db.session.delete(student)
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port="3602")
