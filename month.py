#!/usr/bin/env python3
'''Handles the code base for month 0 of the alx programme.
'''

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

        # if len(self.args) == 3 and self.args[1] == "-m":
        #    self.cal_month()

    def cal_month(self):
        """calculate and compute the sccore for a given month
        """

        print(self.to_dict())
