from flask import render_template
from flask_mail import Message
from app import mail

def send_email(user):

    token = user.get_reset_token()

    msg = Message(
    subject = "Nominator Password Reset",
    sender = ("Nominator",['MAIL_USERNAME']),
    recipients = [user.email],
    body= "This is the reset link for your nominator account. ",
    html = render_template('reset_email.html', user=user, token=token))
    
    mail.send(msg)

    return "RESET LINK IS SENT TO YOUR EMAIL"