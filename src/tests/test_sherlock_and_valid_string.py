
from src.sherlock_and_valid_string import main

from . import loop


def test_answer() -> None:
    loop.loop_inputs("sherlock-and-valid-string-*", main)
