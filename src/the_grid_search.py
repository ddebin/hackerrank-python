#!/usr/bin/env python3

import sys
import os
from typing import IO


def gridSearch(G: list[str], P: list[str]) -> str:
    """
    Returns a string("YES", "NO") if pattern P has been found in G.

    Arguments:
    G - the grid to search
    P - the pattern to search for
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
                return "YES"
            start += 1
    return "NO"


def main(fptr: IO) -> None:
    t = int(input().strip())

    for _ in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])
        C = int(first_multiple_input[1])

        G = []
        for _ in range(R):
            G_item = input()
            assert len(G_item) == C
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])
        c = int(second_multiple_input[1])

        P = []
        for _ in range(r):
            P_item = input()
            assert len(P_item) == c
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + "\n")


if __name__ == "__main__":
    if "OUTPUT_PATH" in os.environ:
        with open(os.environ["OUTPUT_PATH"], "wt") as fptr:
            main(fptr)
            fptr.close()
    else:
        main(sys.stdout)
