# MotifFinder

The MotifFinder class is a Python script designed for finding a motif within a given DNA sequence. 
It provides a simple and efficient way to identify the starting positions of a specified motif in a DNA sequence and save the results to an output file.

## Input

The script takes input from a file (default: data.txt) which should contain two lines:
- The DNA sequence.
- The motif to be found in the DNA sequence.

## Output

The script outputs the starting positions of the motif in the DNA sequence to a file (default: result.txt).

## MotifFinder Class
### Initialization

```python
motif_finder = MotifFinder(input_path="data.txt", output_path="result.txt")
```

You can customize the input and output file paths during initialization.

### Reading Sequence

```python
motif_finder.read_sequence()
```

Reads the DNA sequence and motif from the specified input file.

### Finding Motif

```python
motif_finder.find_motif()
```

Identifies the starting positions of the motif in the DNA sequence.

### Writing Positions

```python
motif_finder.write_positions()
```

Writes the identified positions to the specified output file.

### Running the Script

```python
if __name__ == "__main__":
    main()
```
Executes the MotifFinder script, reading the sequence, finding the motif, and writing the positions to the output file.
