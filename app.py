from flask import Flask, render_template, request, redirect, url_for
from models import db, StudentModel
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymysql://sa1:LAPTOP-GURU@LAPTOP-GRU6VT04\\SQLEXPRESS/student?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'

db.init_app(app)

@app.before_request
def create_table():
    db.create_all()

@app.route('/', methods=['GET'])
def RetrieveList():
    students = StudentModel.query.all()
    return render_template('index.html', students=students)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('create.html')
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        hobby = request.form.getlist('hobbies')
        hobbies = ",".join(map(str, hobby))
        country = request.form['country']
        student = StudentModel(first_name=first_name, last_name=last_name, email=email, password=password, gender=gender, hobbies=hobbies, country=country)
        db.session.add(student)
        db.session.commit()
        return redirect('/')
    
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    student = StudentModel.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('edit.html', student=student)
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        email = request.form['email']
        password = request.form['password']
        gender = request.form['gender']
        hobby = request.form.getlist('hobbies')
        hobbies = ",".join(map(str, hobby))
        country = request.form['country']
        if student:
            student.first_name = first_name
            student.last_name = last_name
            student.email = email
            student.password = password
            student.gender = gender
            student.hobbies = hobbies
            student.country = country
            db.session.commit()
            return redirect('/')
        else:
            student = StudentModel(first_name=first_name, last_name=last_name, email=email, password=password,gender=gender, hobbies=hobbies, country=country)
            db.session.add(student)
    return render_template('edit.html', student=student)

        

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    student = StudentModel.query.filter_by(id=id).first()
    if request.method == 'POST':
        if student:
            db.session.delete(student)
            db.session.commit()
            return redirect('/')        
    return render_template('delete.html', student=student)





if __name__ == '__main__':
    app.run(debug=True)