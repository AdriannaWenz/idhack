from flask import render_template
from app import app
from app import db
from app.models import User, Post

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')
@app.route('/experts')
def experts():
    expertz = User.query.all()
    return render_template('experts.html', title="Experts", experts = expertz)
@app.route('/chat')
