# showroom-booking

Harvey Norman Commercial has a state-of-the-art showroom for it's products to sell to its clients, including Ovens, Dishwashers, Tapware and Sanitaryware. Despite bringing clients from different industries through every day, the process of getting them booked is manual and tedious. There is also an automation aspect that is missing, as everything that a user has selected is written down on paper.

My application is positioned to solve and streamline this process. First, a user makes a booking online, selecting a date & time (either 9:30am or 1:30pm). After entering their contact details, an email will be sent to the staff email where an appointment is made.

As of right now, it's merely an MVC, but my future plans are:

- Once the appointment has started, a staff member can add product codes from the session. From here they can submit to the CRM API which will generate the opportunity work flow.
- The user can log in and manage their own bookings.
- Redesign the UI
- The admin can also CONFIRM or CANCEL the booking via the email

Live site: https://showroom-booking.onrender.com

If it doesn't work, please retry in 5 minutes for it to bootup again.

# Challenges:

This was my first time implementing Postgres into a project of mine as well as my first time using Flask. So no doubt that a lot of the challenges were more growing pains understanding the ins and outs of the framework.

Outside of Flask, I would say the challenge (and will definitely be a hurdle in the future) is the Email API. At the moment I'm using SendGrid which is a freemium service that allows me to authorize a sender (my personal email) which sends an email to the user. The issue however is that gmail picks it up as a spam email so it goes to the junk folder. Microsoft also have an API which I'll explore, but for now since I'm prototyping this I'll keep it like such.

## TODO

- Disallow user to delete themselves
- Cleanup the dirty code
- There's too many SQL queries (IMO), let's make it more efficient
- Allow user to change password
- Return requested URL
- Flesh out Email functionality
