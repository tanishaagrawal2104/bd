from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Time(db.Model):  # Capitalized class name
    __tablename__ = "time"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    time = db.Column(db.Date, nullable=False)  # Change db.Time to db.Date if you want to store just the date
    
    def __init__(self, time):
        self.time = time

    def __repr__(self):
        return f"<Time {self.time}>"
