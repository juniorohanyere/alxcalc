#!/usr/bin/env python3
"""Main module for the alxcalc program.
"""

import sys
import os
import subprocess

from calc import Parser


def main():
    """Entry point.
    """

    if len(sys.argv) <= 2:
        print("Usage: {} <option> <value>".format(sys.argv[0]))
        sys.exit()

    filename = 'month_{}/month_{}'.format(sys.argv[2], sys.argv[2])

    try:
        os.stat(filename)
    except (FileNotFoundError, IsADirectoryError):
        print("DEBUGGER 4: File Not Found")
        sys.exit()

    subprocess.run(f'editor {filename}', shell=True, text=True)

    m0 = Parser(filename=filename, args=sys.argv)


if __name__ == '__main__':
    main()
