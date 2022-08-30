from flask import Flask, render_template, request, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

from helpers import get_logger

from dotenv import load_dotenv
import os
import string
import youtube_dl_wrapper

logger = get_logger("main")
load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['TEMPLATES_AUTO_RELOAD'] = True
bootstrap = Bootstrap(app)

class LinkForm(FlaskForm):
    url = StringField("Youtube Link: ",validators=[DataRequired(),URL()])
    submit = SubmitField("Get Download Links")

@app.route('/',methods=["GET","POST"])
def index():
    form = LinkForm()
    title = None
    error_message = None
    video_urls = {}

    if (form.validate_on_submit()):
        # if post get video links
        logger.info(f"Request from: {request.remote_addr}")
        url = session["url"] = form.url.data
        video_information = youtube_dl_wrapper.get_video_information(url)
        title = video_information['title']
        video_urls = video_information['video_urls']
        error_message = video_information['error_message']

    return render_template("index.html", form=form, title=title, video_urls=video_urls, error_message=error_message)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404


if __name__ == "__main__":
    app.run()
