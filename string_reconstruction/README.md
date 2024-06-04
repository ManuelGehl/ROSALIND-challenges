# String Reconstruction from De Bruijn Graph

## Overview

This project provides a tool for reconstructing a sequence from its k-mer compositions using De Bruijn graphs. It reads sequences from an input file, constructs the De Bruijn graph, finds an Eulerian path, and outputs the reconstructed sequence.

## Installation
**Prerequisites:**
- Python 3.7 or later
- Required Python packages: pathlib, random, itertools, logging

## Usage

By default, the script reads sequences from input.txt and writes the reconstructed sequence to output.txt. You can run the script with the following command:

```{bash}
python string_reconstruction.py
```

**Custom Input and Output Paths**

You can specify custom paths for the input and output files by modifying the StringReconstruction class initialization:

```{python}
string_reconstructor = StringReconstruction(input_path="your_input_file.txt", output_path="your_output_file.txt")
```

## Files and Directories

- string_reconstruction.py: Main script for reconstructing the string from De Bruijn graph.
- input.txt: Default input file containing k-mer sequences.
- output.txt: Default output file where the reconstructed sequence is written.
- log_files/: Directory for storing log configuration files.

## StringReconstruction Class

The `StringReconstruction` class is designed to reconstruct a sequence from its k-mer compositions using De Bruijn graphs. It reads sequences from an input file, constructs the De Bruijn graph, finds an Eulerian path, and outputs the reconstructed sequence.

**Class Attributes:**
- `DEFAULT_INPUT_PATH` (Path): Default path to the input file (input.txt).
- `DEFAULT_OUTPUT_PATH` (Path): Default path to the output file (output.txt).

**Instance Attributes:**
- `input_path` (Path): Path to the input file.
- `output_path` (Path): Path to the output file.
- `sequences` (list): List of k-mer sequences read from the input file.
- `graph` (dict): Adjacency list representing the De Bruijn graph.
- `additional_edge` (dict): Dictionary to store an additional edge added to make the graph Eulerian.
- `logger` (Logger): Logger instance for logging information and debugging.

### Methods
**`__init__(self, input_path=None, output_path=None)`**

Initializes the StringReconstruction object, sets up logging, and defines the input and output paths.

**Parameters:**
- `input_path` (str, optional): Custom path to the input file. Defaults to input.txt.
- `output_path` (str, optional): Custom path to the output file. Defaults to output.txt.

**`read_sequences(self) -> None`**

Reads sequences from the input file and stores them in the sequences attribute. Raises an error if the file does not exist or is empty.

**`create_edges(self) -> set`**

Creates edges for the De Bruijn graph from the k-mer sequences and stores them in the graph attribute. Raises an error if sequences is not initialized.

**`graph_balance(self) -> dict`**

Calculates the balance of each node in the graph, i.e., the difference between incoming and outgoing edges.

Returns:
- dict: A dictionary with nodes as keys and their balance (incoming and outgoing edges) as values.

**`graph_cycle(self) -> None`**

Transforms the graph into a cycle by adding an artificial edge if necessary to balance the graph.

**`starting_node(self, walked_path: list, unused_edges: dict) -> str`**

Selects the starting node for walking the graph.

Parameters:
- `walked_path` (list): List of nodes in the walked path.
- `unused_edges` (dict): Dictionary of unused edges in the graph.

Returns:
- str: The starting node.

**`next_node(self, unused_edges: dict, current_node: str) -> str`**

Selects the next node to walk to from the current node.

Parameters:
- `unused_edges` (dict): Dictionary of unused edges in the graph.
- `current_node` (str): The current node in the walk.

Returns:
- str: The next node to walk to.

**`remove_edge(self, unused_edges: dict, walked_path: list) -> dict`**

Removes an edge from the graph once it has been walked.

Parameters:
- `unused_edges` (dict): Dictionary of unused edges in the graph.
- `walked_path` (list): List of nodes in the walked path.

Returns:
- dict: Updated dictionary of unused edges.

**`new_walk(self, unused_edges: dict, walked_path: list) -> tuple[dict, list]`**

Starts a new walk when no further path can be found from the current node.

Parameters:
- `unused_edges` (dict): Dictionary of unused edges in the graph.
- `walked_path` (list): List of nodes in the walked path.

Returns:
- tuple: Updated dictionary of unused edges and walked path.

**`walk_graph(self) -> list`**

Walks through the graph to find an Eulerian path.

Returns:
- list: List of nodes representing the walked Eulerian path.

**`linearize_path(self, walked_path: list) -> list`**

Linearizes a walked path in the graph by ensuring overlap between segments.

Parameters:
- `walked_path` (list): A list representing the walked path in the graph.

Returns:
- list: A linearized path obtained by splitting the walked path at the position of the ending node and reordering the segments to ensure overlap.

Raises:
- ValueError: If the walked path cannot be split into left and right parts due to lack of overlap.

**`sequence_reconstruction(self, linearized_path: list) -> str`**

Reconstructs the sequence from the linearized path.

Parameters:
- `linearized_path` (list): A list representing the linearized path in the graph.

Returns:
- str: The reconstructed sequence.

**`output_reconstructed_string(self, reconstructed_string: str) -> None`**

Writes the reconstructed string to the output file.

Parameters:
- `reconstructed_string` (str): The reconstructed string to be written to the file.

## Example Usage

Here's an example of how to use the StringReconstruction class:

```{python}
from string_reconstruction import StringReconstruction
from pathlib import Path
import random
import itertools
import logging
from log_files.configure_logging import setup_logging

string_reconstructor = StringReconstruction(input_path="your_input_file.txt", output_path="your_output_file.txt")
string_reconstructor.read_sequences()
string_reconstructor.create_edges()
string_reconstructor.graph_cycle()
walked_path = string_reconstructor.walk_graph()
linear_path = string_reconstructor.linearize_path(walked_path=walked_path)
reconstructed_string = string_reconstructor.sequence_reconstruction(linear_path)
string_reconstructor.output_reconstructed_string(reconstructed_string)
```

This example reads sequences from your_input_file.txt, constructs the De Bruijn graph, finds an Eulerian path, linearizes it, reconstructs the sequence, and writes the result to your_output_file.txt.
