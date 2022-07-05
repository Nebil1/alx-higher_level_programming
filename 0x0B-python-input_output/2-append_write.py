#!/usr/bin/python3
'''
file: 4-append_write.py
functions:
-> append_write
'''


def append_write(filename="", text=""):
    ''' appends a string at the end of a text file '''

    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
