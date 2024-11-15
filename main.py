from flask import Flask, render_template, redirect, url_for, request, session, flash
from model import db, Time
import os

from datetime import datetime


current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(current_dir, "uff.sqlite3")


db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    
    return render_template('index.html')

@app.route('/gift', methods=['GET', 'POST'])
def gift():
    return render_template('gift.html')


@app.route('/time', methods=['GET', 'POST'])
def time():
    if request.method == 'POST':
        # Get the time from the form
        movie_time = request.form.get('time')  # Use 'get' to avoid KeyError
        
        if movie_time:
            # Convert the date string into a date object
            movie_time_obj = datetime.strptime(movie_time, "%Y-%m-%d").date()
            
            # Create a new Time record in the database
            new_time = Time(time=movie_time_obj)
            db.session.add(new_time)
            db.session.commit()
        
            return redirect(url_for('last'))
        
    
    return render_template('time.html')

@app.route('/last')
def last():
    return render_template('last.html')  # Make sure 'last.html' exists in the templates folder






if __name__ == "__main__":
    app.run(debug=True)
