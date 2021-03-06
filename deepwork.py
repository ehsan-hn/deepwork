#!/usr/bin/env python
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time
import datetime
import sys
import atexit
from model import Session
import db
import csv
import click
from tabulate import tabulate

sec = 0
this_task = ""
host_path = r"/etc/hosts"
app_path = r"/snap/deepwork/x1"
redirect = "127.0.0.1"
is_started = False


@atexit.register
def quite():
    if is_started:
        enable_sites()
        session = Session(this_task, datetime.datetime.now().date(), sec)
        db.save_session(db.init_db(), session)
        print("you deep worked for %i secondes!" % sec)


def enable_sites():
    with open(host_path, 'r+') as file:
        content = file.readlines()
        file.seek(0)
        with open('{0}/bin/urls.csv'.format(app_path)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            websites = []
            for c in csv_reader:
                websites.append(c[0])
            for line in content:
                if not any(website in line for website in websites):
                    file.write(line)
            file.truncate()


def block_sites():
    with open(host_path, "r+") as fileptr:
        content = fileptr.read()
        with open('{0}/bin/urls.csv'.format(app_path)) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for website in csv_reader:
                if website[0] in content:
                    pass
                else:
                    fileptr.write(redirect + "    " + website[0] + "\n")


def timer():
    global sec
    while True:
        sys.stdout.write("\r%s" % str(datetime.timedelta(seconds=sec)))
        sys.stdout.flush()
        time.sleep(1)
        sec += 1


@click.group()
def cli():
    pass


@click.command()
@click.option('--url', prompt='Your url..', default="", help='site url')
def blockurl(url):
    print("hello %s" % url)
    with open('/snap/deepwork/x1/bin/urls.csv', 'a') as fd:
        fd.write(url + "\n")


@click.command()
@click.option('--url', prompt='Your url that you want to unblock it..', default="", help='site url')
def unblockurl(url):
    with open("urls.csv", "r") as f:
        lines = f.readlines()
    with open("urls.csv", "w") as f:
        for line in lines:
            if line.strip("\n") != url:
                f.write(line)


@click.command()
@click.option('--task', prompt='enter the task you will deep work on for next 25 min', default="No Task", help='site url')
def start(task):
    global this_task
    global is_started
    is_started = True
    this_task = task
    time.sleep(1)
    print("block out all possible distraction.")
    time.sleep(1)
    print("Deep Work, with all your might!")
    block_sites()
    time.sleep(1)
    timer()


@click.command()
def sessions():
    rows = db.select_all_sessions(db.init_db())
    table = [["id", "date", "task", "time"]]
    for r in rows:
        table.append([r[0], r[2], "No Task" if r[1] == "" else r[1], str(datetime.timedelta(seconds=r[3]))])
    print(tabulate(table, headers="firstrow",  tablefmt="fancy_grid"))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cli.add_command(start)
    cli.add_command(blockurl)
    cli.add_command(unblockurl)
    cli.add_command(sessions)
    cli()
