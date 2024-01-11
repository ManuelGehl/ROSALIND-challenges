# Monoisotopic Mass Calculator

A Python class for calculating the monoisotopic mass of a peptide sequences.
**Important:** The script is designed for peptides in the context of mass spectrometry, i.e. without full N- and C-terminus. The peptides are considered to be excised from the middle of the protein.

## Overview

The `MonoisotopicMassCalculator` class provides a simple way to calculate the monoisotopic mass of a peptide sequence. 
The monoisotopic mass is calculated based on the weights of individual amino acids in the peptide.

## Usage

To use this calculator, create an instance of the `MonoisotopicMassCalculator` class and call its methods in the following sequence:

1. `read_sequence()`: Read the peptide sequence from the input file.
2. `calculate_mass()`: Calculate the monoisotopic mass of the peptide sequence.
3. `write_result()`: Write the calculated mass to the output file.

The default input and output file paths are set to "data.txt" and "result.txt," respectively. 
You can provide custom paths during the initialization of the calculator.

```python
calculator = MonoisotopicMassCalculator(input_path="custom_input.txt", output_path="custom_output.txt")
calculator.read_sequence()
calculator.calculate_mass()
calculator.write_result()
```

Alternatively, the script can be executed:

```bash
python monoisotopic-mass-calculator.py
```

### Input

The input file should contain a single-line peptide sequence.
Amino acid residues are represented by their one-letter codes (e.g., "MDGHK").

### Output

The calculated monoisotopic mass will be written to the specified output file. The result is rounded to three decimal places.
