from flask.ext.sqlalchemy import SQLAlchemy
from app import db
import bson

class Base(db.Model):
	__abstract__ = True

	id = db.Column(db.Integer, primary_key=True)
	isactive = db.Column(db.Boolean(), default=0, nullable=False)
	isdeleted = db.Column(db.Boolean(), default=0, nullable=False)
	added_on = db.Column(db.DateTime(), default=db.func.current_timestamp(), nullable=False)
	modified_on = db.Column(db.DateTime(), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)
