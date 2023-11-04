#!/usr/bin/env python3
"""Main module for the alxcalc program.
"""

import sys
import subprocess

from month_0 import month_0


def main():
    """Entry point.
    """

    if len(sys.argv) <= 2:
        print("Usage: {} <option> <value>".format(sys.argv[0]))
        sys.exit()

    subprocess.run('editor month_0/month_0', shell=True, text=True)

    m0 = month_0.Month_0(args=sys.argv)


if __name__ == '__main__':
    main()
