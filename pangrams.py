#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    s = s.lower()
    if len(s) < 26:
        return 'not pangram'
    else:
        for i in alphabet:
            if i not in s:
                return 'not pangram'
        return 'pangram'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)
    print(result)

    # fptr.write(result + '\n')

    # fptr.close()
