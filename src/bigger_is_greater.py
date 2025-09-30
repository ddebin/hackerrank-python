#!/usr/bin/env python3

import os
import sys
from typing import IO


def switchAbove(word: list[int]) -> bool:
    for i in range(len(word) - 2, -1, -1):
        for j in range(len(word) - 1, i, -1):
            if word[i] < word[j]:
                w = word[i]
                word[i] = word[j]
                word[j] = w
                return True
    return False


def switchBelow(word: list[int], best: list[int]) -> list[int]:
    previous_equal = True
    for i in range(0, len(word) - 1):
        if previous_equal and word[i] == best[i]:
            continue
        previous_equal = False
        for j in range(i + 1, len(word)):
            if best[j] < best[i]:
                candidate = best.copy()
                candidate[i] = candidate[j]
                candidate[j] = best[i]
                if word < candidate < best:
                    best = candidate
    return best


def biggerIsGreater(word: str) -> str:
    reference = [ord(c) for c in word]
    best = reference.copy()
    if not switchAbove(best):
        return "no answer"

    while True:
        candidate = switchBelow(reference, best)
        if best != candidate:
            best = candidate
        else:
            break

    return "".join(chr(i) for i in best)


def main(fptr: IO) -> None:
    T = int(input().strip())
    for _ in range(T):
        w = input()
        result = biggerIsGreater(w)
        fptr.write(result + "\n")


if __name__ == "__main__":
    if "OUTPUT_PATH" in os.environ:
        fptr = open(os.environ["OUTPUT_PATH"], "wt")
    else:
        fptr = sys.stdout

    main(fptr)

    fptr.close()
