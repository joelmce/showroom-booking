import os
import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from helpers.booking import booking_info

message = Mail(
    from_email='joelanthony.mac@gmail.com',
    to_emails='joelanthony.mac@gmail.com',
    subject=f'New Showroom Booking',
    html_content=f'<div style="text-align: centre"><p>You have a new booking for the showroom.</p><a href="/booking?confirm=">Confirm</a><a href="/booking?cancel=">Cancel</a></div>'
)

def send_email():
    try: 
        sg = SendGridAPIClient(os.getenv('EMAIL_API_KEY'))
        response = sg.send(message)
        booking_info.clear()
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

