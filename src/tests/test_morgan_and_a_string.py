
from src.morgan_and_a_string import main

from . import loop


def test_answer() -> None:
    loop.loop_inputs("morgan-and-a-string-*", main)
