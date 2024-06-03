import pytest
from eulerian_path import EulerianPath
from pathlib import Path

# Create fixture for instantiating
@pytest.fixture
def tester():
    return EulerianPath()

# Test for unbrached edges
def test_remove_edges_unbranched(tester):
    unused_edges = {"1": ["2"], "2": ["3"]}
    walked_path = ["9", "9", "9", "1", "2"]
    assert tester.remove_edge(walked_path=walked_path, unused_edges=unused_edges) == {"2": ["3"]}

# Test for brached edges
def test_remove_edges_branched(tester):
    unused_edges = {"1": ["2", "3", "4"], "2": ["3"]}
    walked_path = ["9", "9", "9", "1", "2"]
    assert tester.remove_edge(walked_path=walked_path, unused_edges=unused_edges) == {"1": ["3", "4"], "2": ["3"]}
