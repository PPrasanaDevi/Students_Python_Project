from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class StudentModel(db.Model):
    __tablename__ = 'students'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String())
    password = db.Column(db.String())
    gender = db.Column(db.String(10))
    hobbies = db.Column(db.String(100))
    country = db.Column(db.String(50))

    def __init__(self, first_name, last_name, email, password, gender, hobbies, country):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.gender = gender
        self.hobbies = hobbies
        self.country = country

    def __repr__(self):
        return f"<Student {self.first_name} {self.last_name}>"

