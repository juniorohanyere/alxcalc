#!/usr/bin/env python3
"""Main module for the alxcalc program.
"""

import sys
import os
import subprocess

from task import Task
from project import Project
from month import Month


class Calc:
    def __init__(self, filename, args, master=None):
        self.filename = filename
        self.args = args
        self.master = master
        self.calc()

    def calc(self):
        elif isinstance(self.master, Month) is True:
            print(str(self.master.cal_month()) + "%")
        elif isinstance(self.master, Project) is True:
            print(str(self.master.cal_project()) + "%")
        if isinstance(self.master, Task) is True:
            print(str(self.master.cal_task()) + "%")

            return


class Main:
    def __init__(self, master=None):
        self.master = master
        self.args = sys.argv
        length = len(self.args)

        if length <= 2:
            print("Usage: alxcalc <option> <value>")
            sys.exit()

        if self.args[1] == "-M" or self.args[1] == "-m" :
            if self.args[2].isdigit() is False:
                print("Error: Invalid input value for option {}: {}".
                      format(self.args[1], self.args[2]))
                print("       Expecting <int>, got <str>")
                sys.exit()

            home = os.environ['HOME']
            self.filename = '{}/.alxcalc/month_{}/month_{}'.format(home,
                                                                   self.args[2],
                                                                   self.args[2])

            try:
                os.stat(self.filename)
            except (FileNotFoundError, IsADirectoryError):
                print("Error: No such month in the ALX calendar: {}".
                      format(self.args[2]))
                sys.exit()

            subprocess.run(f'editor {self.filename}', shell=True, text=True)

    def main(self):
        """Entry point.
        """

        length = len(self.args)

        if length == 3:
            month = Month(self.filename, self.args)
            self.master = month
        elif length == 5:
            if self.args[3] == '-p':
                project = Project(self.filename, self.args)
                self.master = project
        elif length == 7 and self.args[5] == '-t':
            if self.args[6].isdigit() is False:
                print("Error: Invalid Input Value for {}: {}".
                      format(self.args[5], self.args[6]))
                sys.exit()
            if self.args[3] != '-p':
                print()
                print("Error: Invalid Syntax")
                sys.exit()
            if self.args[1] != '-m' and self.args[1] != '-M':
                print()
                print("Error: Invalid Syntax.")
                sys.exit()
            if self.args[2].isdigit() is False:
                print()
                print("Error: Invalid Input Value")
                sys.exit()

            month = "month_" + self.args[2]

            project = Project(self.filename, self.args)
            project = project.project_key()

            task = "task_" + self.args[6]

            filename = self.filename

            my_task = Task(project, task, filename, self.args)
            self.master = my_task

        else:
            self.master = None

        calc = Calc(self.filename, self.args, self.master)


if __name__ == '__main__':
    Main().main()
