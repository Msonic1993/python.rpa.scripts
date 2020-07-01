import smtplib,ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import encoders
from SelectDataFromDB import DBSelectQuery

class Send:
    GetFileName = DBSelectQuery.tempExtractFileName

    def SendMail(self):

        print("Start sending mail with file" + self.GetFileName)

        file = 'C:\\temp_ZW\\' + self.GetFileName
        username = 'noreply@xx.pl'
        password = 'xx'
        send_from = 'noreply@xx.pl'
        send_to = 'xx.xx-xx@xx.com'

        #Parametry, które są zawarte w mailu
        msg = MIMEMultipart()
        msg['From'] = send_from
        msg['To'] = send_to
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = '[xx] xx xx xx'
        body = 'Dzień dobry,\n\n ' \
               'W załaczniku znajduje się plik csv z danymi dziennymi   xx.\n\n ' \
               'Pozdrawiamy, \n' \
               'Zespół xx'

        #Tworzenie maila
        msg.attach(MIMEText(body))
        fp = open(file, 'rb')
        part = MIMEBase('application', 'csv')
        part.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment', filename=self.GetFileName)
        msg.attach(part)

        #logowanie do serwera poczty
        smtp = smtplib.SMTP('mail.xx.xx')
        smtp.ehlo()
        smtp.starttls()
        smtp.login(username, password)

        #Wysyłka maila
        smtp.sendmail(send_from, send_to.split(',') , msg.as_string())
        smtp.quit()
        print("Mail sended successfully")



