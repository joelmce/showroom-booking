from dotenv import load_dotenv
load_dotenv()

import os
import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='joelanthony.mac@gmail.com',
    to_emails='joelanthony.mac@gmail.com',
    subject='This is a test!',
    html_content='<strong>Another test!</strong>'
)

def send_email():
    try: 
        sg = SendGridAPIClient(os.getenv('EMAIL_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)