#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    summ = sum(s[:m])
    low = 0
    high = m
    count = 0

    for i in range(m-1, len(s)):
        if summ == d:
            count += 1
        if high<len(s):
            summ = summ - s[low] + s[high]
            low += 1
            high += 1
    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
