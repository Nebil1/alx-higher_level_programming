#!/usr/bin/python3
def fizzbuzz():
    for x in range(0,101):
        if x % 5 == 0 & x % 3 == 0:
            print(f"{x} ",end="")
        elif x % 3 == 0:
            print(f"{x} ",end="")
        elif x % 5 == 0:
            print(f"{x} ",end="")
        else:
            print(f"{x} ",end="")
