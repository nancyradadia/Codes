#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    # initialize the dictionaries
        r2 = {}
        r3 = {}
        count = 0

        # loop throgh the arr itens
        for k in arr:
                # print(k)
                # if k in r3 indicates the triplet already completed,
                # the count need be incremented
                if k in r3:
                        print("Third",k)
                        count += r3[k]

                # if k in r2, it is the secound number of the triplet,
                # your successor (third element k*r) need be added or incremented in the r3 dict
                # because is a potencial triplet 
                if k in r2:
                        print("Second:",k)
                        if k*r in r3:
                                r3[k*r] += r2[k]
                        else:
                                r3[k*r] = r2[k]

                # else, k is the first element of the triplet, so,
                # your seccessor (secound element k*r) need be added or incremented in the r2 dict
                # because is a potencial triplet
                if k*r in r2:
                        print(k)
                        r2[k*r] += 1
                else:
                        r2[k*r] = 1

        return count

if __name__ == '__main__':
    

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    print(ans)
