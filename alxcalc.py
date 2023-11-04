#!/usr/bin/env python3

import sys
import subprocess

from month_0 import month_0


def main():
    subprocess.run('editor month_0/month_0', shell=True, text=True)
    m0 = month_0.Month_0(args=sys.argv)
    m0.main()


if __name__ == '__main__':
    main()
