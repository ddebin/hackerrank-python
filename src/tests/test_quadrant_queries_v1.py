
from src.quadrant_queries_v1 import main

from . import loop


def test_answer() -> None:
    loop.loop_inputs("quadrant-queries-*", main)
