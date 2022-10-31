#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    am_pm = s[-2:]
    hour = (s[:2])
    new_time = str()
    if am_pm == "PM":
        hour = int(hour)+12
        if hour == 24:
            hour = 12
        new_time = str(hour)+s[2:-2]
    elif am_pm == "AM":
        if hour == "12":
            hour = "00"
        new_time = hour+s[2:-2]
    return new_time

if __name__ == '__main__':
    s="12:45:54PM"
    import pdb; pdb.set_trace()
    print(timeConversion(s))
