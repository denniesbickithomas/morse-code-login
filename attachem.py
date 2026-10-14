import smtplib
##from email.MIMEMultipart import MIMEMultipart
##from email.MIMEBase import MIMEBase
##from email.MIMEText import MIMEText
##from email.Utils import COMMASPACE, formatdate
##from email import Encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import email.encoders as Encoders
import os

# Credentials live in config.py (gitignored). Use a Gmail App Password, not your normal password.
from config import EMAIL_USER as USERNAME, EMAIL_APP_PASSWORD as PASSWORD

def sendMail(to, subject, text, files=[]):
    assert type(to)==list
    assert type(files)==list

    msg = MIMEMultipart()
    msg['From'] = USERNAME
    msg['To'] = COMMASPACE.join(to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    
    msg.attach( MIMEText(text) )

    for file in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(file,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"'
                       % os.path.basename(file))
        msg.attach(part)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo_or_helo_if_needed()
        server.starttls()
        server.ehlo_or_helo_if_needed()
        server.login(USERNAME,PASSWORD)
        server.sendmail(USERNAME, to, msg.as_string())
        server.quit()

if __name__ == "__main__":
    # Manual test: sends the last captured frame to the alert recipient in config.py
    from config import ALERT_EMAIL_TO
    sendMail([ALERT_EMAIL_TO],
             "Unknown face detected",
             "An unknown face attempted to log in. Snapshot attached.",
             ["frame.png"])
