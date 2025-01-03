from flask import Blueprint, render_template
from controllers.user import add_user_function
import sys

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@main.route('/adduser', methods=['GET','POST'])
def add_user():
    data = add_user_function()
    print(data,file=sys.stderr)
    return render_template('adduser.html', data=data)
