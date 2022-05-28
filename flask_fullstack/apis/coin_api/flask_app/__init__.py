from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os 
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.config['API_KEY'] = os.environ.get("API_KEY")
app.config['API_HOST'] = os.environ.get("API_HOST")

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("MYSQL_URI")
db = SQLAlchemy(app)

# user = 'root'
# password = 'root'
# host = '127.0.0.1'
# port = 3306
# database = 'GeeksForGeeks'
# def get_connection():
#     return create_engine(
#         url="mysql://{0}:{1}@{2}:{3}/{4}".format(
#             user, password, host, port, database
#         )
#     )

# try:
        
#     # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
#     engine = get_connection()
#     print(
#         f"Connection to the {host} for user {user} created successfully.")
# except Exception as ex:
#     print("Connection could not be made due to the following error: \n", ex)