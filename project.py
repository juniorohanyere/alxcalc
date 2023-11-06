#!/usr/bin/env python3

import sys

from month import Month


class Project(Month):
    def __init__(self, month, project, filename=None, args=None):
        super().__init__(filename, args)

        self.month = month
        self.project = project
        self.filename = filename

    """this method should probably be part of the Main class
    def project_key(self):
        dictionary = self.from_json()

        for key, value in dictionary.items():
            if value['name'] == self.args[4]:
                return key

        print("Error: unrecognized project: {}".format(self.args[4]))
        print("       in month {}".format(self.month))
        sys.exit()
    """

    def cal_project(self):
        dictionary = self.to_dict()
        score = 0
        count = 0

        for key, value in dictionary[self.project].items():
            if key == 'score':
                if value != '':
                    if value.endswith('%') is False:
                        print()
                        print("Error: invalid input value")
                        sys.exit()
                    try:
                        score += int(value.rstrip('%'))
                        return score

                    except ValueError:
                        print()
                        print("Error: invalid input value")
                        sys.exit()

                else:
                    # compute from tasks
                    pass

            elif key.startswith('task_'):
                from task import Task

                task = Task(self.project, key, self.filename, self.args)
                my_task = task.cal_task()
                if my_task == '--':
                    return '--'

                score += my_task
                count += 1

        my_score = score / count
