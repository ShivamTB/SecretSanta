import random
from send_email import send_emails
from people import PEOPLE

def assign(people):
    santa_list = list(people.keys())

    assignment = {}

    for person in people:
        secret_santa = random.choice(santa_list)
        while secret_santa == person or secret_santa in assignment:
            secret_santa = random.choice(santa_list)
            if secret_santa in assignment and assignment[secret_santa] == person:
                continue
            elif secret_santa == person:
                continue
            break
        assignment[person] = secret_santa
        santa_list.pop(santa_list.index(secret_santa))

    return assignment

send_emails(PEOPLE, assign(PEOPLE))