# bruijn_graph_string

`BruijnGraphString` is a Python class designed to read a DNA sequence and k-mer size from an input file, generate k-mers, construct a De Bruijn graph, and write the adjacency list of the graph to an output file.

## Class: `BruijnGraphString`

### Constants

`DEFAULT_INPUT_PATH`: Default path for the input file, set to "input.txt".

`DEFAULT_OUTPUT_PATH`: Default path for the output file, set to "output.txt".

### Constructor

```{python}
def __init__(self, input_path=None, output_path=None):
```

Parameters:

`input_path` (str, optional): Path to the input file. Defaults to "input.txt".

`output_path` (str, optional): Path to the output file. Defaults to "output.txt".

### Methods

`read_sequence() -> None`: Reads the sequence and k-mer size from the input file.

`create_k_mers() -> set`: Creates a set of unique k-mers from the sequence.

`construct_graph(k_mers: set) -> list`: Constructs the De Bruijn graph from the k-mers.

`output(adjacency_list: list) -> None`: Writes the adjacency list to the output file.

## Input File Format

The input file should contain:
- The k-mer size on the first line.
- The DNA sequence on the subsequent line.

Example Input File (input.txt)

```
4
ACGTACGTG
```

## Output

The output file will contain the adjacency list of the De Bruijn graph.

Example Output File (output.txt)
```
ACG -> CGT
CGT -> GTA,GTG
GTA -> TAC
TAC -> ACG
```
