from flask import Flask
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import imaplib
import email
from email.header import decode_header

app = Flask(__name__)


# TODO: Create a function that can received an email message
def received_email(self):
    """
    probably should be return dictionary (or maybe any other data structure whatever the best)
    example_return = {
        "sender" : "example@gmail.com"
        "subject" : "Example Subject"
        "text" : "Hello this is example email"
    }
    """
    pass


# TODO: Create a function that can send an email message
def send_email(self, subject, body, to):
    """
    Either AI or other method to separate subject, body, and to argument
    """
    pass


@app.route('/')
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)