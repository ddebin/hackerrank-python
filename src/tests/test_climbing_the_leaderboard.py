
from src.climbing_the_leaderboard import main

from . import loop


def test_answer() -> None:
    loop.loop_inputs("climbing-the-leaderboard-*", main)
