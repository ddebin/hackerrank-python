
from src.quadrant_queries_v2 import main

from . import loop


def test_answer() -> None:
    loop.loop_inputs("quadrant-queries-*", main)
