# import datetime
import re
from flask_app import db,app
from flask import flash
from sqlalchemy.sql import func
from sqlalchemy import text

# ! FIGURE OUT THE BEST PLACE TO PUT THIS PROBABLY IN THE INIT.PY?
from flask_login import LoginManager, login_manager, UserMixin, login_required, login_user, logout_user, current_user
login_manager = LoginManager()
login_manager.init_app(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.TIMESTAMP, nullable=False, server_default=func.now())
    updated_at = db.Column(db.TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    purchases = db.relationship("Purchase", backref="user", lazy=True)

    @staticmethod
    def validate_register(data):
        is_valid = True
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        if len(data['first_name']) < 2:
            flash("First name must be more than 2 or more characters")
            is_valid = False
        if len(data['last_name']) < 2:
            flash("last name must be more than 2 or more characters")
            is_valid = False
        if len(data['email']) == 0:
            is_valid = False
            flash('Enter an email')
        elif not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash('Invalid email address')

        # ! CHECK FOR DUPLICATE EMAILS 

        if len(data['password']) < 6:
            is_valid = False
            flash('Password must be more than 6 characters')
        elif data['password'] != data['confirm_password']:
            flash("Password don't match")
            is_valid = False
        return is_valid

    # @staticmethod
    # def validate(data):
    #     match data:
    #         case (len(data) < 3, ):
    #             print("yopu lost")


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
