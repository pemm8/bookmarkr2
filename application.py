from flask import flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(**config_overrides):
	app = Flask(__name__)

	# app config
	app.config.from_pyfile('config.py')
	app.config.update(config_overrides)

	# init db
	db.init_app()

	# register blueprints

	# blueprint: users

	# blueprint: grid


	return app