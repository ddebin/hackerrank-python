import sys
import tempfile
from collections.abc import Callable
from pathlib import Path


def loop_inputs(pattern: str, function: Callable) -> None:
    files = Path(__file__).parent.joinpath("data").glob(f"{pattern}.input")
    for input_file in files:
        output_file = input_file.with_suffix(".output")
        with (
            Path(input_file).open(encoding="utf-8") as sys.stdin,
            tempfile.NamedTemporaryFile(
                mode="w+t", encoding="utf-8", delete=True, delete_on_close=True,
            ) as temp_file,
        ):
            function(temp_file.file)
            temp_file.file.seek(0)
            with Path(output_file).open(mode="r+t", encoding="utf-8") as output_file:
                assert (
                    output_file.read() == temp_file.read()
                ), f"Answer failed for {Path(input_file).name}"
                output_file.close()
            temp_file.close()
