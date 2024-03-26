#!/bin/python3

import math
import os
import random
import re
import sys

def plusMinus(arr):
    c = 0
    zero = 0
    positive = 0
    negative = 0
    total_positive = 0
    total_negative = 0
    total_zero = 0
    i = 0
    for i in range(n):
        if arr[i] == 0:
            zero += 1
        elif arr[i] > 0:
            positive += 1
        else:
            negative += 1

    if positive != 0:
        total_positive = positive/n
    print('%.6f' % total_positive) 

    if negative != 0:
        total_negative = negative/n
    print('%.6f' % total_negative)

    if zero != 0:
        total_zero = zero/n
    print('%.6f' % total_zero)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

