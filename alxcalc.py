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
        if isinstance(self.master, Task) is True:
            self.master.cal_task()

            return


class Main:
    def __init__(self, master=None):
        self.master = master
        self.args = sys.argv

        if len(self.args) <= 2:
            print("Usage: {} <option> <value>".format(self.args[0]))
            sys.exit()

        if self.args[1] != "-M" and self.args[1] != "-m":
            print("Error: Invalid option: {}".format(self.args[1]))
            sys.exit()

        if self.args[2].isdigit() is False:
            print("Error: Invalid input value for option {}: {}".
                  format(self.args[1], self.args[2]))
            sys.exit()

        self.filename = 'month_{}/month_{}'.format(self.args[2], self.args[2])

    def main(self):
        """Entry point.
        """

        try:
            os.stat(self.filename)
        except (FileNotFoundError, IsADirectoryError):
            print("DEBUGGER 4: File Not Found")
            sys.exit()

        if self.args[1] == "-M":
            subprocess.run(f'editor {self.filename}', shell=True, text=True)

        month = Month(self.filename, self.args)
        project = Project(self.filename, self.args)
        task = Task(self.filename, self.args)

        if len(self.args) == 7:
            self.master = task
        else:
            self.master = None

        calc = Calc(self.filename, self.args, self.master)


if __name__ == '__main__':
    Main().main()
