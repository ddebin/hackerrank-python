
from src.magic_square_forming import main

from . import loop


def test_answer() -> None:
    loop.loop_inputs("magic-square-forming-*", main)
