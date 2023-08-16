from datetime import datetime, timedelta
from email.message import EmailMessage
import ssl
import smtplib
import imaplib
import email
from imap_tools import MailBox, AND
import time

# for sendind
email_sender = "chloedarcy2007@gmail.com"
email_password = "jcheknyjdpehptjy"
email_receiver = "chloedarcy2007@gmail.com"  # change

skipDateStart = None
skipDateEnd = None
dontSignUpTime = []
middleDay = None


def readEmail():
    global dontSignUpTime
    global skipDateStart
    global skipDateEnd
    global messageBody
    with MailBox("imap.gmail.com").login(email_sender, email_password, initial_folder="DRIVE") as mailbox:
        unseen_emails = list(mailbox.fetch("UNSEEN"))
        if unseen_emails:
            messageBody = unseen_emails[-1].text
            # send format 2023-07-02 until 2023-07-10
            calcSkipDates(messageBody[:10], messageBody[-12:-2])
            return dontSignUpTime
        else:
            return []


def calcSkipDates(skip_date_start, skip_date_end):
    global dontSignUpTime

    skipDateStart = datetime.strptime(skip_date_start, "%Y-%m-%d")
    skipDateEnd = datetime.strptime(skip_date_end, "%Y-%m-%d")
    skipDateStart -= timedelta(days=6)
    skipDateEnd -= timedelta(days=5)

    dontSignUpTime.append(str(skipDateStart))

    days = (skipDateEnd - skipDateStart).days
    middleDay = skipDateStart

    if days > 1:  # i think 1
        for i in range(days - 1):
            middleDay += timedelta(days=1)
            dontSignUpTime.append(str(middleDay))

    dontSignUpTime.append(str(skipDateEnd))

    for i in range(len(dontSignUpTime)):
        dontSignUpTime[i] = dontSignUpTime[i].replace(' 00:00:00', '')


readEmail()


def sendEmail(subject, body):

    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


# sendEmail("test", "test")
# readEmail()
