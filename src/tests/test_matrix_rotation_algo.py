
from src.matrix_rotation_algo import main

from . import loop


def test_answer() -> None:
    loop.loop_inputs("matrix_rotation_algo-*", main)
