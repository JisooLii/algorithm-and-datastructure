#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the hourglassSum function below.
def hourglassSum(arr):
    hourglass_sum_set = []
    for first_idx, first_val in enumerate(arr):
        if first_idx + 2 >= len(arr):
            continue
        else:
            for second_idx, second_item in enumerate(first_val):
                if second_idx + 2 >= len(arr):
                    continue
                else:
                    r0e0 = arr[first_idx][second_idx]
                    r0e1 = arr[first_idx][second_idx + 1]
                    r0e2 = arr[first_idx][second_idx + 2]

                    r1e0 = arr[first_idx + 1][second_idx + 1]

                    r2e0 = arr[first_idx + 2][second_idx]
                    r2e1 = arr[first_idx + 2][second_idx + 1]
                    r2e2 = arr[first_idx + 2][second_idx + 2]

                    hourglass_sum_set.append(r0e0 + r0e1 + r0e2 + r1e0 + r2e0 + r2e1 + r2e2)

    sum_max = None;
    for sum_item in hourglass_sum_set:
        if sum_max is None:
            sum_max = sum_item
        elif sum_max < sum_item:
            sum_max = sum_item
    return sum_max


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
