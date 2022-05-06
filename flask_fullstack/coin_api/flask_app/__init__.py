from flask import Flask
import os 
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.config['API_KEY'] = os.environ.get("API_KEY")
app.config['API_HOST'] = os.environ.get("API_HOST")