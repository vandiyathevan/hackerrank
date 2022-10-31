#!/bin/python3

import math
import os
import random
import re
import sys

import logging
from dayone import DayOne

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.


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


class TestLonelyInteger(DayOne):

    def test_lonely_integer_1(self):
        logging.warning("running test1")
        assert (lonelyinteger([34,95,34,64,45,95,16,80,80,75,3,25,75,25,31,3,64,16,31]) == 45)
        logging.warning("test1 completed")


    def test_lonely_integer_2(self):
        logging.warning("running test2")
        assert (lonelyinteger([1,1,2,2,3,4,5,5,3]) == 3)
        logging.warning("test2 completed")
