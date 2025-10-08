#!/usr/bin/env python3

import sys
import os
from typing import IO
from operator import itemgetter


def buildSuffixArray(s: str) -> list[int]:
    global dur_1, dur_2, dur_3
    """Build SuffixArray from string in O(N*log(N)^2)"""

    N = len(s)

    # Example "abaab"
    # Suffix Array for this (2, 3, 0, 4, 1)
    # Create a tuple to store rank for each suffix

    # struct myTuple {
    #   originalIndex // stores original index of suffix
    #   firstHalf * 2**24 + secondHalf // store rank for firstand second half of suffix
    # }
    L = [(0, 0) for _ in range(N)]

    # suffixRank is table hold the rank of each string
    # Initialize suffix ranking on the basis of only single character
    # for single character ranks will be 'a' = 0, 'b' = 1, 'c' = 2 ... 'z' = 25
    suffixRank = [ord(s[i]) - ord("a") for i in range(N)]

    # Iterate log(n) times i.e. till when all the suffixes are sorted
    # 'stp' keeps the track of number of iteration
    # 'cnt' store length of suffix which is going to be compared
    #
    # On each iteration we initialize tuple for each suffix array
    # with values computed from previous iteration

    cnt = 1
    stp = 1
    while cnt < N:
        L = [
            (i, suffixRank[i] * 2**24 + (suffixRank[i + cnt] if i + cnt < N else -1))
            for i in range(N)
        ]

        # On the basis of tuples obtained sort the tuple array
        # L.sort(key = cmp_to_key(lambda a, b: a[2] - b[2] if a[1] == b[1] else a[1] - b[1]))
        L.sort(key=itemgetter(1))  # faster than using `cmp_to_key`

        # Initialize rank for rank 0 suffix after sorting to its original index
        # in suffixRank array
        suffixRank[L[0][0]] = 0

        currRank = 0
        for i in range(1, N):
            # compare ith ranked suffix (after sorting) to (i - 1)th ranked suffix
            # if they are equal till now assign same rank to ith as that of (i - 1)th
            # else rank for ith will be currRank (i.e. rank of (i - 1)th) plus 1,
            # i.e (currRank + 1)
            if L[i - 1][1] != L[i][1]:
                currRank += 1

            suffixRank[L[i][0]] = currRank

        cnt *= 2
        stp += 1

    return [ll[0] for ll in L]


def kasaiLCP(s: str, sa: list[int]) -> list[int]:
    """Build LCP (Longest Common Prefix between two consecutive entries in SA) from SuffixArray, Kasai's algo in O(N)"""

    N = len(s)
    lcp = [0] * N
    rank = [0] * N

    for i in range(N):
        rank[sa[i]] = i

    k = 0
    for i in range(N):
        if rank[i] == N - 1:
            k = 0
            continue
        j = sa[rank[i] + 1]
        while i + k < N and j + k < N and s[i + k] == s[j + k]:
            k += 1
        lcp[rank[i]] = k
        k = max(k - 1, 0)

    return lcp


def stringSimilarity(s: str) -> int:
    sa = buildSuffixArray(s)
    fullstring_index = sa.index(0)
    lcp = kasaiLCP(s, sa)
    sum = 0
    previous = 2**31
    # [0:fullstring_index]
    if fullstring_index > 0:
        for i in range(fullstring_index - 1, -1, -1):
            if lcp[i] == 0:
                break
            next = min(lcp[i], previous)
            sum += next
            previous = next
    # fullstring_index
    sum += len(s)
    previous = 2**31
    # [fullstring_index:len(sa)]
    if fullstring_index < len(sa) - 1:
        for i in range(fullstring_index, len(sa)):
            if lcp[i] == 0:
                break
            next = min(lcp[i], previous)
            sum += next
            previous = next
    return sum


def main(fptr: IO) -> None:
    t = int(input().strip())
    for _ in range(t):
        s = input()
        result = stringSimilarity(s)
        fptr.write(str(result) + "\n")


if __name__ == "__main__":
    if "OUTPUT_PATH" in os.environ:
        with open(os.environ["OUTPUT_PATH"], "wt") as fptr:
            main(fptr)
            fptr.close()
    else:
        main(sys.stdout)
