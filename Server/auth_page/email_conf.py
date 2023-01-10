import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Template
import random
from auth_page.routes import session

    
def genCode():
    return random.randrange(100000, 999999)

def sendCode(email):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Confirmation Code"
    msg['From'] = "test1database.project@gmail.com"
    msg['To'] = email
    
    # Create the body of the message (a plain-text and an HTML version).
    template = Template('''<html>
    <head>
        <style type="text/css">
        body, div {
            font-family: Helvetica, Arial, sans-serif;
            font-size: 14px;
        }
        a {
            text-decoration: none;
        }
        </style>
        <title></title>
    </head>
    <body>
    <center>
        <p>
        The verification code is:
        </p>

        <div>
            <p>
                <strong>{{code}}</strong>
            </p>
        </div>
    </center>
    </body>
    </html>''')

    html = template.render(code = session['OTP'])

    part2 = MIMEText(html, 'html')
    msg.attach(part2)

    s = smtplib.SMTP('smtp.gmail.com', 587)    
    s.ehlo() 

    #Start TLS for security
    s.starttls()
    
    # #Your Gmail authentication
    s.login("test1Database.Project@gmail.com", "junceituwflsrrth")

    #Send the mail
    s.sendmail("test1database.project@gmail.com", email, msg.as_string())
    
    #Terminate
    s.quit()
        




