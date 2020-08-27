# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import datetime
import sys
import atexit
from model import Session
import db

sec = 0
task = ""
host_path = r"/etc/hosts"
redirect = "127.0.0.1"
websites = ["www.facebook.com", "https://www.facebook.com", "www.varzesh3.com", "https://www.varzesh3.com/"]


@atexit.register
def quite():
    enable_sites()
    session = Session(task, datetime.datetime.now().date(), sec)
    db.save_session(db.init_db(), session)
    print("you deep worked for %i secondes!" % sec)


def enable_sites():
    with open(host_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in websites):
                file.write(line)
        file.truncate()


def block_sites():
    with open(host_path, "r+") as fileptr:
        content = fileptr.read()
        for website in websites:
            if website in content:
                pass
            else:
                fileptr.write(redirect + "    " + website + "\n")


def timer():
    global sec
    while True:
        sys.stdout.write("\r%s" % str(datetime.timedelta(seconds=sec)))
        sys.stdout.flush()
        time.sleep(1)
        sec += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    task = raw_input("enter the task you will deep work on for next 25 min: ")
    time.sleep(1)
    print("block out all possible distraction.")
    time.sleep(1)
    print("Deep Work, with all your might!")
    block_sites()
    time.sleep(1)
    timer()
