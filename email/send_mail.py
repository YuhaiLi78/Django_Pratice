import smtplib
from email.mime.text import MIMEText
from email.header import Header
from subprocess import check_output

receiver = ''
mail_host = 'smtp.gmail.com'
mail_user = 'xxx@gmail.com'
mail_pass = ''
sender = mail_user
receivers = [receiver]
log = 'This is a test'

message = MIMEText(log)
message['From'] = Header(mail_user, 'utf-8')
message['To'] = Header(str(receivers), 'utf-8')

subject = 'my test'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print("Mail sent successfully")
except smtplib.SMTPException,e:
    print(e)
