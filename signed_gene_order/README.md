# Permutation List Generator

## Overview
This Python script generates all possible permutations of genes based on user input. It takes a number representing the number of genes for permutation and generates all possible permutations of these genes. The results are then printed to a file named "results.txt".

## Script Details

### `PermutationList` Class
- Represents a permutation list.
- Attributes:
  - `input_n`: The number of genes for permutation.
  - `genes`: The stock of available numbers for permutations.
  - `results`: The generated permutations.
- Methods:
  - `__init__()`: Initializes a `PermutationList` object with default values.
  - `input()`: Takes user input for the number of genes for permutation.
  - `next_gene(partial_sequence)`: Generates possible next gene sequences based on the given partial sequence.
  - `generate_permutations()`: Generates all possible permutations of genes based on the number of genes specified.
  - `print_results()`: Prints the generated permutations to a file named "results.txt".

### `main()` Function
- Orchestrates the process of generating permutations and printing results.
