from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'ankitsankalp1997@gmail.com'
email_password = 'pass'

email_receiver =''

subject = 'Python email sender'
body = """
This mail is sent using python 
"""

em= EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject']= subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465,context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver,em.as_string())
