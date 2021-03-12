#!/usr/bin/python3
"RSVP autoform"
# Copyright 2020 Tero Karvinen http://TeroKarvinen.com

from flask import Flask, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from wtforms.ext.sqlalchemy.orm import model_form
from flask_wtf import FlaskForm
import wtforms

app = Flask(__name__)
db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///autoformed.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "dUCF)mtd9MAoZ?;R|8*iB^.+TCV//0"

class Reply(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	coming = db.Column(db.Boolean, nullable=False)
	email = db.Column(db.String, nullable=False)
	name = db.Column(db.String, nullable=False)

field_args = { "email": {"validators": [wtforms.validators.Email()]} }
ReplyForm = model_form(model=Reply, base_class=FlaskForm, db_session=db.session, field_args=field_args)

@app.before_first_request
def beforeFirstRequest():
	db.create_all()

@app.route("/", methods=["GET", "POST"])
def index():
	form = ReplyForm()

	if form.validate_on_submit():
		reply = Reply()
		form.populate_obj(reply)
		db.session.add(reply)
		db.session.commit()
		flash("Your reply has been added. Welcome!")
		return redirect("/")
	replies = db.session.query(Reply)
	return render_template("replies.html", form=form, replies=replies)

def main():
	app.run(debug=True)

if __name__ == "__main__":
	main()
