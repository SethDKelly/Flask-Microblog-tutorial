from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Setting variable name with LoginManager for the app, flask_login library
login = LoginManager(app)

# Requiring users to login to view certain pages
# Allows use of @login_required decorator
# login_view is set to the name of the view to redirect to
# This uses dynamic name setting with url_for
# Absolute naming may also be used '/login'
login.login_view = 'login'


from app import routes, models
