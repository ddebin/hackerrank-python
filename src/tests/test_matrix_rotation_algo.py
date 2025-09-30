from ..matrix_rotation_algo import main
import sys
import glob
import os
import tempfile


def test_answer():
    files = glob.glob(os.path.dirname(__file__) + "/data/matrix_rotation_algo-*.input")
    for input_file in files:
        print(input_file)
        output_file = input_file.replace(".input", ".output")
        sys.stdin = open(input_file)
        with tempfile.NamedTemporaryFile(
            mode="w+t", encoding="utf-8", delete=True, delete_on_close=True
        ) as temp_file:
            main(temp_file.file)
            temp_file.file.seek(0)
            with open(output_file, mode="r+t", encoding="utf-8") as output_file:
                assert (
                    output_file.read() == temp_file.read()
                ), f"Answer failed for {os.path.basename(input_file)}"
                output_file.close()
            temp_file.close()


def setup_method(self):
    self.orig_stdin = sys.stdin


def teardown_method(self):
    sys.stdin = self.orig_stdin
