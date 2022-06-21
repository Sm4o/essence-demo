from flask import (
    Flask,
    Response,
    request,
    redirect,
)

from essence_demo.config import Config
from essence_demo.extensions import login_manager, oauth_client
from essence_demo.user.models import User


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config())
    configure_extensions(app)
    configure_blueprints(app)
    return app


def configure_extensions(app: Flask) -> None:
    @login_manager.unauthorized_handler
    def unauthenticated() -> Response:
        redirect_url = oauth_client.prepare_request_uri(
            "https://github.com/login/oauth/authorize",
            redirect_url=f"{request.url_root}/login/callback",
        )
        return redirect(redirect_url)

    @login_manager.user_loader
    def load_user(name) -> User:
        return User(name)

    login_manager.init_app(app)


def configure_blueprints(app: Flask) -> None:
    from .auth.auth import auth as auth_blueprint
    from .dashboard.dashboard import dash as dashboard_blueprint

    for bp in [auth_blueprint, dashboard_blueprint]:
        app.register_blueprint(bp)


if __name__ == "__main__":
    app = create_app()
    app.run()
