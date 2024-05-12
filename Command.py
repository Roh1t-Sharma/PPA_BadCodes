from threading import Thread
import time


# Command Interface
class Command:
    def execute(self):
        pass

    def undo(self):
        pass


# Concrete Command
class SendEmailCommand(Command):
    def __init__(self, email_sender, to_address, subject, body):
        self.email_sender = email_sender
        self.to_address = to_address
        self.subject = subject
        self.body = body
        self.sent = False  # Tracks if the email was sent

    def execute(self):
        self.email_sender.send_email(self.to_address)
        self.sent = True

    def undo(self):
        if self.sent:
            print(f"Undoing email to {self.to_address}: Mail has been deleted.")
            self.sent = False


# Receiver
class EmailSender:
    @staticmethod
    def send_email(to_address):
        print(f"Sending promotional email and Newsletters to {to_address}...")
        time.sleep(1)  # Simulates sending delay
        print("Emails sent!")


# Invoker
class TaskScheduler:
    def __init__(self):
        self.commands = []
        self.completed_commands = []  # To keep track of executed commands

    def add_command(self, command):
        self.commands.append(command)

    def run(self):
        threads = [Thread(target=self.execute_command, args=(cmd,)) for cmd in self.commands]
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    def execute_command(self, command):
        command.execute()
        self.completed_commands.append(command)

    def undo_last_command(self):
        if self.completed_commands:
            last_command = self.completed_commands.pop()
            last_command.undo()


# Client
def handle_request(emails):
    email_sender = EmailSender()
    scheduler = TaskScheduler()
    for email in emails:
        cmd = SendEmailCommand(email_sender, email, "Special promo code for 10% Off",
                               "Check out our new Merchandise on the website: www.MerchClub.com")
        scheduler.add_command(cmd)
    scheduler.run()
    # Simulate undoing the last sent email
    scheduler.undo_last_command()


# Simulating request with a list of emails
handle_request(["user1@mail.com", "user2@mail.com", "user3@mail.com"])
