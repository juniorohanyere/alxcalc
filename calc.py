#!/usr/bin/env python3
'''Handles the code base for month 0 of the alx programme.
'''

import sys


class Calc:
    """Defines methods to handle computation and calculation of score for month
    0.
    """

    def __init__(self, master=None, args=None):
        """Initializer.
        """

        self.master = master
        self.args = args
        self.main()

    def main(self):
        """Main method for Month_0 class.
        """

        print(self.to_dict())

    def to_dict(self):
        """Translates the content read from a particular file to a python
        dictionary for fine access.
        """

        dictionary = {}

        if self.args[1] == "-M":
            if self.args[2] == "0":
                try:
                    with open("month_0/month_0", "r") as file:
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
                        m += [n]
                        n = []
                    else:
                        n += [line.strip()]
                m += [n]

                # the aim now is to generate a fine dictionary to access the
                # data
                dictionary = {}
                for i in range(1, len(m)):
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
                                    if isinstance(value, str) == False:
                                        value.update([(t_key, t_value)])
                                    dictionary.update([(key, value)])
                            elif tmp.startswith("deadline"):
                                deadline = tmp.split("==")
                                d_key = deadline[0]     # deadline key
                                d_value = deadline[1]   # deadline value
                                if isinstance(t_value, str) == False:
                                    t_value.update([(d_key, d_value)])
                                if isinstance(value, str) == False:
                                    value.update([(t_key, t_value)])
                                dictionary.update([(key, value)])
                            elif tmp.startswith("check_"):
                                check = tmp.split("==")
                                c_key = check[0]    # check key
                                c_value = check[1]  # check value
                                if isinstance(t_value, str) == False:
                                    t_value.update([(c_key, c_value)])
                                if isinstance(value, str) == False:
                                    value.update([(t_key, t_value)])
                                dictionary.update([(key, value)])
                            else:
                                print()
                                print("DEBUGGER 0")
                    else:
                        value = project[1]
                        dictionary.update([(key, value)])

                return (dictionary)

    def cal_task(self, task):
        """Calculate the score for a given task.

        Args:
            task (str): Defines the task to calculate the score for.
                        This should be something like "task_0", "task_1", etc.
        """

        dictionary = self.to_dict()

        for key, value in dictionary.items():
            if isinstance(value, dict) == True:
                # check for NULL values
                t_dict = value
                for t_key, t_value in t_dict.items():
                    if t_key == task and isinstance(t_value, dict) == True:
                        c_dict = t_value
                        for c_key, c_value in c_dict.items():
                            if c_value == '':
                                print()
                                print("DEBUGGER 1")
                                sys.exit()

                # get the values after successful NULL value checkup
                c_list = list(c_dict)
                for i in range(len(c_list)):
                    if i == 0:
                        deadline = int(c_list[i])
                    else:
                        check = int(c_list[i]) # and some crazy calculations :)
                        cal += cal + check

                if (int(deadline) <= 0 or int(deadline) > 3 or int(check_0) < 0
                        or int(check_0) > 1 or int(check_1) < 0 or
                        int(check_1) > 1 or int(check_2) < 0 or
                        int(check_2) > 1):
                    print()
                    print("DEBUGGER 3")
                    sys.exit()
