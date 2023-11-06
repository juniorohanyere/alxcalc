#!/usr/bin/env python3
'''Handles the code base for month 0 of the alx programme.
'''

import sys
from base import Base


class Month(Base):
    """Defines methods to handle computation and calculation of score for a
    given month. This is the base class
    """

    def __init__(self, filename=None, args=None):
        """Initializer.
        """

        super().__init__(filename, args)

        self.month = "month_" + self.args[2]

    def cal_month(self):
        """calculate and compute the sccore for a given month
        """

        dictionary = self.to_dict()
        score = 0
        t_score = 0
        t_count = 0

        for key, value in dictionary.items():
            for k, v in value.items():
                if k == 'score':
                    if v != '':
                        if v.endswith('%') is False:
                            print()
                            print("Error: Invalid Input Value.")
                            sys.exit()
                        try:
                            score += int(v.rstrip('%'))
                            break
                        except ValueError:
                            print()
                            print("Error: Invalid Input Value.")
                            sys.exit()
                    else:
                        # compute from task
                        pass

                elif k.startswith('task_'):
                    from task import Task

                    t_count += 1
                    task = Task(key, k, self.filename, self.args)
                    my_task = task.cal_task()
                    if my_task != '--':
                        score += my_task
                        break

        m_score = score / 2
        return (m_score)
