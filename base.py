#!/usr/bin/env python3
'''Handles the code base for month 0 of the alx programme.
'''

import sys
import json


class Base:
    """Defines methods to handle computation and calculation of score for a
    given month. This is the base class
    """

    def __init__(self, filename=None, args=None):
        """Initializer.
        """

        self.filename = filename
        self.args = args

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

    def from_json(self):
        filename = self.filename + '.json'

        try:
            with open(filename, 'r') as file:
                rfile = file.read()
        except (FileNotFoundError, IsADirectoryError):
            print("DEBUGGER 5: file not found")
            sys.exit()

        dictionary = json.loads(rfile)

        return dictionary
