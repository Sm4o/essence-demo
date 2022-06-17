import os


class Config:
    def __init__(self):
        self.SECRET_KEY = os.environ.get('SECRET_KEY')
        self.GITHUB_CLIENT_ID = os.environ.get('GITHUB_CLIENT_ID')
        self.GITHUB_CLIENT_SECRET = os.environ.get('GITHUB_CLIENT_SECRET')

        if not self.SECRET_KEY:
            raise ValueError("No SECRET_KEY set for Flask application. Did you follow the setup instructions?")

        if not self.GITHUB_CLIENT_ID or not self.GITHUB_CLIENT_SECRET:
            raise ValueError("No GITHUB_CLIENT_ID or GITHUB_CLIENT_SECRET provided")
