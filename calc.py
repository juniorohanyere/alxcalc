#!/usr/bin/env python3
'''Handles the code base for month 0 of the alx programme.
'''

import sys
import json


class Month:
    """Defines methods to handle computation and calculation of score for a
    given month. This is the base class
    """

    def __init__(self, filename=None, args=None):
        """Initializer.
        """

        self.filename = filename
        self.args = args

        self.month = "month_" + self.args[2]

        # if len(self.args) == 3 and self.args[1] == "-m":
        #    self.cal_month()

    def to_dict(self):
        """Translates the content read from a particular file to a python
        dictionary for fine access.
        """

        dictionary = {}

        try:
            with open(self.filename, "r") as file:
                lines = file.readlines()

        except (FileNotFoundError, IsADirectoryError):
            print("File Not Found")
            sys.exit()

        m = []
        n = []
        for line in lines:
            # split up the project into lines
            # getting rid of lines beginning with '#' as comments
            if line.startswith("#"):
                pass
            elif line == "\n":
                if n != []:
                    m += [n]
                n = []
            else:
                n += [line.strip()]
        m += [n]

        # the aim now is to generate a fine dictionary to access the
        # data
        dictionary = {}
        for i in range(len(m)):
            project = m[i][0].split("==")
            key = project[0]    # project key
            if project[1] == '':
                value = {}  # project value
                for j in range(1, len(m[i])):
                    tmp = m[i][j]
                    if tmp.startswith("task_"):
                        task = tmp.split("==")
                        t_key = task[0]     # task key
                        if task[1] == '':
                            t_value = {}    # task value
                        else:
                            t_value = task[1]
                            if isinstance(value, str) is False:
                                value.update([(t_key, t_value)])
                            dictionary.update([(key, value)])
                    elif tmp.startswith("deadline"):
                        deadline = tmp.split("==")
                        d_key = deadline[0]     # deadline key
                        d_value = deadline[1]   # deadline value
                        if isinstance(t_value, str) is False:
                            t_value.update([(d_key, d_value)])
                        if isinstance(value, str) is False:
                            value.update([(t_key, t_value)])
                        dictionary.update([(key, value)])
                    elif tmp.startswith("check_"):
                        check = tmp.split("==")
                        c_key = check[0]    # check key
                        c_value = check[1]  # check value
                        if isinstance(t_value, str) is False:
                            t_value.update([(c_key, c_value)])
                        if isinstance(value, str) is False:
                            value.update([(t_key, t_value)])
                        dictionary.update([(key, value)])
                    else:
                        print()
                        print("DEBUGGER 0")
            else:
                value = project[1]
                dictionary.update([(key, value)])

        return (dictionary)

    def json_to_dict(self):
        filename = self.filename + '.json'

        try:
            with open(filename, 'r') as file:
                rfile = file.read()
        except (FileNotFoundError, IsADirectoryError):
            print("DEBUGGER 5: file not found")
            sys.exit()

        dictionary = json.loads(rfile)

        return dictionary


class Project(Month):
    def __init__(self, filename=None, args=None):
        if len(args) >= 5 and args[3] == '-p':
            super().__init__(filename, args)
            self.project = self.project_id()

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

    def project_id(self):
        dictionary = self.json_to_dict()

        for key, value in dictionary.items():
            for k, v in value.items():
                if k == 'name' and v == self.args[4]:
                    # ==> DEBUGGER
                    print(key)
                    # <==

                    return key

        print("Error: No such project for month {}: {}".
              format(self.month, self.args[4]))


class Task(Project):
    def __init__(self, filename=None, args=None):
        if len(args) == 7 and args[5] == '-t':
            super().__init__(filename, args)

            self.args = args

            if self.args[5] == "-t":
                if self.args[6].isdigit() is False:
                    print("Error: Invalid input value for {}: {}".
                          format(self.args[5], self.args[6]))
                    sys.exit()

                self.task = "task_" + self.args[6]

class Calc(Task):
    def __init__(self, filename=None, args=None):
        super().__init__(filename, args)
        self.cal_task()

    def cal_task(self):
        """Calculate the score for a given task.

        Args:
            task (str): Defines the task to calculate the score for.
                        This should be something like "task_0", "task_1", etc.
        """

        my_dict = self.to_dict()     # dictionary for learner's entry
        dictionary = self.json_to_dict()     # predefined dictionary (full values)

        deadline = int(my_dict[self.project][self.task]["deadline"])
        check = 0
        full_check = 0

        for key, value in my_dict[self.project][self.task].items():
            if key == "deadline":
                pass
            else:
                if value == '' or int(value) < 0 or int(value) > 1:
                    print()
                    print("DEBUGGER 6: Empty Value.")
                    sys.exit()
                check += int(value)

        length = len(dictionary[self.project][self.task]["mandatory"].items())
        full_check = length

        try:
            length = len(dictionary[self.project][self.task]['optional'].
                        items())
            full_check += length
        except KeyError:
            pass

        if deadline == 0:   # before end of first deadline (100%)
            task = (check / full_check) * 100
        elif deadline == 1:     # before end of second deadline (65%)
            task = (check / full_check) * 65
        elif deadline == 2:     # after second deadline (50%)
            task = (check / full_check) * 50

        # ==> DEBUGGER
        print(check)
        print(full_check)
        print(task)
        # <==

        return task

    def cal_project(self):
        pass

    def cal_month(self):
        """calculate and compute the sccore for a given month
        """

        print(self.to_dict())

