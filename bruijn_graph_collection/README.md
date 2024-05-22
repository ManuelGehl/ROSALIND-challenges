# De Bruijn Graph Collection

The bruijn_graph_collection.py script is designed to construct a De Bruijn graph from a collection of sequences. It reads sequences from an input file, constructs the graph by creating edges based on k-mers, and writes the resulting graph to an output file.

## Classes
`BruijnGraphCollection`: 
- This class handles the creation of the De Bruijn graph from sequences. It provides methods to read sequences, create graph edges, and output the graph.
- Attributes:
  - `DEFAULT_INPUT_PATH`: Default input file path (input.txt).
  - `DEFAULT_OUTPUT_PATH`: Default output file path (output.txt).

## Methods
`__init__(self, input_path=None, output_path=None)`

Initializes the BruijnGraphCollection object with optional input and output file paths. If paths are not provided, default paths are used.

Parameters:

    `input_path` (str, optional): Path to the input file containing sequences.
    `output_path` (str, optional): Path to the output file for the graph.

`read_sequences(self) -> None`

Reads sequences from the input file and stores them in the sequences attribute. Raises a FileNotFoundError if the input file is missing or empty.

Exceptions:

    FileNotFoundError: Raised if the input file is not found or is empty.

`create_edges(self) -> dict`

Creates edges for the De Bruijn graph from the sequences. Each sequence is split into nodes and edges based on k-mers. Returns a dictionary where keys are nodes and values are lists of adjacent nodes.

Returns:

    dict: Dictionary representing the edges of the De Bruijn graph.

Exceptions:

    ValueError: Raised if sequences are not initialized.

`output(self, edges: dict) -> None`

Writes the edges of the De Bruijn graph to the output file. The format is node_1 -> node_2,node_3,....

Parameters:

    edges (dict): Dictionary of graph edges to be written to the output file.

## Usage
The script can be run as a standalone program. It reads sequences from the input file, constructs the De Bruijn graph, and writes the graph to the output file.

### Main Function

The main function orchestrates the sequence of operations: reading sequences, creating edges, and outputting the graph.

```{python}
def main():
    de_bruijn_graph = BruijnGraphCollection()
    de_bruijn_graph.read_sequences()
    nodes = de_bruijn_graph.create_edges()
    de_bruijn_graph.output(nodes)
    print("Finished construction of De Bruijn graph")
```

## Dependencies

The script relies on the `pathlib` module from the Python standard library for file path operations.
