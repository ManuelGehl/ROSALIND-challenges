# Expected Offspring Calculator

## Overview

This Python script calculates the expected number of offspring displaying the dominant phenotype in the next generation, based on the genotype pairings of a population. 
The program assumes that every couple has exactly two offspring.

## Usage

1. **Input Data:**
   - Create or provide an input file (`data.txt`) with six non-negative integers, each representing the number of couples possessing a specific genotype pairing. The genotypes are as follows:
      - "AA-AA"
      - "AA-Aa"
      - "AA-aa"
      - "Aa-Aa"
      - "Aa-aa"
      - "aa-aa"
   
2. **Run the Script:**
   - Execute the script (`expected_offspring.py`) to read the input data, perform calculations, and write the result to an output file (`result.txt`).
  
```bash
python expected_offspring.py
```

## Configuration

Default input file path: `data.txt`

Default output file path: `result.txt`

## Customization

You can customize the input and output file paths by providing optional arguments when creating an instance of the ExpectedOffspring class.

```python
offspring = ExpectedOffspring(input_path="custom_input.txt", output_path="custom_output.txt")
```

## Class Constants

`DEFAULT_INPUT_PATH`: Default path for the input file.

`DEFAULT_OUTPUT_PATH`: Default path for the output file.

`PAIRING_PROBABILITIES`: Probabilities for each genotype pairing.

## Class Methods

`read_data`: Reads genotype pair counts from the input file.

`calculate_offspring`: Calculates the expected number of offspring displaying the dominant phenotype.

`write_result`: Writes the calculated result to the output file.
