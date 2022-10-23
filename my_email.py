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
information = input()

while information != 'Stop':
    split_info = information.split(" ")
    sender = split_info[0]
    receiver = split_info[1]
    content = split_info[2]
    email = Email(sender, receiver, content)
    emails.append(email)

    information = input()

sent_emails = list(map(lambda x: int(x), input().split(', ')))
for x in sent_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())
