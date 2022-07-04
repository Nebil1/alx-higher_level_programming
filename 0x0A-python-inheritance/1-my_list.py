#!/usr/bin/python3
"""
file: 1-mi_list.py
Class:
-> MyList
"""


class MyList(list):
    """ class MyList that inherits from list """

    def print_sorted(self):
        """ prints the list, but sorted """
        print(sorted(self))
