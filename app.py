# app.py
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists
from sqlalchemy import func, exc

app = Flask(__name__)
db = SQLAlchemy()
db_name = "Buford.db"
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///'+db_name
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

from models import *

if database_exists('sqlite:///instance/'+db_name):
    print(db_name + " already exists.")
else:
    print(db_name + " does not exist, will create " + db_name)
    # this is needed in order for database session calls (e.g. db.session.commit)
    with app.app_context():
        try:
            db.create_all()
        except exc.SQLAlchemyError as sqlalchemyerror:
        	print("got the following SQLAlchemyError: " + str(sqlalchemyerror))
        except Exception as exception:
        	print("got the following Exception: " + str(exception))
        finally:
        	print("db.create_all() was successfull - no exceptions were raised")

@app.route('/', methods=['GET'])
def home():
    return render_template('main.html', title="Portfolio - Dynse Clyde Sacote")

@app.route('/contact', methods=['GET'])
def contact():
    return "Contact page"
    
if __name__ == "__main__":
    app.run()
