#!/bin/python3

import math
import os
import random
import re
import sys

input1 = ['5 3 4', '1 5 8', '6 4 2']
input2 = ['4 9 2', '3 5 7', '8 1 5']
input3 = ['4 8 2', '4 5 7', '6 1 6']

# Complete the formingMagicSquare function below.
def formingMagicSquare(s):
  convertS = convertToIntArr(s)

  print(normal)
  print(malformed)

# convert Str array To Int array
def convertToIntArr(s):
  convertedS = []
  for row in s:
    convertedS.append(list(map(lambda x: int(x), row.split(' '))))
  return convertedS


if __name__ == '__main__':
  formingMagicSquare(input1)
