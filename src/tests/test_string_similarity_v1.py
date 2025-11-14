
from src.string_similarity_v1 import main

from . import loop


def test_answer() -> None:
    loop.loop_inputs("string-similarity-*", main)
