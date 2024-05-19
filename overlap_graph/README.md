# overlap_graph

The `OverlapGraph` class is designed to create an overlap graph from a set of sequences. An overlap graph is a directed graph where each sequence is represented as a node, and a directed edge from node A to node B exists if the suffix of sequence A matches the prefix of sequence B. This class reads sequences from an input file, constructs the graph, and writes the adjacency list to an output file.

## Class: OverlapGraph
Attributes:
- `DEFAULT_INPUT_PATH` (Path): Default path to the input file containing sequences (input.txt).
- `DEFAULT_OUTPUT_PATH` (Path): Default path to the output file for the adjacency list (output.txt).

## Methods
`__init__(self, input_path=None, output_path=None)`:
- Initializes the OverlapGraph object with optional input and output file paths.

`read_sequences(self)`:
- Reads sequences from the input file and sets the overlap length.

`construct_graph(self)`:
- Constructs the overlap graph as an adjacency list.

`output(self, adjacency_list: list)`:
- Writes the adjacency list to the output file.

## Usage Example

```{python}
def main():
    """
    Main function to execute the OverlapGraph operations: read sequences, construct the graph, and output the result.
    """
    
    overlap_graph = OverlapGraph()
    overlap_graph.read_sequences()
    graph = overlap_graph.construct_graph()
    overlap_graph.output(graph)
    print("Done")

if __name__ == "__main__":
    main()
```

**Notes:**
- Ensure that the input file is in the correct format, with one sequence per line.
- The sequences should all be of the same length for the overlap length to be correctly computed.
