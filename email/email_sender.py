import smtplib
from email.message import EmailMessage
from email.headerregistry import Address

class EmailSender():
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_SERVER_PORT = "465"
    EMAIL_SENDER = "nguyen.tat.thanh@miyatsu.vn"
    EMAIL_SENDER_PASSWORD = "It12345!"
    EMAIL_RECIVES =['thanhntt89bk@gmail.com','5tfethut@gmail.com']
    
    SUBJECT = 'Welcome!'
    content = ''
    message = EmailMessage()
    
    #########################
    # Sending email 
    #########################
    @staticmethod
    def SendMessage():
        try:            
            EmailSender.message.set_content(EmailSender.content) 
            EmailSender.message['Subject'] = EmailSender.SUBJECT
            EmailSender.message['From'] = Address("Nguyen Tat Thanh", EmailSender.EMAIL_SENDER) 
            EmailSender.message['To'] = EmailSender.EMAIL_RECIVES

            email_server = smtplib.SMTP_SSL(EmailSender.SMTP_SERVER, EmailSender.SMTP_SERVER_PORT)
            email_server.ehlo()
            email_server.login(EmailSender.EMAIL_SENDER, EmailSender.EMAIL_SENDER_PASSWORD)
            email_server.send_message(EmailSender.message)
            email_server.close()
            print("Email sent!!!")
        except Exception as e:
            print("%s"%e)

if __name__ == "__main__":
    EmailSender.content ="Hello everyone, this email send by python client!!!"    
    
    EmailSender.SendMessage()