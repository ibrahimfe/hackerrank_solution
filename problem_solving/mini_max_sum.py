#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    maksimum, minimum = [], []
    for i in range(4):
        maksimum.append(max(arr))
        arr.remove(max(arr))
        
    arr += maksimum
    for j in range(4):
        minimum.append(min(arr))
        arr.remove(min(arr))
    print(f"{sum(minimum)} {sum(maksimum)} ")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
