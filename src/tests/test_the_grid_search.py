
from src.the_grid_search import main

from . import loop


def test_answer() -> None:
    loop.loop_inputs("the-grid-search-*", main)
