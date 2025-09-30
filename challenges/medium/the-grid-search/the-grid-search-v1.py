#!/usr/bin/env python3

import sys
import os

#
# Complete the 'gridSearch' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY G
#  2. STRING_ARRAY P
#

def gridSearch(G: list[str], P: list[str]) -> str:
    """
    Returns a string("YES", "NO") if pattern P has been found in G.

    Arguments:
    G – the grid to search
    P – the pattern to search for
    """
    p = P[0]
    for i in range(len(G) - len(P) + 1):
        start = 0
        while True:
            start = G[i].find(p, start)
            if start == -1:
                break
            found = True
            for j in range(1, len(P)):
                if G[i + j][start : start + len(p)] != P[j]:
                    found = False
                    break
            if found:
                return 'YES'
            start += 1
    return 'NO'

if __name__ == '__main__':
    if "FOO" in os.environ:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
    else:
        fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])
        C = int(first_multiple_input[1])

        G = []
        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])
        c = int(second_multiple_input[1])

        P = []
        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
