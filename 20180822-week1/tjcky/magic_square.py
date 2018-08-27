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

  normal, malformed = [], []
  
  rn, rm = verifyRow(convertS)
  cn, cm = verifyCol(convertS)
  dn, dm = verifyDiagonal(convertS)
  normal += (rn + cn + dn)
  malformed += (rm + cm + dm)

  print(normal)
  print(malformed)

# convert Str array To Int array
def convertToIntArr(s):
  convertedS = []
  for row in s:
    convertedS.append(list(map(lambda x: int(x), row.split(' '))))
  return convertedS

# verify sum(row) is 15
def verifyRow(s):
  normal, malformed = [], []
  for rowIdx, row in enumerate(s):
    isValid = (s[rowIdx][0] + s[rowIdx][1] + s[rowIdx][2] == 15)
    rowName = str(rowIdx) + '0' + str(rowIdx) + '1' + str(rowIdx) + '2'

    if isValid:
      normal.append(rowName)
    else:
      malformed.append(rowName)
  return normal, malformed

# verify sum(col) is 15
def verifyCol(s):
  normal, malformed = [], []
  for n in range(0, 3):
    isValid = (s[0][n] + s[1][n] + s[2][n] == 15)
    colName = '0' + str(n) + '1' + str(n) + '2' + str(n)
    
    if isValid:
      normal.append(colName)
    else:
      malformed.append(colName)

  return normal, malformed

# verify sum(diagonal) is 15
def verifyDiagonal(s):
  normal, malformed = [], []

  if s[0][0] + s[1][1] + s[2][2] == 15:
    normal.append('001122')
  else:
    malformed.append('001122')
  
  if s[0][2] + s[1][1] + s[2][0] == 15:
    normal.append('021120')
  else:
    malformed.append('001122')

  return normal, malformed


if __name__ == '__main__':
  formingMagicSquare(input1)
