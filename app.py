# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Under Construction!"

@app.route('/contact', methods=['GET'])
def contact():
    return "Contact page"
    
if __name__ == "__main__":
    app.run()
