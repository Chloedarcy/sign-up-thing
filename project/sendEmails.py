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

dontSignUpTime = None
skipDates = None


def readEmail():
    global dontSignUpTime
    global skipDates
    with MailBox("imap.gmail.com").login(email_sender, email_password, initial_folder="DRIVE") as mailbox:
        unseen_emails = list(mailbox.fetch("UNSEEN"))
        if unseen_emails:
            latest_email = unseen_emails[-1]
            skipDates = latest_email.text
            # send format 2023-07-02
            calcSkipDates(skipDates)
            print(dontSignUpTime)
            return dontSignUpTime


def calcSkipDates(skipDates):
    global dontSignUpTime

    skipDates = skipDates[:10]
    skipDates = datetime.strptime(skipDates, "%Y-%m-%d")
    dontSignUpTime = skipDates - timedelta(days=5)
    dontSignUpTime = str(dontSignUpTime).rstrip('00:00:00')
    dontSignUpTime = "Current Date: " + dontSignUpTime
    return dontSignUpTime


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
