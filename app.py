# app.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists
from sqlalchemy import func, exc, create_engine

app = Flask(__name__)

connection_str = f'postgresql://postgres.xgmzxcdyetduyrypqbhh:RaymanIsAwesome123@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres'
db = create_engine(connection_str)

from models import *

Project.metadata.create_all(db)

@app.route('/admin/login', methods=['GET'])
def admin_login():
    return "login_page"
	
@app.route('/admin', methods=['GET'])
def admin_projects_list():
    return "Observing"

@app.route('/', methods=['GET'])
def home():
    return render_template('main.html', title="Portfolio - Dynse Clyde Sacote")

@app.route('/contact', methods=['GET'])
def contact():
    return "Contact page"
    
if __name__ == "__main__":
    app.run()
