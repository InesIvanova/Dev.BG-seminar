from flask import Flask
from blog.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
db.init_app(app)

from blog.models.contact import Email, Phone
from blog.models.user import User
from blog.models.post import Post