import os
from twilio.rest import Client
from dotenv import load_dotenv


load_dotenv()
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_number = os.getenv("TWILIO_PHONE_NUMBER")

client = Client(account_sid, auth_token)

def send_sms(to_number, message_body):
    try:
        message = client.messages.create(
            body=message_body,
            from_=twilio_number,
            to=to_number
        )
        print(f" Message sent to {to_number}. SID: {message.sid}")
    except Exception as e:
        print(f" Failed to send message: {e}")

if __name__ == "__main__":
    to = input("Enter recipient phone number (e.g., +919876543210): ")
    msg = input("Enter your message: ")
    send_sms(to, msg)
