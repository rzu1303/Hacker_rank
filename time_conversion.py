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
    # Write your code here
    d = int(s[:2])
    if s.find('PM') == -1:
        s = s.replace('AM', '')
        if d == 12:
            s = s.replace('12', '00', 1)


    else:
        s = s.replace('PM', '')
        if d != 12:
            d  = d + 12
            d = str(d)
            s = s.replace(s[:2], d)
    
    return s



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)
    print(s)

    # fptr.write(result + '\n')

    # fptr.close()
