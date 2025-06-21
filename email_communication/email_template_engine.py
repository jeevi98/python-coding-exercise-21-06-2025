import os
import ssl
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import pandas as pd
from jinja2 import Template


load_dotenv()
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", 465))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
FROM_NAME = os.getenv("FROM_NAME", "Your Name")

with open("email_template.txt", "r") as f:
    template_str = f.read()
template = Template(template_str)


contacts = pd.read_csv("contacts.csv")


context = ssl.create_default_context()
with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as server:
    server.login(SMTP_USER, SMTP_PASS)

    for _, row in contacts.iterrows():
        msg = EmailMessage()
        msg["From"] = f"{FROM_NAME} <{SMTP_USER}>"
        msg["To"] = row["email"]
        msg["Subject"] = "Exclusive Discount Just for You!"

     
        email_body = template.render(row.to_dict())
        msg.set_content(email_body)

        try:
            server.send_message(msg)
            print(f" Sent to {row['email']}")
        except Exception as e:
            print(f" Failed to send to {row['email']}: {e}")
