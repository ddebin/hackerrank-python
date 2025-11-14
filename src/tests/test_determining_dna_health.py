
from src.determining_dna_health import main

from . import loop


def test_answer() -> None:
    loop.loop_inputs("determining-dna-health-*", main)
