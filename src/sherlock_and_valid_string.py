#!/usr/bin/env python3

import sys
import os
from collections import defaultdict
from typing import IO


def isValid(s: str) -> bool:
    """
    Sherlock considers a string to be valid if all characters of the string appear the same number of times.
    It is also valid if he can remove just  character at  index in the string, and the remaining characters
    will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.
    """
    counts = defaultdict(int)
    for char in s:
        counts[char] += 1
    counts = sorted(counts.values())

    return \
        (counts[0] == counts[-1]) or \
        (counts[0] == 1 and counts[1] == counts[-1]) or \
        (counts[0] == counts[-2] == counts[-1] - 1)


def main(fptr: IO) -> None:
    s = input()
    result = isValid(s)
    fptr.write(('YES' if result else 'NO') + '\n')


if __name__ == "__main__":
    if "OUTPUT_PATH" in os.environ:
        with open(os.environ["OUTPUT_PATH"], "wt") as fptr:
            main(fptr)
            fptr.close()
    else:
        main(sys.stdout)
