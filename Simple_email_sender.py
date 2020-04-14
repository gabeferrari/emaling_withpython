import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Who is sending'
email['to'] = 'E-mails to send'
email['subject'] = 'E-mail subject'

email.set_content('E-mail content...Write here')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login('E-MAIL ADDRESS', 'PASSWORD')
	smtp.send_message(email)
	print('all good boss!')
