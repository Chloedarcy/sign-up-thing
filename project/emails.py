import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email details
sender_email = "chloe_darcy@icloud.com"
receiver_email = "johnreo222@gmail.com"
subject = "Hello from Python"
message = "This is a test email sent using Python."

# Create a MIME message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(message, "plain"))

# Connect to the SMTP server
smtp_server = "smtp.example.com"
smtp_port = 587
smtp_username = "johnreo222@gmail.com"
smtp_password = "825055jR"

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(msg)
    print("Email sent successfully.")
