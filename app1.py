import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "adikusuma1402@gmail.com"
toaddr = "adikusuma1402@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = 'Send mail with python'

body = "Ini pesan dikirim lewat email"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "lintangutara")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()