import pytest
from eulerian_path import EulerianPath

# Create fixture for instantiating
@pytest.fixture
def tester():
    return EulerianPath()

# Test for no branching point
def test_no_branching(tester):
    unused_edges = {"1": ["2"], "2": ["3"]}
    current_node = "1"
    assert tester.next_node(unused_edges=unused_edges, current_node=current_node) == "2"

# Test for branching point
def test_branching(tester):
    unused_edges = {"1": ["2", "3"]}
    current_node = "1"
    assert tester.next_node(unused_edges=unused_edges, current_node=current_node) in ("2", "3")
