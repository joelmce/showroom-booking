import os
import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='joelanthony.mac@gmail.com',
    to_emails='joelanthony.mac@gmail.com',
    subject=f'New Showroom Booking',
    html_content=f'<div style="text-align: centre"><p>You have a new booking for the showroom.</p><a href="/booking?confirm=">Confirm</a><br/><a href="/booking?cancel=">Cancel</a></div>'
)

def send_email():
    try: 
        sg = SendGridAPIClient(os.getenv('EMAIL_API_TOKEN'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

