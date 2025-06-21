from validate_email_address import validate_email
import warnings
warnings.filterwarnings("ignore") 

def check_email(email):
    is_valid = validate_email(email_address=email, check_format=True, check_blacklist=True, check_dns=True, check_smtp=True, smtp_timeout=10, dns_timeout=10)
    if is_valid:
        print(f" Valid: {email}")
    else:
        print(f" Invalid: {email}")

if __name__ == "__main__":
    email = input("Enter an email address to validate: ").strip()
    check_email(email)
