from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '6d9a7a812296d7d87ca519e2'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
from market import routes
