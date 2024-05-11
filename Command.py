from threading import Thread
import time

# Command Interface
class Command:
    def execute(self):
        pass

# Concrete Command
class SendEmailCommand(Command):
    def __init__(self, email_sender, to_address, subject, body):
        self.email_sender = email_sender
        self.to_address = to_address
        self.subject = subject
        self.body = body

    def execute(self):
        self.email_sender.send_email(self.to_address)

# Receiver
class EmailSender:
    def send_email(self, to_address):
        print(f"Sending promotional email and Newsletters to {to_address}...")
        time.sleep(1)
        print("Emails sent!")


# Invoker
class TaskScheduler:
    def __init__(self):
        self.commands = []
        self.subject = None
        self.body = None

    def add_command(self, command):
        self.commands.append(command)
        # Assuming all emails share the same subject and body
        self.subject = command.subject
        self.body = command.body

    def run(self):
        threads = [Thread(target=cmd.execute) for cmd in self.commands]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

        # Print details after all emails are sent
        self.print_email_details()

    def print_email_details(self):
        print(f"\nSubject: {self.subject}")
        print(f"Body: {self.body}")

# Client
def handle_request(emails):
    email_sender = EmailSender()
    scheduler = TaskScheduler()
    for email in emails:
        cmd = SendEmailCommand(email_sender, email, "Special promo code for 10% Off",
                               "Check out our new Merchandise on the website: www.YourMom.com")
        scheduler.add_command(cmd)
    scheduler.run()

# Simulating request with a list of emails
handle_request(["user1@mail.com", "user2@mail.com", "user3@mail.com"])
