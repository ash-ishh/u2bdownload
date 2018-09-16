from flask import Flask,render_template,redirect,session,url_for,flash
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required,URL
import utube_dl

app = Flask(__name__)
app.config['SECRET_KEY'] = "ayolyricalmiraclespiritualindividualcriminalsubliminalinyourswimmingp00l"
app.config['TEMPLATES_AUTO_RELOAD'] = True
bootstrap = Bootstrap(app)

class LinkForm(Form):
    u2blink = StringField("Youtube Link: ",validators=[Required(),URL()])
    submit = SubmitField("Get Download Links")

@app.route('/',methods=["GET","POST"])
def index():
    form = LinkForm()
    if(form.validate_on_submit()):
        session["url"] = form.u2blink.data
        name, links = utube_dl.download(session.get("url"))
        session["name"] = name
        session["link480"] = None
        session["link720"] = None

        for f,link in links:
            if f == 18:
                session["link480"] = link
            if f == 22:
                session["link720"] = link
        if session["link480"] is None and session["link720"] is None:
            flash("Sorry :( cannot generate links of this url..")
        return redirect(url_for("index"))
    return render_template("index.html",form=form,link480=session.get("link480"),link720=session.get("link720"),name=session.get("name"))


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

if __name__ == "__main__":
    #app.debug = True
    app.run()
