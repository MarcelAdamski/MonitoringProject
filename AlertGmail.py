import smtplib
import functools
import sys

def email_alert(msg):
    address = 'enterEmailAdressHere'
    password = 'enterGmailPasswordHere'
    mailFrom = 'Automation system'
    mailTo = ['thisEmailWillReceiveAlert@gmail.com', 'thisEmailAlsoWillReceiveAlert@gmail.com']
    mailSubject = 'Your machine is offline'
    mailBody = '''Hello!

{}

Have a nice day!'''.format(msg)
    message = '''From: {}
Subject: {}

{}
'''.format(mailFrom, mailSubject, mailBody)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(address, password)
        server.sendmail(address, mailTo, message.encode('utf-8'))
        server.close()
        return True
    except:
        print('error while sending email', sys.exc_info())
        return False
if __name__ == "__main__":
    SendAlertEmailFromGmail = functools.partial(email_alert, user, password, mailSubject=mailSubject)
    SendAlertEmailFromGmail(mailFrom=mailFrom, mailTo=mailTo, mailBody=mailBody)
