#!/usr/bin/env python3

import math
import os
import sys
from typing import IO


#  MERGING TWO NODES b & c TO FORM A SINGLE NODE a
def _merge(a: list[int], b: list[int], c: list[int]) -> None:
    bb = b
    if b[4] & 1 == 1:
        bb = [bb[3], bb[2], bb[1], bb[0]]
    if b[4] & 2 == 2:
        bb = [bb[1], bb[0], bb[3], bb[2]]
    cc = c
    if c[4] & 1 == 1:
        cc = [cc[3], cc[2], cc[1], cc[0]]
    if c[4] & 2 == 2:
        cc = [cc[1], cc[0], cc[3], cc[2]]
    a[0] = bb[0] + cc[0]
    a[1] = bb[1] + cc[1]
    a[2] = bb[2] + cc[2]
    a[3] = bb[3] + cc[3]


# FUNCTION BUILDS UP SEGMENT TREE ON THE BASIS OF INITIAL AVAILABLE INFORMATION
def buildst(idx: int, ss: int, se: int, source: list[list[int]]) -> None:
    if ss == se:
        # base case (only single node)
        tree[idx] = [0] * 5
        tree[idx][0:4] = source[ss - 1]
        return

    mid = (ss + se) // 2
    buildst(2 * idx, ss, mid, source)  # build left subtree
    buildst(2 * idx + 1, mid + 1, se, source)  # build right subtree

    # combine result of left subtree and right subtree into current node
    _merge(tree[idx], tree[2 * idx], tree[2 * idx + 1])


# UPDATING NEW INFORMATION IN THE SEGMENT TREE
def update(idx: int, ss: int, se: int, val: int, pos: int) -> None:
    if ss == se:
        # point where the actual updation is required
        tree[idx][4] ^= val
        return

    mid = (ss + se) // 2
    if pos <= mid:
        update(2 * idx, ss, mid, val, pos)
    else:
        update(2 * idx + 1, mid + 1, se, val, pos)

    # propagating upwards the updated information
    _merge(tree[idx], tree[2 * idx], tree[2 * idx + 1])


# UPDATING NEW INFORMATION IN THE SEGMENT TREE
def updateRange(idx: int, ss: int, se: int, val: int, L: int, R: int) -> None:
    if se < L or ss > R:
        # out of range
        return
    if ss == se or (ss >= L and se <= R):
        # point where the actual updation is required
        # or current segment lies completely in the required interval i.e [L,R]
        tree[idx][4] ^= val
        return

    mid = (ss + se) // 2
    updateRange(2 * idx, ss, mid, val, L, R)
    updateRange(2 * idx + 1, mid + 1, se, val, L, R)

    # propagating upwards the updated information
    _merge(tree[idx], tree[2 * idx], tree[2 * idx + 1])


# QUERING INTERVAL [L,R] FOR THE REQUIRED INFORMATION
def query(idx: int, ss: int, se: int, L: int, R: int) -> list[int]:
    if se < L or ss > R:
        # out of range
        return [0, 0, 0, 0, 0]

    if ss >= L and se <= R:
        # current segment lies completely in the required interval i.e [L,R]
        ret = tree[idx]
        if tree[idx][4] & 1 == 1:
            ret = [ret[3], ret[2], ret[1], ret[0], 0]
        if tree[idx][4] & 2 == 2:
            ret = [ret[1], ret[0], ret[3], ret[2], 0]
        return ret

    mid = (ss + se) // 2
    left = query(
        2 * idx, ss, mid, L, R
    )  # extracting information from the left if left segment contains part of our interval
    right = query(
        2 * idx + 1, mid + 1, se, L, R
    )  # extracting information from the right if right segment contains part of our interval

    ret = [0, 0, 0, 0, 0]
    _merge(ret, left, right)
    if tree[idx][4] & 1 == 1:
        ret = [ret[3], ret[2], ret[1], ret[0], 0]
    if tree[idx][4] & 2 == 2:
        ret = [ret[1], ret[0], ret[3], ret[2], 0]

    return ret


def quadrants(fptr: IO, queries: list[list[str]]) -> None:
    for q in queries:
        start = int(q[1])
        end = int(q[2])
        match q[0]:
            case "X":
                updateRange(1, seg_start, seg_end, 1, start, end)
            case "Y":
                updateRange(1, seg_start, seg_end, 2, start, end)
            case "C":
                C = query(1, seg_start, seg_end, start, end)
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
        ]
        p.append(quadrant_count)

    # create left-complete binary tree
    # array representation starts with higher level node (0) and ends with leafs
    # each node contains the count per quadrant of the subtree and if it's flipped X/Y

    global tree, levels, leafs, seg_start, seg_end
    levels = math.ceil(math.log2(len(p))) + 1
    leafs = 2 ** (levels - 1)
    tree = [[0, 0, 0, 0, 0] for _ in range(2**levels)]
    seg_start = 1
    seg_end = len(p)
    buildst(1, seg_start, seg_end, p)

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
