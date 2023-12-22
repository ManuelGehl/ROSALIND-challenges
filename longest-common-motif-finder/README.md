# Longest Common Motif Finder

The Longest Common Motif Finder is a Python script designed to find the longest common motif among a collection of DNA sequences provided in a FASTA file. 
The script utilizes a class-based approach to encapsulate the motif-finding logic and provides flexibility by allowing users to specify input and output file paths.

## Usage

To find the longest common motif, follow these steps:

1. Ensure you have a FASTA file containing DNA sequences. The default input file path is set to "data.txt", but you can specify a different file by providing the input_path parameter when creating an instance of the LongestCommonMotifFinder class.

2. Run the script by executing the following command in your terminal:

    ```bash
    longest-common-motif-finder.py
    ```

3. The script will output the longest common motif found among the provided DNA sequences to the specified output file. The default output file path is set to "result.txt", but you can specify a different file by providing the output_path parameter when creating an instance of the LongestCommonMotifFinder class.

## Class Overview LongestCommonMotifFinder Class
### Attributes

- `DEFAULT_INPUT_PATH` (str): Default path to the input file containing DNA sequences.
- `DEFAULT_OUTPUT_PATH` (str): Default path to the output file for storing the result.
- `START_POSITION` (int): Default start position for extracting motifs from sequences.
- `END_POSITION` (int): Default end position for extracting motifs from sequences.
- `LOOP_TOGGLE` (bool): Default loop toggle to control motif extraction process.
- `input_path` (str): Path to the input FASTA file containing DNA sequences.
- `output_path` (str): Path to the output file for storing the longest common motif.
- `dna_sequences` (list): Contains DNA strings read from FASTA.
- `reference_seq` (str): Per default first DNA sequence from FASTA file.
- `current_motif` (str): Current motif being evaluated during the search process.
- `longest_motif` (str): Longest common motif found among all sequences.
- `start_pos` (int): Current start position for motif extraction.
- `end_pos` (int): Current end position for motif extraction.
- `loop_toggle` (bool): Toggle to control the loop for motif extraction.

### Methods
- `__init__(self, input_path=None, output_path=None)`: Initializes the LongestCommonMotifFinder instance.
- `read_sequence(self)`: Reads DNA sequences from the input FASTA file.
- `initialize_motif(self)`: Initializes the motif extraction process by setting the current motif to the first nucleotide of the reference sequence.
- `check_motif(self)`: Checks if the current motif is present in all DNA sequences and updates the longest motif if needed. Calls methods to extend or shift the motif.
- `extend_motif(self)`: Extends the current motif by one nucleotide if the current motif was found in all DNA sequences.
- `shift_motif(self)`: Shifts the current motif by one nucleotide to the right if the current motif was NOT found in all DNA sequences.
- `write_result(self)`: Writes the longest common motif to the output file.

## Example Usage

```python
from longest_common_motif_finder import LongestCommonMotifFinder

# Create an instance of LongestCommonMotifFinder with custom input and output paths
motif_finder = LongestCommonMotifFinder(input_path="path/to/custom.fasta", output_path="path/to/custom_output.txt")

# Read DNA sequences from the input FASTA file
motif_finder.read_sequence()

# Initialize the motif extraction process
motif_finder.initialize_motif()

# Continue motif extraction until the loop toggle is False
while motif_finder.loop_toggle:
    motif_finder.check_motif()
```
