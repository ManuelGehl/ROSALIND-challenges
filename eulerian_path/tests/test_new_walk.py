import pytest
from eulerian_path import EulerianPath
from pathlib import Path

# Create fixture for instantiating
@pytest.fixture
def tester():
    return EulerianPath()

# Test for no edge in unused_edges
def test_no_edge(tester):
    unused_edges = {"1": ["2"], "2": ["3"]}
    walked_path = ["5", "6", "7", "8"]
    with pytest.raises(ValueError):
        result_edges, result_path = tester.new_walk(unused_edges=unused_edges, walked_path=walked_path)

# Test for edge already in unused_edges
def test_with_edge(tester):
    unused_edges = {"1": ["2"]}
    walked_path = ["0", "1", "3", "0"]
    result_edges, result_path = tester.new_walk(unused_edges=unused_edges, walked_path=walked_path)
    assert result_edges == {"1": ["2"]}
    assert result_path == ["1", "3", "0", "1"]
