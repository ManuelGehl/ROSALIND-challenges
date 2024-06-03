import pytest
from eulerian_path import EulerianPath
from pathlib import Path

# Create fixture for instantiating
@pytest.fixture
def tester():
    return EulerianPath()

# Helper function to compare cylces
def are_cycles_equivalent(cycle1, cycle2):
    # Check if both cycles have the same length
    if len(cycle1) != len(cycle2):
        return False
    
    # Double one of the cycles and check if the other cycle is a sublist
    doubled_cycle1 = cycle1 + cycle1
    for i in range(len(cycle1)):
        if doubled_cycle1[i:i + len(cycle2)] == cycle2:
            return True
    
    return False

# Test for function
def test_walk_graph_1(tester):
    graph = {
        "0" : ["2"], "1" : ["3"], "2" : ["1"], "3" : ["0","4"], 
        "6" : ["3","7"], "7" : ["8"], "8" : ["9"], "9" : ["6"]
        }
    expectation = ["6","7","8","9","6","3","0","2","1","3","4"]
    tester.graph = graph
    tester.graph_cycle()
    eulerian_cycle = tester.walk_graph()[:-1]
    
    # Check if 2 cycles are equivalent
    assert are_cycles_equivalent(cycle1=expectation, cycle2=eulerian_cycle) == True

def test_walk_graph_2(tester):
    graph_path = Path("tests/test_graph.txt")
    tester.input_path = graph_path
    tester.read_input()
    tester.graph_cycle()
    walked_path = tester.walk_graph()
    linear_path = tester.linearize_path(walked_path=walked_path)
    
    expected_path = Path("tests/expected_output.txt")
    with open(expected_path, "r") as file:
        expected_output = file.readline()
        expected_output = expected_output.split("->")
        
        # Check if 2 cycles are equivalent
        assert are_cycles_equivalent(cycle1=expected_output, cycle2=linear_path) == True
    
