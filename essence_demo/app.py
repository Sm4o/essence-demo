import requests
from flask import (
    Flask,
    request, 
    redirect,
    url_for,
)
from flask_login import (
    LoginManager, 
    login_user, 
    UserMixin, 
)
from oauthlib.oauth2 import WebApplicationClient

from essence_demo.config import Config
# from essence_demo.views.views import ViewModel

login_manager = LoginManager()

@login_manager.unauthorized_handler
def unauthenticated():
    client = WebApplicationClient(Config().GITHUB_CLIENT_ID)
    redirect_url = client.prepare_request_uri('https://github.com/login/oauth/authorize', 
                                              redirect_url=f"{request.url_root}/login/callback")
    return redirect(redirect_url)


class User(UserMixin):
    def __init__(self, name):
        self.id = name 


@login_manager.user_loader
def load_user(name):
    return User(name)


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

    login_manager.init_app(app)

    client = WebApplicationClient(Config().GITHUB_CLIENT_ID)

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    @app.route('/login/callback', methods=['GET'])
    def login_callback():
        code = request.args.get('code')
        # Obtain an access token
        url, headers, data = client.prepare_token_request(
            "https://github.com/login/oauth/access_token", 
            client_id=Config().GITHUB_CLIENT_ID, 
            client_secret=Config().GITHUB_CLIENT_SECRET,
            code=code,
        )
        headers['Accept'] = 'application/json'  
        response = requests.post(url, data=data, headers=headers)
        client.parse_request_body_response(response.text)
        url, headers, _ = client.add_token('https://api.github.com/user', headers=headers)
        github = requests.get(url, headers=headers)
        github_user = github.json()
        name = github_user['login']
        user = User(name)
        login_user(user)
        app.logger.info("User %s logged in" % name)
        return redirect(url_for('main.dashboard'))

    return app


if __name__ == '__main__':
    app = create_app() 
    app.run()
