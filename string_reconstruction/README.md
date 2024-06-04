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
