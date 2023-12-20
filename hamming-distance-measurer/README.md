# MutationMeasurer

## Overview

The DNA Mutation Measurer is a Python script that measures the Hamming distance between two DNA sequences read from a file. 
The Hamming distance is the number of positions at which corresponding symbols (characters) are different between the two sequences. 
This project includes a `MutationMeasurer` class with methods to read sequences from a file and calculate the Hamming distance.

## Usage

The script accepts a text file ("data.txt") with two simple DNA (or RNA) sequences in each line.
It then simply prints out the Hamming distance for that pair of sequences as it runs.

### Initialization

```python
measurer = MutationMeasurer(input_path="data.txt")
```

You can customize the input file path during initialization.
### Reading Sequences

```python
measurer.read_sequence()
```

Reads two DNA sequences from the specified input file.

### Measuring Hamming Distance

```python
measurer.hamming_distance()
```

Measures the Hamming distance between the two sequences and prints the result.

### Running the Script

```python
if __name__ == "__main__":
    main()
```

Executes the MutationMeasurer script, reading sequences from the input file, measuring the Hamming distance, and printing the result.
