#!/usr/bin/env python3

import sys
import os
from typing import IO


def morganAndString(fptr: IO, a: str, b: str) -> None:
    i = j = 0
    # '~' is > 'z'
    while not a[i] == b[j] == "~":
        if a[i:] < b[j:]:
            fptr.write(a[i])
            i += 1
        else:
            fptr.write(b[j])
            j += 1


def main(fptr: IO) -> None:
    t = int(input().strip())
    for _itr in range(t):
        a = input() + "~"
        b = input() + "~"
        morganAndString(fptr, a, b)
        fptr.write("\n")


if __name__ == "__main__":
    if "OUTPUT_PATH" in os.environ:
        fptr = open(os.environ["OUTPUT_PATH"], "wt")
    else:
        fptr = sys.stdout

    main(fptr)

    fptr.close()
