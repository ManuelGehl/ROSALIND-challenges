# ConsensusFinder

The ConsensusFinder class is a Python script designed for reading multiple DNA sequences from a FASTA file, computing the profile matrix, and determining the consensus sequence. 
It provides a comprehensive analysis of a set of DNA sequences, summarizing the most prevalent nucleotide at each position and generating a consensus sequence.

## Usage

### Initialization

```python
consensus_finder = ConsensusFinder(input_path="data.txt", output_path="result.txt")
```

You can customize the input and output file paths during initialization.

### Reading Sequences

```python
consensus_finder.read_sequence()
```

Reads DNA sequences from the specified FASTA file.

### Computing Profile Matrix

```python
consensus_finder.profile_matrix()
```

Computes the profile matrix, representing the frequency of each nucleotide (A, C, G, T) at each position in the sequences.

### Computing Consensus Sequence

```python
consensus_finder.consensus()
```

Determines the consensus sequence from the computed profile matrix.

### Writing Results

```python
consensus_finder.write_results()
```

Writes the consensus sequence and profile matrix to the specified output file.
