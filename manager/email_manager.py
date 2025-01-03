import os
from smtplib import SMTP
from dotenv import load_dotenv

class MailManager:
    def __init__(self):
        load_dotenv()
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("EMAIL_PASS")


    def send_email(self, name: str, email: str, phone: str, message: str):
        message_to_send = f"""
            Name: {name}
            Email: {email}
            Phone: {phone}
            Message: {message}
        """
        
        with SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user = self.email, password = self.password)
            connection.sendmail(
                from_addr=self.email,
                to_addrs=self.email,
                msg=f"Subject:New contact\n\n{message_to_send}")
            
