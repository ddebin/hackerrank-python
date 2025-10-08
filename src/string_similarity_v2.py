#!/usr/bin/env python3

import sys
import os
from typing import IO


# cf. https://www.hackerrank.com/challenges/string-similarity/topics/z-function
def zFunction(s: str) -> list[int]:
    N = len(s)
    z = [0] * N
    m_l = m_r = 0
    for i in range(1, N):
        if i <= m_r:
            z[i] = min(m_r - i + 1, z[i - m_l])
        while i + z[i] < N and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > m_r:
            m_l = i
            m_r = i + z[i] - 1

    return z


def stringSimilarity(s: str) -> int:
    z = zFunction(s)
    return sum(z) + len(s)


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
