# RNATranslator

## Overview

The RNATranslator script is designed to translate mRNA sequences into protein sequences using a predefined codon table. 
The resulting protein sequence is then saved to an output file.

## Usage
### Initialization

```python
# Default initialization with input and output file paths
rna_translator = RNATranslator()

# Custom initialization with specified input and output file paths
rna_translator = RNATranslator(input_path="custom_input.txt", output_path="custom_output.txt")
```

### Reading mRNA Sequence

```python
# Read the mRNA sequence from the input file
rna_translator.read_rna()
```

### Translating mRNA Sequence

```python
# Translate the mRNA sequence into a protein sequence
rna_translator.translate()
```
### Writing Protein Sequence

```python
# Write the protein sequence to the output file
rna_translator.write_sequence()
```
## Usage as script

The usage as script will perform the above pipeline.

```bash
python RNA-translator.py
```
