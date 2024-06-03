import pytest
from eulerian_path import EulerianPath

# Create fixture for instantiating
@pytest.fixture
def tester():
    return EulerianPath()

# Test for balance dictionary
def test_graph_balance(tester):
    graph = {"0" : ["2"], "1" : ["3"], "2" : ["1"], "3" : ["0","4"], "6" : ["3","7"], "7" : ["8"], "8" : ["9"], "9" : ["6"]}
    tester.graph = graph
    generated_balance = tester.graph_balance()
    expected_balance = {"0" : [1,1], "1" : [1,1] , 
                        "2" : [1,1], "3" : [2,2], 
                        "6" : [1,2], "7" :[1,1], 
                        "8" : [1,1], "9" :[1,1],
                        "4":[1,0]
                        }
    assert expected_balance == generated_balance

def test_graph_cycle(tester):
    graph = {"0" : ["2"], "1" : ["3"], "2" : ["1"], "3" : ["0","4"], "6" : ["3","7"], "7" : ["8"], "8" : ["9"], "9" : ["6"]}
    expected_graph = {"0" : ["2"], "1" : ["3"], "2" : ["1"], "3" : ["0","4"], "6" : ["3","7"], "7" : ["8"], "8" : ["9"], "9" : ["6"], "4": ["6"]}
    tester.graph = graph
    tester.graph_cycle()
    modified_graph = tester.graph
    assert expected_graph == modified_graph
    




