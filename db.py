from app import app
from flask_sqlalchemy import SQLAlchemy
from os import getenv

#app.secret_key = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
if app.config["SQLALCHEMY_DATABASE_URI"].startswith("postgres://"):
    app.config["SQLALCHEMY_DATABASE_URI"] = app.config["SQLALCHEMY_DATABASE_URI"].replace(
        "postgres://", "postgresql://", 1)

db = SQLAlchemy(app)

