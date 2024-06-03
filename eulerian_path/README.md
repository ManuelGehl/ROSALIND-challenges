# Eulerian Path Finder

This repository contains a Python script for finding an Eulerian path in a directed graph. The script reads a graph from an input file, processes it to find the Eulerian path, and writes the path to an output file.

## Usage

To use the script, you need to prepare an input file that describes the directed graph. The input file should have each edge on a new line in the format:

```{rust}

Node1 -> Node2

```

## Methods
__init__(self, input_path=None, output_path=None)

Initializes the EulerianPath class with input and output paths.

    Parameters:
        input_path (str or Path, optional): Path to the input file.
        output_path (str or Path, optional): Path to the output file.

read_input(self) -> None

Reads and parses the input file to construct the graph.

    Raises:
        FileNotFoundError: If the input file is not found or is empty.

output_result(self, path: list) -> None

Writes the Eulerian path to the output file.

    Parameters:
        path (list): The Eulerian path to be written to the file.

graph_balance(self) -> dict

Calculates the balance of each node in the graph.

    Returns:
        dict: A dictionary with nodes as keys and their balance (incoming and outgoing edges) as values.

graph_cycle(self) -> None

Transforms the graph to a cycle by adding an artificial edge if necessary.
starting_node(self, walked_path: list, unused_edges: dict) -> str

Selects the starting node for walking the graph.

    Parameters:
        walked_path (list): List of nodes in the walked path.
        unused_edges (dict): Dictionary of unused edges in the graph.

    Returns:
        str: The starting node.

next_node(self, unused_edges: dict, current_node: str) -> str

Selects the next node to walk to from the current node.

    Parameters:
        unused_edges (dict): Dictionary of unused edges in the graph.
        current_node (str): The current node in the walk.

    Returns:
        str: The next node to walk to.

remove_edge(self, unused_edges: dict, walked_path: list) -> dict

Removes an edge from the graph once it has been walked.

    Parameters:
        unused_edges (dict): Dictionary of unused edges in the graph.
        walked_path (list): List of nodes in the walked path.

    Returns:
        dict: Updated dictionary of unused edges.

new_walk(self, unused_edges: dict, walked_path: list) -> tuple[dict, list]

Starts a new walk when no further path can be found from the current node.

    Parameters:
        unused_edges (dict): Dictionary of unused edges in the graph.
        walked_path (list): List of nodes in the walked path.

    Returns:
        tuple: Updated dictionary of unused edges and walked path.

walk_graph(self) -> list

Walks through the graph to find an Eulerian path.

    Returns:
        list: List of nodes representing the walked Eulerian path.

linearize_path(self, walked_path: list) -> list

Linearizes the Eulerian cycle to form the Eulerian path by removing the artificial edge.

    Parameters:
        walked_path (list): A list representing the walked path in the graph.

    Returns:
        list: A linearized path obtained by reordering segments to ensure overlap.

    Raises:
        ValueError: If the walked path cannot be split into left and right parts due to lack of overlap.

Logging

The script uses Python's logging module to provide detailed information during execution. Logs are written both to the console and to a file (eulerian_path.log). The logging setup ensures that logs are rotated to manage file sizes efficiently.
Log Levels

    DEBUG: Detailed information for diagnosing problems.
    INFO: Confirmation that things are working as expected.
    WARNING: Indications of potential issues.
    ERROR: Serious problems that prevent the program from performing some function.
    CRITICAL: Severe errors indicating that the program may be unable to continue running.

Log Configuration

The logging is configured with a rotating file handler to ensure log files do not grow indefinitely. The log format includes timestamps, log level, and the message for easy tracing.

python

import logging
from logging.handlers import RotatingFileHandler

def setup_logging(log_file='eulerian_path.log'):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    c_handler = logging.StreamHandler()
    f_handler = RotatingFileHandler(log_file, maxBytes=5*1024*1024, backupCount=2)
    c_handler.setLevel(logging.INFO)
    f_handler.setLevel(logging.DEBUG)

    c_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    f_handler.setFormatter(c_format)
    c_handler.setFormatter(c_format)

    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

setup_logging()

Example

Here is an example of how to run the script:

    Prepare your input file (input.txt):

    css

A -> B
B -> C
C -> A

Run the script:

bash

python eulerian_path_finder.py

Check the output file (output.txt) for the Eulerian path.
