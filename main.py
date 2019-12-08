import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

login = input ('SMTP login :')
password = input ('SMTP pass :')
msg = MIMEMultipart('mixed')

sender = input ('sender mail :')
recipient = input ('recipient mail :')

msg['Subject'] = input ('Subject :')
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
try:
    print ("Mail Gonderildi")
except:
    print ("Mail Gonderilemedi")
 
