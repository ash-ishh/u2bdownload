from modal import App, Image, asgi_app
from main import app as fh_app

image = (
    Image.debian_slim(python_version="3.12")
    .pip_install("python-fasthtml")
    .pip_install("pytubefix")
)

app = App("u2bdownload")


@app.function(image=image)
@asgi_app()
def get():
    return fh_app
