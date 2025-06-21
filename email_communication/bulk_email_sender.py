import os
import ssl
import smtplib
from email.message import EmailMessage
import pandas as pd
from dotenv import load_dotenv


load_dotenv()  
SMTP_HOST = os.getenv("SMTP_HOST")
SMTP_PORT = int(os.getenv("SMTP_PORT", "465"))
SMTP_USER = os.getenv("SMTP_USER")
SMTP_PASS = os.getenv("SMTP_PASS")
FROM_NAME = os.getenv("FROM_NAME", SMTP_USER)

assert all([SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS]), "Missing SMTP settings!"


try:
    df = pd.read_csv("contacts.csv")
except FileNotFoundError:
    raise SystemExit("contacts.csv not found. Put it in the same folder.")

required_cols = {"email", "subject", "body"}
if not required_cols.issubset(df.columns):
    raise SystemExit(f"CSV must contain columns: {', '.join(required_cols)}")


context = ssl.create_default_context()
with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT, context=context) as server:
    server.login(SMTP_USER, SMTP_PASS)
    for _, row in df.iterrows():
        msg = EmailMessage()
        msg["From"] = f"{FROM_NAME} <{SMTP_USER}>"
        msg["To"] = row["email"]
        msg["Subject"] = row["subject"]
        msg.set_content(row["body"])

        try:
            server.send_message(msg)
            print(f" Sent to {row['email']}")
        except Exception as e:
            print(f" Failed to {row['email']}: {e}")
