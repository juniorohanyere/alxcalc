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

        self.month = self.args[2]

    def cal_month(self):
        """calculate and compute the sccore for a given month
        """

        dictionary = self.to_dict()
        score = 0
        t_score = 0
        t_count = 0

        for key, value in dictionary.items():
            from project import Project

            project = Project(self.month, key, self.filename, self.args)
            my_project = project.cal_project()
            if my_project == '--':
                return '--'

            score += my_project * weight    # weight of the project

        m_score = score / total_weight # total_weight

        return (m_score)
