#sending mail using python



import smtplib

s=smtplib.SMTP('smtp.gmail.com','587')
s.starttls()
sender='chandanabhat163@gmail.com'
reciever='chethanmanu7777@gmail.com'
msg='hi!!how r u?'
s.login(sender,'chinnuchandu')
s.sendmail(sender,reciever,msg)
print("msg sent successfully")
s.quit()