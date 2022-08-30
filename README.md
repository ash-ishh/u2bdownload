## **u2bdownload** is a simple flask based website to extract video links of given URL


Steps to run it locally:

1 - Create .env with SECRET_KEY

Linux example: `echo "SECRET_KEY=$(openssl rand -base64 12)" >> .env`

2 - Create and activate virtual envirnoment

Linux example

`$ python3 -m venv venv`

`$ source bin/activate`

2 - Install requriements

`(venv) $ pip install -r requirements.txt`

3 - Run dev webserver

`python app.py`