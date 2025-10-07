#!/usr/bin/env python3

import sys
import os
import bisect
from collections import defaultdict
from typing import IO, Dict, List
from collections import deque
from operator import itemgetter


class TrieNode:
    def __init__(self):
        # Initialize TrieNode attributes
        self.children: Dict[str, TrieNode] = defaultdict(TrieNode)
        self.output: List[str] = []
        self.fail: TrieNode | None = None


# cf. https://en.wikipedia.org/wiki/Aho%E2%80%93Corasick_algorithm
def build_automaton(keywords: set[str]) -> TrieNode:
    # Initialize root node of the trie
    root = TrieNode()

    # Build trie
    for keyword in keywords:
        node = root
        # Traverse the trie and create nodes for each character
        for char in keyword:
            node = node.children[char]
        # Add keyword to the output list of the final node
        node.output.append(keyword)

    # Build failure links using BFS
    queue = deque()

    # Start from root's children
    for node in root.children.values():
        queue.append(node)
        node.fail = root

    # Breadth-First traversal of the trie
    while queue:
        current_node = queue.popleft()
        # Traverse each child node
        for key, next_node in current_node.children.items():
            queue.append(next_node)
            fail_node = current_node.fail
            # Find the longest proper suffix that is also a prefix
            while fail_node and (key not in fail_node.children):
                fail_node = fail_node.fail
            # Set failure link of the current node
            next_node.fail = fail_node.children[key] if fail_node else root
            # Add output patterns of failure node to current node's output
            next_node.output += next_node.fail.output

    return root


def computeHealth(
    root: TrieNode,
    catalogue: dict[str, list[tuple[int, int]]],
    first: int,
    last: int,
    dna: str,
) -> int:
    h = 0
    current_node = root
    # Traverse the text
    for char in dna:
        # Follow failure links until a match is found
        while current_node and (char not in current_node.children):
            current_node = current_node.fail
        if not current_node:
            current_node = root
            continue

        # Move to the next node based on current character
        current_node = current_node.children[char]

        # Update sum with gene found at this position
        for gene in current_node.output:
            h += sumInRange(catalogue[gene], first, last)

    return h


def sumInRange(values: list[tuple[int, int]], first: int, last: int) -> int:
    start = bisect.bisect_left(values, first, key=itemgetter(0))
    end = bisect.bisect_right(values, last, key=itemgetter(0))
    return (
        values[end - 1][1] - (values[start - 1][1] if start > 0 else 0)
        if end > start
        else 0
    )


def main(fptr: IO) -> None:
    n = int(input().strip())
    genes = input().rstrip().split()
    assert len(genes) == n
    health = list(map(int, input().rstrip().split()))
    assert len(health) == n
    s = int(input().strip())

    len_max = 0
    len_min = sys.maxsize
    alphabet = set()
    genes_dict = defaultdict(list[tuple[int, int]])
    genes_dict_csum = defaultdict(int)
    for i in range(n):
        g = genes[i]
        genes_dict_csum[g] += health[i]
        genes_dict[g].append((i, genes_dict_csum[g]))
        len_max = max(len_max, len(g))
        len_min = min(len_min, len(g))
        alphabet.update(list(g))

    print(
        f"Alphabet of {len(alphabet)}, genes length between {len_min} and {len_max}, {len(genes_dict)} genes, {s} strands"
    )

    dnas = []
    for _ in range(s):
        first_multiple_input = input().rstrip().split()
        first = int(first_multiple_input[0])
        last = int(first_multiple_input[1])
        d = first_multiple_input[2]
        dnas.append((first, last, d))

    max_h = 0
    min_h = sys.maxsize

    if len_min == len_max:
        print("Fast Mode!")
        for first, last, d in dnas:
            h = 0
            for i in range(len(d) - len_min + 1):
                keyword = d[i : i + len_min]
                if keyword in genes_dict:
                    h += sumInRange(genes_dict[keyword], first, last)
            max_h = max(max_h, h)
            min_h = min(min_h, h)

    else:
        # Build the Aho-Corasick automaton
        print("Aho-Corasick!")
        genes_unique = set(genes)
        trie = build_automaton(genes_unique)
        for first, last, d in dnas:
            h = computeHealth(trie, genes_dict, first, last, d)
            max_h = max(max_h, h)
            min_h = min(min_h, h)

    fptr.write(f"{min_h} {max_h}\n")


if __name__ == "__main__":
    if "OUTPUT_PATH" in os.environ:
        with open(os.environ["OUTPUT_PATH"], "wt") as fptr:
            main(fptr)
            fptr.close()
    else:
        main(sys.stdout)
