#!/usr/bin/env python3

import sys

from project import Project


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

    def cal_task(self):
        """Calculate the score for a given task.

        Args:
            task (str): Defines the task to calculate the score for.
                        This should be something like "task_0", "task_1", etc.
        """

        my_dict = self.to_dict()     # dictionary for learner's entry

        dictionary = self.from_json()     # predefined dictionary (full values)

        deadline = int(my_dict[self.project][self.task]["deadline"])
        check = 0
        full_check = 0
        points = []

        for key, value in dictionary[self.project][self.task]["mandatory"]. \
                items():
            if value == '' or int(value) < 0 or int(value) > 1:
                print()
                print("DEBUGGER 0: Corrupt JSON file.")
                sys.exit()

            full_check += int(value)
            points += value

        i = 0
        for key, value in my_dict[self.project][self.task].items():
            if key == "deadline" or key == "score":
                pass
            else:
                if value == '':
                    # ==> DEBUGGER
                    print("--")
                    # <==

                    return "--"

                if int(value) < 0 or int(value) > 1:
                    print()
                    print("DEBUGGER 6: Invalid Value.")
                    sys.exit()

                check += int(value) * int(points[i])
                i += 1

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
