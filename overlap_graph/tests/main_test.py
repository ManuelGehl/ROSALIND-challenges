import pytest
from pathlib import Path
from overlap_graph import OverlapGraph

# Import correct solution
expected_output_path = Path("tests/exp_output.txt")
input_path = Path("tests/input.txt")
generated_output_path = Path("tests/gen_output.txt")

# Read in correct solution
with open(expected_output_path, "r") as file:
    expected_output = file.read().strip()
    
def test_overlap_graph():
    tester = OverlapGraph(input_path=input_path, output_path=generated_output_path)
    tester.read_sequences()
    graph = tester.construct_graph()
    tester.output(graph)
    
    # Read generated output
    with open(generated_output_path, "r") as file:
        generated_output = file.read().strip()
    
    # Check if outputs are equal
    assert generated_output == expected_output
        
    