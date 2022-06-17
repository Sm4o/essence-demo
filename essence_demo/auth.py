from flask import Blueprint
import requests
from flask import (
    redirect,
    url_for,
)
from flask_login import (
    login_required, 
    logout_user,
)

from essence_demo.config import Config
# from essence_demo.views.views import ViewModel

auth = Blueprint('auth', __name__)


@auth.route('/login')
@login_required
def login():
    return redirect(url_for("main.dashboard"))


@login_required
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("main.index"))
