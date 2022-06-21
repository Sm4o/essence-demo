from flask_login import UserMixin

# Can be extended to be SQLAlchemy https://github.com/imwilsonxu/fbone/blob/master/fbone/user/models.py

class User(UserMixin):
    def __init__(self, name):
        self.id = name 