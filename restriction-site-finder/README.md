# Restriction Site Finder

## Overview

The Restriction Site Finder is a Python script designed to read DNA sequences from a FASTA file, generate substrings, identify palindromic DNA sequences, and write the results to an output file.

## Requirements

- Python 3.12.0
- Dependencies:
    - os
    - sys
    - read_fasta from [fasta_reader](https://github.com/ManuelGehl/CodeToolbox/blob/main/fasta_reader.py)

## Usage

Execute the script:

```bash

    python restriction-site-finder.py

    [Optional: Specify input and output files]
```

## Script Structure

### Classes

`RestrictionSiteFinder`

#### Methods

`read_sequence()`: Read DNA sequences from a FASTA file.

`create_substrings()`: Generate substrings from the DNA sequence.

`find_palindrom()`: Check for palindromic DNA substrings.

`write_result()`: Write palindromic results to an output file.

`reverse_complement(sequence: str) -> str`: Compute the reverse complement of a DNA sequence.

#### Class Constants

`DEFAULT_INPUT_PATH`: Default input file path if not provided during instance creation.

`DEFAULT_OUTPUT_PATH`: Default output file path if not provided during instance creation.
