import pytest
from eulerian_path import EulerianPath
from pathlib import Path

# Create fixture for instantiating
@pytest.fixture
def tester():
    return EulerianPath()

# Test for non-existing file
def test_read_sequence_file_not_found(tester):
    tester.input_path = Path("no_file.txt")
    with pytest.raises(FileNotFoundError):
        tester.read_input()

# Test for empty file
def test_read_sequence_empty_file(tester):
    # Prepare test file
    test_path = Path("tests/test_sequence.txt")
    with open(test_path, "w") as file:
        file.write("")
    # Conduct test
    tester.input_path = test_path
    with pytest.raises(FileNotFoundError):
        tester.read_input()

# Test for correct reading of file
def test_read_sequence(tester):
    # Prepare test file
    test_path = Path("tests/test_sequence.txt")
    with open(test_path, "w") as file:
        file.write("0 -> 3\n1 -> 0\n2 -> 1,6")
    
    # Test for correct reading
    tester.input_path = test_path
    tester.read_input()
    assert tester.graph == {"0": ["3"], "1": ["0"], "2": ["1", "6"]}