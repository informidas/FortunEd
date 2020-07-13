from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class user (db.Model):
    """ User model """

    __tablename__ = "users"
    id= db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    profile = db.Column(db.String(20))
    optIn = db.Column(db.Boolean)

    db.create_all()