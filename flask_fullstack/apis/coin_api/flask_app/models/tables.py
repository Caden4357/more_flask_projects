import datetime
from flask_app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now(datetime.timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now(datetime.timezone.utc))
    purchases = db.relationship("Purchase", backref="user", lazy=True)



class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, unique=True)
    coin_name = db.Column(db.String(50), nullable=False)
    price_at_purchase = db.Column(db.Integer, nullable=False)
    quantity_purchased = db.Column(db.Float, nullable=False)
    total_amount_paid = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now(datetime.timezone.utc))
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now(datetime.timezone.utc))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
