#!/usr/bin/env python3

import math
import os
import sys
from typing import IO


# count nodes in a range
def countNodes(
    start: int, end: int, level: int, leaf_start: int, leaf_end: int
) -> list[int]:
    leafs = 2 ** (levels - level)
    node_idx = 2 ** (level - 1) - 1 + leaf_end // leafs - 1

    if end - start + 1 == leafs:
        n = tree[node_idx][:4]
    else:
        split = leaf_start + (leaf_end - leaf_start) // 2
        left = (
            countNodes(start, min(end, split), level + 1, leaf_start, split)
            if start <= min(end, split)
            else [0, 0, 0, 0]
        )
        right = (
            countNodes(max(start, split + 1), end, level + 1, split + 1, leaf_end)
            if max(start, split + 1) <= end
            else [0, 0, 0, 0]
        )
        n = [left[i] + right[i] for i in range(4)]

    if tree[node_idx][4] & 1 == 1:
        n = [n[3], n[2], n[1], n[0]]
    if tree[node_idx][4] & 2 == 2:
        n = [n[1], n[0], n[3], n[2]]

    return n


# flip nodes in a range and update all counts in the subtree containing the range
def flipNodes(
    start: int,
    end: int,
    level: int,
    leaf_start: int,
    leaf_end: int,
    flip: int,
    deepInit: bool,
) -> list[int]:
    leafs = 2 ** (levels - level)  # leafs count at level
    node_idx = 2 ** (level - 1) - 1 + leaf_end // leafs - 1  # node index in tree array
    width = end - start + 1

    if (width == leafs or start > end) and (not deepInit or level == levels):
        n = tree[node_idx][:4]
        if width == leafs:
            tree[node_idx][4] ^= flip
    else:
        split = leaf_start + (leaf_end - leaf_start) // 2
        left = flipNodes(
            start, min(end, split), level + 1, leaf_start, split, flip, deepInit
        )
        right = flipNodes(
            max(start, split + 1), end, level + 1, split + 1, leaf_end, flip, deepInit
        )
        n = [left[i] + right[i] for i in range(4)]
        tree[node_idx][:4] = n

    if tree[node_idx][4] & 1 == 1:
        n = [n[3], n[2], n[1], n[0]]
    if tree[node_idx][4] & 2 == 2:
        n = [n[1], n[0], n[3], n[2]]

    return n


def quadrants(fptr: IO, queries: list[list[str]]) -> None:
    # init counts
    flipNodes(1, leafs, 1, 1, leafs, 0, True)

    for q in queries:
        start = int(q[1])
        end = int(q[2])
        match q[0]:
            case "X":
                flipNodes(start, end, 1, 1, leafs, 1, False)
            case "Y":
                flipNodes(start, end, 1, 1, leafs, 2, False)
            case "C":
                C = countNodes(start, end, 1, 1, leafs)
                fptr.write(f"{C[0]} {C[1]} {C[2]} {C[3]}\n")


def main(fptr: IO) -> None:
    n = int(input().strip())
    p = []
    for _ in range(n):
        c = list(map(int, input().rstrip().split()))
        quadrant_count = [
            int(c[0] > 0 and c[1] > 0),  # 1st quadrant
            int(c[0] < 0 and c[1] > 0),  # 2nd quadrant
            int(c[0] < 0 and c[1] < 0),  # 3rd quadrant
            int(c[0] > 0 and c[1] < 0),  # 4th quadrant
            0,  # flip X 0/1, flip Y 0/2
        ]
        p.append(quadrant_count)

    # create left-complete binary tree
    # array representation starts with higher level node (0) and ends with leafs
    # each node contains the count per quadrant of the subtree and if it's flipped X/Y

    global tree, levels, leafs
    levels = math.ceil(math.log2(len(p))) + 1
    tree = [[0, 0, 0, 0, 0] for _ in range(2**levels - 1)]
    leafs = 2 ** (levels - 1)
    tree[leafs - 1 : leafs - 1 + len(p)] = p

    q = int(input().strip())
    queries = []
    for _ in range(q):
        queries_item = input().split()
        queries.append(queries_item)

    quadrants(fptr, queries)


if __name__ == "__main__":
    if "OUTPUT_PATH" in os.environ:
        with open(os.environ["OUTPUT_PATH"], "wt") as fptr:
            main(fptr)
            fptr.close()
    else:
        main(sys.stdout)
