#!/bin/python3

import math
import os
import random
import re
import sys

def rotateleft(a,d) :
    return a[d:] + a[:d]


if __name__ == '__main__':
    nd = input().split()
    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))
    result=rotateleft(a,d)
    res=str(result)[1:-1]
    print(res.replace(",",""))
