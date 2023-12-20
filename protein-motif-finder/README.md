# ProteinMotifFinder

The ProteinMotifFinder class is a Python script designed for reading Uniprot Identifiers from a text file, accessing protein sequences from the Uniprot database, and searching for a specific N-glycosylation motif (N{P}[ST]{P}) in these sequences. 
It provides a useful tool for identifying potential N-glycosylation sites in a set of proteins.

## Usage
### Initialization

```python
glycosylation_finder = ProteinMotifFinder(input_path="data.txt", output_path="result.txt")
```

You can customize the input and output file paths during initialization.

### Reading Identifiers

```python
glycosylation_finder.read_identifiers()
```

Reads Uniprot identifiers from the specified input file.

### Getting Protein Sequences

```python
glycosylation_finder.get_sequence()
```

Uses Uniprot IDs to retrieve protein sequences from the Uniprot database.

### Finding N-Glycosylation Motif

```python
glycosylation_finder.find_motif()
```

Searches for the N-glycosylation motif in the protein sequences.

### Writing Results

```python
glycosylation_finder.write_results()
```

Writes the results (Uniprot accessions and corresponding starting positions of the motif) to the specified output file.
