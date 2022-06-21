from flask import Blueprint
import requests
from flask import (
    redirect,
    url_for,
    request,
)
from flask_login import (
    login_required, 
    logout_user,
    login_user,
)

from essence_demo.config import Config
from essence_demo.extensions import oauth_client
from essence_demo.user.models import User
# from essence_demo.views.views import ViewModel

auth = Blueprint('auth', __name__)


@auth.route('/login')
@login_required
def login():
    return redirect(url_for("dash.dashboard"))


@login_required
@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("dashboard.index"))


@auth.route('/login/callback', methods=['GET'])
def login_callback():
    code = request.args.get('code')
    # Obtain an access token
    url, headers, data = oauth_client.prepare_token_request(
        "https://github.com/login/oauth/access_token", 
        client_id=Config().GITHUB_CLIENT_ID, 
        client_secret=Config().GITHUB_CLIENT_SECRET,
        code=code,
    )
    headers['Accept'] = 'application/json'  
    response = requests.post(url, data=data, headers=headers)
    oauth_client.parse_request_body_response(response.text)
    url, headers, _ = oauth_client.add_token('https://api.github.com/user', headers=headers)
    github = requests.get(url, headers=headers)
    github_user = github.json()
    name = github_user['login']
    user = User(name)
    login_user(user)
    return redirect(url_for('dash.dashboard'))
