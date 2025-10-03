#!/usr/bin/env python3

import os
import sys
import math
from typing import IO


def encryption(s: str) -> str:
    s_len = len(s)

    rows = math.floor(math.sqrt(s_len))
    columns = math.ceil(math.sqrt(s_len))
    while rows * columns < s_len:
        if rows < columns:
            rows += 1
        else:
            columns += 1

    matrix = [s[i : i + columns] for i in range(0, s_len, columns)]

    return " ".join(
        "".join(line[i] for line in matrix if i < len(line)) for i in range(columns)
    )


def main(fptr: IO) -> None:
    s = input().rstrip()
    result = encryption(s)
    fptr.write(result + "\n")


if __name__ == "__main__":
    if "OUTPUT_PATH" in os.environ:
        with open(os.environ["OUTPUT_PATH"], "wt") as fptr:
            main(fptr)
            fptr.close()
    else:
        main(sys.stdout)
