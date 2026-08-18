# guests = ["Alice", "Bob", "jake", "Kate", "John"]

# for guest in guests:
#     print(guest)

# function to get guests from database
import time

def get_guests_from_database():
    # mock data
    guests = ["Alice", "Bob", "jake", "Kate", "John"]

    for guest in guests:
        yield guest

# send mail

def sendMail():
    # generator object
    guest_generator = get_guests_from_database()

    print(f"guest_generator : {guest_generator}")

    for guest in guest_generator:
        time.sleep(2)
        print(f"Sending mail to guest : {guest}")
        time.sleep(2)
        print(f"Mail sent to {guest}")
        time.sleep(2)

sendMail()

import time

def sendMailToGuests():
    # mock data 

    guests = ["Alice", "Bob", "Kate", "Jake", "John"]
    for guest in guests:
        # delay for 2s
        time.sleep(2)
        print(f"Sending mail to guest : {guest}")
        # delay for 2s
        time.sleep(2)
        print(f"Mail sent to {guest}")
        # delay for 2s
        time.sleep(2)

# calling the function
sendMailToGuests()
