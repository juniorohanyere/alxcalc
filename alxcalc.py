#!/usr/bin/env python3
"""Main module for the alxcalc program.
"""

import sys
import os
import subprocess

from calc import Month, Project, Task, Calc


def main():
    """Entry point.
    """

    if len(sys.argv) <= 2:
        print("Usage: {} <option> <value>".format(sys.argv[0]))
        sys.exit()

    if sys.argv[1] != "-M" and sys.argv[1] != "-m":
        print("Error: Invalid option: {}".format(sys.argv[1]))
        sys.exit()

    if sys.argv[2].isdigit() is False:
        print("Error: Invalid input value for option {}: {}".
              format(sys.argv[1], sys.argv[2]))
        sys.exit()

    filename = 'month_{}/month_{}'.format(sys.argv[2], sys.argv[2])

    try:
        os.stat(filename)
    except (FileNotFoundError, IsADirectoryError):
        print("DEBUGGER 4: File Not Found")
        sys.exit()

    if sys.argv[1] == "-M":
        subprocess.run(f'editor {filename}', shell=True, text=True)

    month = Month(filename=filename, args=sys.argv)
    project = Project(filename=filename, args=sys.argv)
    task = Task(filename, args=sys.argv)
    calc = Calc(filename, args=sys.argv)


if __name__ == '__main__':
    main()
