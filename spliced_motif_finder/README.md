# Spliced Motif Finder

This Python script is designed to find a spliced motif in a given sequence. A spliced motif is a substring that appears in the sequence but may have characters missing at various positions. 
The program takes input data in FASTA format, where the first sequence is considered the main sequence, and the second sequence is treated as the motif.

## Usage

**Input File:** The input file should be in FASTA format with at least two sequences. The default input file is data.txt, but you can provide a custom input file using the optional `input_path` parameter during object initialization.

**Output File:** The spliced motif positions will be written to the output file, which is named result.txt by default. You can specify a custom output file using the optional `output_path` parameter during object initialization.

**Execution:** The main function, `main()`, creates an instance of the `SplicedMotifFinder` class, reads the sequence from the input file, generates position lists for each character in the motif, finds the spliced motif based on the generated position lists, and finally, writes the result to the output file.

## How It Works

**Initialization:** The `SplicedMotifFinder` class is initialized with optional custom input and output paths. If not provided, default paths are used.

**Reading Sequence:** The `read_sequence` method reads the sequences from the input file and stores the main sequence in the sequence attribute and the motif in the motif attribute.

**Generating Positions:** The `generate_positions` method generates a list of position lists for each character in the motif, indicating the positions where that character appears in the sequence.

**Finding Spliced Motif:** The `find_spliced_motif` method processes the generated position lists to find the spliced motif. It considers positions sequentially and selects the first position for each motif character that is greater than the last position of the previous character.

**Writing Result:** The `write_result` method writes the identified spliced motif positions to the output file.

## Example

```python

# Example usage
spliced_motif_finder = SplicedMotifFinder(input_path="custom_data.txt", output_path="custom_result.txt")
spliced_motif_finder.read_sequence()
pos_lists = spliced_motif_finder.generate_positions()
spliced_motif_finder.find_spliced_motif(pos_lists=pos_lists)
spliced_motif_finder.write_result()
```

## Dependencies

This script depends on helper functions for reading FASTA files, which can be found in the [Codetoolbox](https://github.com/ManuelGehl/CodeToolbox) repository.
