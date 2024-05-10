import time


class EmailSender:
    @staticmethod
    def send_email(to_address, subject, body):
        print(f"Sending promotional email and Newsletters to {to_address}...")
        time.sleep(2)
        print("Email sent!")
        print(f"\nSubject: {subject}")
        print(f"Body: {body}\n")


def handle_request(emails):
    email_sender = EmailSender()
    for email in emails:
        email_sender.send_email(email, "Special promo code for 10% Off",
                                "Check out our new Merchandise on the website: www.YourMom.com")


handle_request(["user1@example.com", "user2@example.com", "user3@example.com"])
