
import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_app import app
import os 
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("MYSQL_URI")
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now(datetime.timezone.utc))
