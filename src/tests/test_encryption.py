
from src.encryption import main

from . import loop


def test_answer() -> None:
    loop.loop_inputs("encryption-*", main)
