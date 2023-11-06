#!/usr/bin/env python3

import sys

from month import Month


class Project(Month):
    def __init__(self, filename=None, args=None):
        if (len(args) >= 5 and args[3] == '-p' and len(args) <= 7 and
                len(args) % 2 != 0):
            super().__init__(filename, args)
            self.project = self.project_key()

    """
        mand_pnt = 0    # obtained mandatory points
        opt_pnt = 0     # obtained optional points
        pnt = 0     # total obtained points

        total_mand_pnt = 0  # full mandatory points
        total_opt_pnt = 0   # full optional points
        total_pnt = 0   # total full points

        for key, value in dictionary[project][task][mandatory].items():
            total_mand_pnt += int(value)

        try:
            for key, value in dictionary[project][task][optional].items():
                total_opt_pnt += int(value)
        except KeyError:
            total_opt_pnt = 0

        total_pnt = total_mand_pnt + total_opt_pnt
    """

    def project_key(self):
        dictionary = self.from_json()

        for key, value in dictionary.items():
            if value['name'] == self.args[4]:
                return key

        print("Error: No such project for month {}: {}".
              format(self.month.lstrip('month_'), self.args[4]))
        sys.exit()

    def cal_project(self):
        pass
