import smtplib
from email.mime.text import MIMEText
sender = 'your sender email'
to = 'send to someone'
msg = MIMEText(result)
msg['Subject'] = 'This is the topic'
msg['From'] = sender
msg['To'] = to
server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()
server.login("your user name account", "your password")
server.sendmail(sender, [to], msg.as_string())
server.quit()