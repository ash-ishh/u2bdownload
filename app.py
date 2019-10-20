from flask import Flask, render_template, request, redirect, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required, URL

from helpers import get_logger

from dotenv import load_dotenv
import os
import utube_dl

logger = get_logger("main")
load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['TEMPLATES_AUTO_RELOAD'] = True
bootstrap = Bootstrap(app)

class LinkForm(FlaskForm):
    url = StringField("Youtube Link: ",validators=[Required(),URL()])
    submit = SubmitField("Get Download Links")

@app.route('/',methods=["GET","POST"])
def index():
    form = LinkForm()
    links = list()
    name = None
    nolinks = False

    if(form.validate_on_submit()):
        logger.info(f"Request from: {request.remote_addr}")
        session["url"] = form.url.data
        name, links = utube_dl.download(session.get("url"))
        nolinks = True if len(links) == 0 else False
    return render_template("index.html", form=form, links=links, nolinks=nolinks, name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404


if __name__ == "__main__":
    app.run()
