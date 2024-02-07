# app.py
from flask import Flask, render_template, jsonify, g, request, abort, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists
from sqlalchemy import func, exc, create_engine, select
from sqlalchemy.orm import sessionmaker
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Dolph Laserhawk and Alex Taylor are a complicated couple'
connection_str = f'postgresql://postgres.xgmzxcdyetduyrypqbhh:RaymanIsAwesome123@aws-0-ap-southeast-1.pooler.supabase.com:5432/postgres'
db = create_engine(connection_str)
auth = HTTPBasicAuth()

from models import *

Project.metadata.create_all(db)
User.metadata.create_all(db)

Session = sessionmaker(bind=db)
session = Session()

@app.route('/admin/start', methods=['GET'])
def create_first_admin():
    # this returns int
    user_count = session.query(User).count()
    if user_count > 0:
        return "Admin already existed"
    else:
        default_admin = User(username = "admin")
        # change this later
        default_pass = "admin"
        default_admin.hash_password(default_pass)
        session.add(default_admin)
        session.commit()
        return "Create default admin creds here"

@auth.verify_password
def verify_password(username_or_token, password):
    # first try to authenticate by token
    user = User.verify_auth_token(username_or_token)
    if not user:
        # try to authenticate with username/password
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

@app.route('/api/admin/token')
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token(600)
    return jsonify({'token': token.decode('ascii'), 'duration': 600})

@app.route('/api/admin/login', methods=['POST'])
def api_admin_login():
    
    return jsonify({ 'hoie': "JSON with token"})

@app.route('/admin/login', methods=['GET'])
def admin_login():
    return render_template('login.html', title="Portfolio Management Login")
	
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
