class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False


    def send(self):
        self.is_sent = True


    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []

command = input()

while command != "Stop":
    command = command.split()
    sender = command[0]
    receiver = command[1]
    content = command[2]
    email = Email(sender, receiver, content)
    emails.append(email)

    command = input()

indices_of_sent_emails = [int(x) for x in input().split(", ")]

for index in indices_of_sent_emails:
    emails[index].send()

for email in emails:
    print(email.get_info())
