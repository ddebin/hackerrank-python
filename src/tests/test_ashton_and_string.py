
from src.ashton_and_string import main

from . import loop


def test_answer() -> None:
    loop.loop_inputs("ashton-and-string-*", main)
