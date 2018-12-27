import smtplib


def sendemail():

    gmail_user = '****@gmail.com'
    gmail_password = '****'


    fromx = '*****@gmail.com'
    to = '****@bitmain.com'
    subject = 'Li Shuo'  # Line that causes trouble
    msg = 'Subject:{}\n\nexample'.format(subject)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.ehlo()
    server.login('*****@gmail.com', 'password')
    server.sendmail(fromx, to, msg)
    server.quit()


sendemail()