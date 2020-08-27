# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from datetime import timedelta
import sys
import atexit

host_path = r"/etc/hosts"
redirect = "127.0.0.1"
websites = ["www.facebook.com", "https://www.facebook.com", "www.varzesh3.com"]


@atexit.register
def quite():
    enable_sites()
    print('bye ')


def enable_sites():
    with open(host_path, 'r+') as file:
        content = file.readlines();
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
    sec = 0
    while True:
        time.sleep(1)
        sys.stdout.write("\r%s" % str(timedelta(seconds=sec)))
        sys.stdout.flush()
        sec += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    block_sites()
    timer()

