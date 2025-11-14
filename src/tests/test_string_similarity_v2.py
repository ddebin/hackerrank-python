
from src.string_similarity_v2 import main

from . import loop


def test_answer() -> None:
    loop.loop_inputs("string-similarity-*", main)
