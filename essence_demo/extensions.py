from essence_demo.config import Config

from flask_login import LoginManager
login_manager = LoginManager()

from oauthlib.oauth2 import WebApplicationClient
oauth_client = WebApplicationClient(Config().GITHUB_CLIENT_ID)