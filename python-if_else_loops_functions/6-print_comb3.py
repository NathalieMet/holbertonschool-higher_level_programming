#!/usr/bin/python3
for int in range(0, 10):
    for digit in range(1, 10):
        if int < 8:
            if int != digit and int < digit:
                print("{}{}".format(int, digit), end=", ")
        else:
            if int != digit and int < digit:
                print("{}{}".format(int, digit))
