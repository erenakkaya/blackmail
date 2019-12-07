import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

login = 'login.smtp.com'
password = 'pass.smtp'
msg = MIMEMultipart('mixed')

sender = 'mail@example.com'
recipient = 'recipient@exampleee.com'

msg['Subject'] = 'KONU KONU KONU'
msg['From'] = sender
msg['To'] = recipient

text_message = MIMEText('Mesaj Buraya Yazilacak.(Message is here)', 'plain')
html_message = MIMEText('Buda resim falan eklersen diye Mesaj yani.(With images Messages)', 'html')
msg.attach(text_message)
msg.attach(html_message)

mailServer = smtplib.SMTP('smtp-relay.sendinblue.com', 587) # 8025, 587 and 25 can also be used.
mailServer.ehlo()
mailServer.ehlo()
mailServer.login(login, password)
mailServer.sendmail(sender, recipient, msg.as_string())
mailServer.close()
