import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Email bot'
email['to'] = 'destination'
email['subject'] = 'I am a crazy emailer'

email.set_content(html.substitute({'name' : 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('e-mailaddres', 'password')
	smtp.send_message(email)
	print('e-mail sent!')
