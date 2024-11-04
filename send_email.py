import smtplib
from secret import user, password

def send_emails(people, assignments):
        server = smtplib.SMTP("smtp.gmail.com", 587) # 587 (gmail port number)
        server.starttls()
        server.login(user, password)
        for person, secret_santa in assignments.items():
            receiver = people[person]
            message = "SUBJECT: SECRET SANTA\n" \
                      f"Hello {person},\n\n" \
                      f"SHHH, your secret santa person is: {secret_santa}.\n\n" \
                      "Enjoy!"
            server.sendmail(user, receiver, message)
            print("{} has been sent their secret person.".format(person))
        server.quit()