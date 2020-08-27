# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
from datetime import timedelta
import sys


def timer():
    sec = 0
    while True:
        time.sleep(1)
        sys.stdout.write("\r%s" % str(timedelta(seconds=sec)))
        sys.stdout.flush()
        sec += 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    timer()

