#!/usr/bin/env python3

import sys
import os
from typing import IO


def climbingLeaderboard(ranked: list[int], player: list[int]) -> list[int]:
    ranks = []

    current_rank = 1
    last_ranked_score = -1
    for ranked_score in ranked:
        while len(player) > 0 and player[-1] >= ranked_score:
            ranks.insert(0, current_rank)
            player.pop()

        if ranked_score != last_ranked_score:
            current_rank += 1
            last_ranked_score = ranked_score

    while len(player) > 0:
        ranks.insert(0, current_rank)
        player.pop()

    return ranks


def main(fptr: IO) -> None:
    ranked_count = int(input().strip())
    ranked = list(map(int, input().rstrip().split()))
    assert len(ranked) == ranked_count
    player_count = int(input().strip())
    player = list(map(int, input().rstrip().split()))
    assert len(player) == player_count
    result = climbingLeaderboard(ranked, player)
    fptr.write("\n".join(map(str, result)) + "\n")


if __name__ == "__main__":
    if "OUTPUT_PATH" in os.environ:
        with open(os.environ["OUTPUT_PATH"], "wt") as fptr:
            main(fptr)
            fptr.close()
    else:
        main(sys.stdout)
