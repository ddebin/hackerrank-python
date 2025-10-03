#!/usr/bin/env python3

import os
import sys
import itertools
from typing import IO


def ashtonString(s: str, k: int) -> str:
    N = len(s)

    # suffixRank is table hold the rank of each string
    suffixRank = [0] * N

    # Example "abaab"
    # Suffix Array for this (2, 3, 0, 4, 1)
    # Create a tuple to store rank for each suffix

    # struct myTuple {
    #   int originalIndex;   // stores original index of suffix
    #   int firstHalf;       // store rank for first half of suffix
    #   int secondHalf;      // store rank for second half of suffix
    # };
    L = [[0] * 3 for _ in range(N)]

    # Initialize suffix ranking on the basis of only single character
    # for single character ranks will be 'a' = 0, 'b' = 1, 'c' = 2 ... 'z' = 25
    for j in range(N):
        suffixRank[j] = ord(s[j]) - ord("a")

    # Iterate log(n) times i.e. till when all the suffixes are sorted
    # 'stp' keeps the track of number of iteration
    # 'cnt' store length of suffix which is going to be compared
    #
    # On each iteration we initialize tuple for each suffix array
    # with values computed from previous iteration

    cnt = 1
    stp = 1
    while cnt < N:

        for i in range(N):
            L[i][0] = i
            L[i][1] = suffixRank[i]
            L[i][2] = suffixRank[i + cnt] if (i + cnt) < N else -1

        # On the basis of tuples obtained sort the tuple array
        # L.sort(key = cmp_to_key(lambda a, b: a[2] - b[2] if a[1] == b[1] else a[1] - b[1]))
        L.sort(key=lambda a: a[1] * 2**24 + a[2])  # faster than using `cmp_to_key`

        # Initialize rank for rank 0 suffix after sorting to its original index
        # in suffixRank array
        suffixRank[L[0][0]] = 0

        currRank = 0
        for i in range(1, N):
            # compare ith ranked suffix (after sorting) to (i - 1)th ranked suffix
            # if they are equal till now assign same rank to ith as that of (i - 1)th
            # else rank for ith will be currRank (i.e. rank of (i - 1)th) plus 1,
            # i.e (currRank + 1)
            if L[i - 1][1] != L[i][1] or L[i - 1][2] != L[i][2]:
                currRank += 1

            suffixRank[L[i][0]] = currRank

        cnt *= 2
        stp += 1

    # loop all ordered substrings
    seen = set()
    length = 0
    for i in range(N):
        index = L[i][0]
        for c in itertools.accumulate(itertools.islice(s, index, N)):
            # more memory efficient to store hash of strings seen, instead of strings
            hash_c = hash(c)
            if hash_c in seen:  # check if unique
                continue
            seen.add(hash_c)
            length += len(c)
            if length >= k:
                return c[k - length - 1]

    raise NotImplementedError("should not happen")


def main(fptr: IO) -> None:
    t = int(input().strip())
    for _ in range(t):
        s = input()
        k = int(input().strip())
        res = ashtonString(s, k)
        fptr.write(str(res) + "\n")


if __name__ == "__main__":
    if "OUTPUT_PATH" in os.environ:
        fptr = open(os.environ["OUTPUT_PATH"], "wt")
    else:
        fptr = sys.stdout

    main(fptr)

    fptr.close()
