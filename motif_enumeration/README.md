# motif_enumeration

This repository provides a Python implementation to identify (k,d)-motifs in a collection of DNA sequences. A (k,d)-motif is a k-mer that appears in every sequence within the collection with at most d mismatches.
This class, `MotifEnumeration`, is designed to solve this problem efficiently by leveraging a dictionary and neighborhood generation.

## Usage

To use the `MotifEnumeration class`, you must provide an input file that contains k (length of k-mers) and d (maximum allowed mismatches) as the first row and the DNA sequences as the other rows.

### Class: MotifEnumeration
### Attributes
- `input_path` (str): Path to the input file.
- `sequences` (list): List of DNA sequences.
- `k_size` (int): Size of the k-mers.
- `distance` (int): Maximum Hamming distance.
- `neighbourhood` (dict): Dictionary of sequences and their k-mers.
- `motifs` (list): List of found motifs.

### Methods
- `__init__(self, input_path=None)`: Initializes the MotifEnumeration object with a default or provided input path.
- `input(self)`: Reads the input file and parses the k-size, distance, and DNA sequences.
- `create_k_mers(self)`: Creates k-mers for each sequence and stores them in a dictionary.
- `create_neighbours(self)`: Creates the d-neighbourhood for each k-mer and updates the neighbourhood dictionary using the generate_d_neighbourhood function from the `functions.neighbourhood module`.
- `find_motif(self)`: Finds motifs that appear in all sequences by counting occurrences in the neighbourhood pool.
