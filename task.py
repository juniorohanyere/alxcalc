#!/usr/bin/env python3

import sys

from project import Project


class Task(Project):
    def __init__(self, project, task, filename=None, args=None):
        super().__init__(filename, args)

        self.project = project
        self.task = task
        self.filename = filename

    def cal_task(self, strict=False):
        """Calculate the score for a given task.

        Args:
            task (str): Defines the task to calculate the score for.
                        This should be something like "task_0", "task_1", etc.
        """

        my_dict = self.to_dict()     # dictionary for learner's entry
        dictionary = self.from_json()     # predefined dictionary (full values)

        new_dict = {}

        score = 0
        deadline = int(my_dict[self.project][self.task]["deadline"])
        check = 0
        full_check = 0

        for key, value in dictionary[self.project][self.task]["mandatory"]. \
                items():
            if value == '' or int(value) < 0 or int(value) > 1:
                print()
                print("DEBUGGER 0: Corrupt JSON file.")
                sys.exit()

            new_dict.update([(key, value)])

        try:
            for key, value in dictionary[self.project][self.task]['optional'] \
                    .items():
                if value == '' or int(value) < 0 or int(value) > 1:
                    print()
                    print("DEBUGGER 1: Corrupt JSON file")
                    sys.exit()

                new_dict.update([(key, value)])
        except KeyError:
            pass

        i = 0
        for key, value in my_dict[self.project][self.task].items():
            if key == 'score':
                if value != '':
                    if value.endswith('%') is False:
                        print()
                        print("Error: Invalid Input Value")
                        sys.exit()
                    try:
                        score += int(value.rstrip('%'))
                        return (score)

                    except ValueError:
                        print()
                        print("Error: Invalid Input Value")
                        sys.exit()
                else:
                    # compute from checks
                    pass

            elif key == "deadline":
                if value == '':
                    if strict is True:
                        return "--"

                    return ""

                elif value.isdigit() is True:
                    deadline = int(value)
                else:
                    print()
                    print("Error: Invalid Input Value")
                    sys.exit()

            elif key.startswith('check_'):
                if value == '':
                    if strict is True:
                        return '--'

                    check += 0
                    full_check += 0
                else:
                    if (value.isdigit() is False or int(value) < 0 or
                            int(value) > 1):
                        print()
                        print("Error: Invalid Input Value")
                        sys.exit()
                    check += int(value) * int(new_dict[key])
                    full_check += int(new_dict[key])

            else:
                print()
                print("Error: Corrupt Input File")
                sys.exit()

        if deadline == 0:   # before end of first deadline (100%)
            task = (check / full_check) * 100
        elif deadline == 1:     # before end of second deadline (65%)
            task = (check / full_check) * 65
        elif deadline == 2:     # after second deadline (50%)
            task = (check / full_check) * 50
        else:
            print()
            print("Error: Invalid Input Value.")
            sys.exit()

        # ==> DEBUGGER
        # print(check)
        # print(full_check)
        # print(task)
        # <==

        return task

    def compare_checks(self, dict1, dict2):
        key1 = []
        key2 = []
        points = []

        if dict1 is None or dict2 is None or dict1 == {} or dict2 == {}:
            return None

        for key, value in dict1.items():
            key1 += key
            points += value

        for key, value in dict2.items():
            key2 += key

        if key1 == key2:
            return points

        return None
