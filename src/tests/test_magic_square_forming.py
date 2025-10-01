from ..magic_square_forming import main
from . import loop
import sys


def test_answer():
    loop.loop_inputs("magic-square-forming-*", main)


def setup_method(self):
    self.orig_stdin = sys.stdin


def teardown_method(self):
    sys.stdin = self.orig_stdin
