#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    a.sort()
    while len(a)>0:
        if len(a) == 1:
            return(a[0])
        if a[0] == a[1]:
            a.pop(0)
            a.pop(0)
        else:
            return(a[0])


print(lonelyinteger([34,95,34,64,45,95,16,80,80,75,3,25,75,25,31,3,64,16,31]))
