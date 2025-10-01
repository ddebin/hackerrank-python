from ..the_grid_search import main
from . import loop
import sys


def test_answer():
    loop.loop_inputs("the-grid-search-*", main)


def setup_method(self):
    self.orig_stdin = sys.stdin


def teardown_method(self):
    sys.stdin = self.orig_stdin
