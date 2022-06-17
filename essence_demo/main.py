from flask import Blueprint
from flask import (
    render_template, 
)
from flask_login import (
    current_user,
    login_required,
)

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html', current_user=current_user)


@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('index.html', current_user=current_user)