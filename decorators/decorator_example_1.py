# 3 functions 
# function 1 -> upload marks
# function 2 -> mark attendance
# function 3 -> get all users

import time

# decorator function

def calculateExecutionTime(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        # print execution time
        print(f"execution time : {end - start} seconds")

    return wrapper

@calculateExecutionTime
def uploadMarks():
    print("Uploading Marks...")
    print("Marks uploaded")

@calculateExecutionTime
def mark_attendance():
    print("Marking attendance...")  
    print("Attendance Marked ...")

@calculateExecutionTime
def getAllUsers():
    print("fetching list of users...")
    print("users fetched!")

@calculateExecutionTime
def sendMail():
    print("Sending mail...")
    print("Mail sent!")

sendMail()
uploadMarks()
mark_attendance()
getAllUsers()