#!/usr/bin/env python3

import sys
import os
from typing import IO


def print_matrix(matrix: list[list[int]]) -> None:
    for r in matrix:
        fptr.write(" ".join(map(str, r)) + "\n")


def rotate(matrix: list[list[int]], layer: int, m: int, n: int) -> None:
    """Rotate matrix with m lines, n columns"""
    tmp = matrix[layer][layer]
    # left border
    for i in range(layer + 1, m - layer):
        tmp2 = matrix[i][layer]
        matrix[i][layer] = tmp
        tmp = tmp2
    # bottom border
    for j in range(layer + 1, n - layer):
        tmp2 = matrix[m - 1 - layer][j]
        matrix[m - 1 - layer][j] = tmp
        tmp = tmp2
    # right border
    for i in range(m - 1 - layer - 1, layer - 1, -1):
        tmp2 = matrix[i][n - 1 - layer]
        matrix[i][n - 1 - layer] = tmp
        tmp = tmp2
    # top border
    for j in range(n - 1 - layer - 1, layer, -1):
        tmp2 = matrix[layer][j]
        matrix[layer][j] = tmp
        tmp = tmp2
    # top left
    matrix[layer][layer] = tmp


def matrixRotation(matrix: list[list[int]], r: int, m: int, n: int) -> None:
    layers = min(m, n) // 2
    for layer in range(layers):
        steps_in_turn = (m - layer * 2 - 1) * 2 + (n - layer * 2 - 1) * 2
        steps = r % steps_in_turn
        for _ in range(steps):
            rotate(matrix, layer, m, n)


def main(fptr: IO) -> None:
    first_multiple_input = input().rstrip().split()
    m = int(first_multiple_input[0])
    n = int(first_multiple_input[1])
    r = int(first_multiple_input[2])
    matrix = []
    for _ in range(m):
        line = list(map(int, input().rstrip().split()))
        assert len(line) == n
        matrix.append(line)
    matrixRotation(matrix, r, m, n)
    print_matrix(matrix)


if __name__ == "__main__":
    if "OUTPUT_PATH" in os.environ:
        fptr = open(os.environ["OUTPUT_PATH"], "wt")
    else:
        fptr = sys.stdout

    main(fptr)

    fptr.close()
