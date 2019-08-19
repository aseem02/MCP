#!/bin/python

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    output = [' ']*n
    for i in range(n-1, -1 , -1):
        output[i] = '#'
        print ''.join(output)

if __name__ == '__main__':
    n = int(raw_input())

    staircase(n)
