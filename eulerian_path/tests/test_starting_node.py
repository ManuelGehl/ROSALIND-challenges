import pytest
from eulerian_path import EulerianPath
from pathlib import Path

# Create fixture for instantiating
@pytest.fixture
def tester():
    return EulerianPath()

# Test for no walked path
def test_no_walked_path(tester):
    unused_edges = {"1": "2", "2": "3"}
    walked_path = []
    assert tester.starting_node(walked_path=walked_path, unused_edges=unused_edges) == "1"

# Test for walked path
def test_walked_path(tester):
    unused_edges = {"1": "2", "2": "3"}
    walked_path = ["1", "2", "3", "4"]
    assert tester.starting_node(walked_path=walked_path, unused_edges=unused_edges) == "2"