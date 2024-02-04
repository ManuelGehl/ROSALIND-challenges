# RNASplicer
## Overview

`RNASplicer` is a Python class designed for splicing DNA sequences by removing introns and mapping them to protein sequences. 
This tool provides a straightforward way to process genetic data stored in FASTA format and generate corresponding protein sequences using codon mapping.

## Usage

To use the `RNASplicer` class, follow these steps:


Additionally, a `main` function is provided as an example pipeline. Running the script will execute this pipeline.

```bash

python RNA_splicer.py
```
## Class Structure

**Attributes:**

`DEFAULT_INPUT_PATH (str)`: Default path to the input data file.

`DEFAULT_OUTPUT_PATH (str)`: Default path to the output result file.

`input_path (str)`: Path to the input data file.

`output_path (str)`: Path to the output result file.

`raw_sequence (str)`: Raw DNA sequence.

`introns (list)`: List of introns to be removed from the sequence.

`spliced_seq (str)`: DNA sequence after splicing.

`protein_seq (str)`: Protein sequence mapped from the spliced DNA.

**Constants:**

`DEFAULT_INPUT_PATH (str)`: Default path to the input data file.

`DEFAULT_OUTPUT_PATH (str)`: Default path to the output result file.

**Methods:**

`__init__(self, input_path: str = None, output_path: str = None) -> None`: Initializes a RNASplicer object with optional custom input and output paths.

`read_sequence(self) -> None`: Reads a sequence from the specified input file in FASTA format.

`splice_sequence(self) -> None`: Splices the raw DNA sequence by removing introns.

`express(self) -> None`: Maps the spliced DNA sequence to a protein sequence using codon mapping.

`write_result(self) -> None`: Writes the protein sequence to the specified output file.

**Main Function:**
The `main()` function executes the RNASplicer class operations in the following sequence:

1. Initialize `RNASplicer` object.
2. Read DNA sequence from the input file.
3. Splice the sequence by removing introns.
4. Map the spliced DNA sequence to a protein sequence.
5. Write the resulting protein sequence to the output file.
