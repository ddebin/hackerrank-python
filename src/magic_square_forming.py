#!/usr/bin/env python3

import os
import sys
from typing import IO

min_cost = 100


def loop(s: list[int], pos: int, cost: int) -> None:
    global min_cost

    s = s.copy()

    orig = s[pos]
    for i in range(1, 10):
        # don't use a number allready in square before `pos`
        if pos > 0 and i in s[:pos]:
            continue

        s[pos] = i
        c = cost + abs(i - orig)

        if pos == 8:
            # all swaps are done
            if (
                s[0] + s[1] + s[2]
                == s[3] + s[4] + s[5]
                == s[6] + s[7] + s[8]
                == s[0] + s[3] + s[6]
                == s[1] + s[4] + s[7]
                == s[2] + s[5] + s[8]
                == s[0] + s[4] + s[8]
                == s[2] + s[4] + s[6]
            ):
                min_cost = min(min_cost, c)
        else:
            loop(s, pos + 1, c)

    return


def formingMagicSquare(s: list[list[int]]) -> int:
    flat = [x for xs in s for x in xs]
    loop(flat, 0, 0)
    return min_cost


def main(fptr: IO) -> None:
    s = [list(map(int, input().rstrip().split())) for _ in range(3)]
    result = formingMagicSquare(s)
    fptr.write(str(result) + "\n")


if __name__ == "__main__":
    if "OUTPUT_PATH" in os.environ:
        fptr = open(os.environ["OUTPUT_PATH"], "wt")
    else:
        fptr = sys.stdout

    main(fptr)

    fptr.close()
