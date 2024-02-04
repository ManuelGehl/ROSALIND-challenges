# Prefix-Suffix Graph for DNA Sequences

This repository contains a Python script implementing a Prefix-Suffix Graph algorithm for a collection of DNA sequences. 
The script reads DNA sequences in FASTA format from an input file, creates k-mers (prefixes and suffixes) for each sequence, and generates an adjacency list representing the overlap relationships between DNA sequences. 
The resulting graph is then written to an output file.

## Usage

### Input File Format

The input file should contain DNA sequences in FASTA format. Example:

```plaintext
>sequence1
ATCGATCGATCG
>sequence2
CGATCGATCGAT
>sequence3
GATCGATCGATC
```

### Output File Format

The output file contains lines representing overlap relationships between sequences. Each line consists of two sequence IDs separated by a space. Example:

```plaintext
sequence1 sequence2
sequence2 sequence3
```

## Class Documentation

### Methods

`__init__(self, input_path: str = None, output_path:str = None) -> None`: Initialize the PrefixSuffixGraph object.

`read_sequences(self) -> Dict[str, str]`: Read DNA sequences from the input file in FASTA format.

`create_k_mers(self, seq_dict: Dict[str, str]) -> Tuple[Dict[str, str], Dict[str, str]]`: Create k-mers (prefixes and suffixes) for each DNA sequence.

`create_adjacency_list(self, prefix_dict: Dict[str, str], suffix_dict: Dict[str, str]) -> Dict[str, list]`: Create an adjacency list representing the overlap relationships between DNA sequences.

`write_results(self, adj_list: Dict[str, list]) -> None`: Write the adjacency list to the output file.

### Example Usage

```python
from Utility.fasta_reader import read_fasta
from prefix_suffix_graph import PrefixSuffixGraph

# Create PrefixSuffixGraph instance
overlap_graphs = PrefixSuffixGraph(input_path="custom_input.txt", output_path="custom_output.txt")

# Read DNA sequences
seq_dict = overlap_graphs.read_sequences()

# Create k-mers
prefix_dict, suffix_dict = overlap_graphs.create_k_mers(seq_dict)

# Create adjacency list
adjacency_list = overlap_graphs.create_adjacency_list(prefix_dict, suffix_dict)

# Write results to output file
overlap_graphs.write_results(adjacency_list)
```
