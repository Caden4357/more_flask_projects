import datetime
from flask_app import db
from sqlalchemy.sql import func
from sqlalchemy import text
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    purchases = db.relationship("Purchase", backref="user", lazy=True)



class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.Integer, nullable=False, unique=True)
    coin_name = db.Column(db.String(50), nullable=False)
    price_at_purchase = db.Column(db.Integer, nullable=False)
    quantity_purchased = db.Column(db.Float, nullable=False)
    total_amount_paid = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
