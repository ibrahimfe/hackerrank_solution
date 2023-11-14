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
    # Extracting hours, minutes, and seconds
    h, m, s_period = map(int, s[:-2].split(':'))
    period = s[-2:]

    # Convert to 24-hour format
    if period == 'PM' and h != 12:
        h += 12
    elif period == 'AM' and h == 12:
        h = 0

    # Formatting the result
    result = '{:02d}:{:02d}:{:02d}'.format(h, m, s_period)

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
