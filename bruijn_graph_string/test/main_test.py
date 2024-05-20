import pytest
from pathlib import Path
from bruijn_graph_string import BruijnGraphString


def file_paths():
    """
    Fixture to provide input and expected output file paths.
    """

    return [
        {
            "input": Path("tests/input.txt"),
            "expected_output": Path("tests/exp_output.txt"),
            "generated_output": Path("tests/gen_output.txt")
        },
    ]

def read_file(path):
    """Helper function to read files"""
    
    with open(path, "r") as file:
        return file.read().strip()

@pytest.mark.parametrize("file_data", file_paths())
def test_bruijn_graph(file_data):
    tester = BruijnGraphString(input_path=file_data["input"], output_path=file_data["generated_output"])
    tester.read_sequence()
    k_mers = tester.create_k_mers()
    graph = tester.construct_graph(k_mers=k_mers)
    tester.output(graph)
    
    # Read expected and generated output
    expected_output = read_file(file_data["expected_output"])
    generated_output = read_file(file_data["generated_output"])
    
    # Check if outputs are equal
    assert expected_output == generated_output