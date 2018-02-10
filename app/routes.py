# <One Light Global>
# Copyright © <2018> <MIT>
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


from flask import render_template, request
from app import app
from app import db
from app.models import User, Post, Conversation
from sqlalchemy import and_, or_

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')
@app.route('/experts')
def experts():
    expertz = User.query.all()
    return render_template('experts.html', title="Experts", experts = expertz)
@app.route('/conversation', methods=['GET', 'POST'])
def conversation():
    expert = request.args.get('expert', None)
    anon = User.query.filter_by(username="Anonymous")
    #convo = Conversation.query.filter_by(or_(user1_id=expert.id, user2_id=anon.id), (user2_id=expert.id, user1_id=anon.id)).first_or_404()
    convo = Conversation.query.get(1)
    posts = Post.query.filter_by(convId=convo.id)
    return render_template('conversation.html', title="Conversation", posts = posts)
