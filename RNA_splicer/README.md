# RNASplicer
## Overview

`RNASplicer` is a Python class designed for splicing DNA sequences by removing introns and mapping them to protein sequences. 
This tool provides a straightforward way to process genetic data stored in FASTA format and generate corresponding protein sequences using codon mapping.

## Usage

To use the `RNASplicer` class, follow these steps:
- Instantiate an `ORFFinder` object.
- Optionally, specify custom input and output paths during instantiation.
- Call the `read_sequence` method to read the DNA sequence from the input file.
- Call the `transform_sequence` method to transform the DNA sequence into its reverse complement.
- Call the `generate_reading_frames` method to create reading frames for both forward and reverse strands.
- Call the `find_start` and `find_stop` methods to identify start and stop codons in each reading frame.
- Call the `find_orf` method to find ORFs in each reading frame and store their positions.
- Call the `translate_orf` method to translate identified ORFs into protein sequences.
- Optionally, call the `remove_duplicates` method to remove duplicate protein sequences.
- Call the `write_result` method to write the translated ORF protein sequences to an output file.

Additionally, a `main` function is provided as an example pipeline for ORF analysis. Running the script will execute this pipeline.

```python

python ORF_finder.py
```
## Class Structure

**Attributes:**

- `DEFAULT_INPUT_PATH`: Default path for the input data file.
- `DEFAULT_OUTPUT_PATH`: Default path for the output result file.
- `START_CODON`: Start codon used to identify the beginning of ORFs.
- `STOP_CODONS`: List of stop codons to identify the end of ORFs.
- `input_path`: Path to the input data file.
- `output_path`: Path to the output result file.
- `raw_sequence`: Raw DNA sequence read from the input file.
- `rev_complement`: Reverse complement of the raw DNA sequence.
- `sequences`: Dictionary to store sequence names and their respective DNA sequences.
- `start_dictionary`: Dictionary to store start codon positions for each sequence.
- `stop_dictionary`: Dictionary to store stop codon positions for each sequence.
- `orf_positions`: Dictionary to store ORF positions for each sequence.
- `translated_orf`: List to store translated protein sequences from identified ORFs.

**Constants:**

- `DEFAULT_INPUT_PATH`: "data.txt"
- `DEFAULT_OUTPUT_PATH`: "result.txt"
- `START_CODON`: "ATG"
- `STOP_CODONS`: ["TAG", "TGA", "TAA"]

**Methods:**

- `__init__(self, input_path: str = None, output_path: str = None) -> None:` Initializes an ORFFinder object with optional custom input and output paths.
- `read_sequence(self) -> None:` Reads a sequence from the specified input file in FASTA format.
- `transform_sequence(self) -> None:` Transforms the DNA sequence into its reverse complement.
- `generate_reading_frames(self) -> None:` Generates reading frames for both forward and reverse strands.
- `find_start(self) -> None:` Finds start codon positions in each reading frame.
- `find_stop(self) -> None:` Finds stop codon positions in each reading frame.
- `find_orf(self) -> None:` Finds Open Reading Frames (ORFs) in each reading frame and stores their positions.
- `translate_orf(self) -> None:` Translates ORFs into amino acid sequences using codon mapping.
- `remove_duplicates(self) -> None:` Removes duplicate protein sequences from the translated ORF list.
- `write_result(self) -> None:` Writes translated ORF protein sequences to a specified output file.

**Main Function:**

The main function provides an example pipeline for executing the ORF analysis. 
It creates an instance of the `ORFFinder` class, reads the DNA sequence from the input file, transforms the sequence, generates reading frames, identifies start and stop codons, finds ORFs, translates ORFs into protein sequences, removes duplicates, and writes the results to the output file.

```python
# Main function workflow
orf_finder = ORFFinder()
orf_finder.read_sequence()
orf_finder.transform_sequence()
orf_finder.generate_reading_frames()
orf_finder.find_start()
orf_finder.find_stop()
orf_finder.find_orf()
orf_finder.translate_orf()
orf_finder.remove_duplicates()
orf_finder.write_result()
```
