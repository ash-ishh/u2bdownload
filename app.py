from flask import Flask,render_template,request
import utube_dl

app = Flask(__name__)

@app.route('/')
def index():
    link480 = ""
    link720 = ""
    return render_template("index.html",link480=link480,link720=link720)

@app.route('/links',methods=["POST","GET"])
def links():
    link480 = "yo"
    link720 = "yo"
    url = request.form['utubelink']
    links = utube_dl.download(url)
    if(len(links) == 1):
        link480 = links[0]
    elif(len(links) == 2 or len(links) > 2):
        link480 = links[1]
        link720 = links[0]
    return render_template("index.html",link480=link480,link720=link720)

if __name__ == "__main__":
    app.debug = True
    app.run()
