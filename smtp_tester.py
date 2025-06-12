import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


smtp_server = "smtp.office365.com"
smtp_port = 587
sender_email = "x"
password = "x"


# Email content
receiver_email = "yyyy"
subject = "Test Email from Python via M365 SMTP"
body = "This is a test email sent from Python using Microsoft 365 SMTP."

# Construct email
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject
msg.attach(MIMEText(body, "plain"))


# Send email
try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, password)
        server.send_message(msg)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {e}")