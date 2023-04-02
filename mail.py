import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the email parameters
sender = "rahamatulla.khaja44@gmail.com"
recipient = "khaja.rahamatulla44@gmail.com"
subject = "This is subject"
message = "This is message"

# Create a MIME multipart message object
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = subject

# Attach the message body to the email
msg.attach(MIMEText(message, 'plain'))

# Connect to the SMTP server and send the email
smtp_server = smtplib.SMTP('smtp.gmail.com', 587) # replace with your SMTP server
smtp_server.starttls()
smtp_server.login(sender, 'ksuqsjwqhdyuttwu') # replace with your password or use a secure method
smtp_server.sendmail(sender, recipient, msg.as_string())
smtp_server.quit()
print("Email sent successfully!")
