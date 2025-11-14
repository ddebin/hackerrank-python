
from src.bigger_is_greater import main

from . import loop


def test_answer() -> None:
    loop.loop_inputs("biggers-is-greater-*", main)
