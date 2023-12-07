# DNA GC Content Measurer

## Overview

This Python script measures the GC content in DNA sequences and identifies the sequence with the highest GC content. 
It reads DNA sequences from an input file in FASTA format, calculates the GC content for each sequence, evaluates and identifies the sequence with the highest GC content, and writes the results to an output file.

## Features

- **Read DNA Sequences:** The script reads DNA sequences from an input file (default: `data.txt`).

- **Measure GC Content:** For each DNA sequence, the script calculates the GC content as a percentage.

- **Identify Highest GC Content:** The script identifies the DNA sequence with the highest GC content.

- **Output Result:** The results, including the ID and GC content of the sequence with the highest GC content, are written to an output file (default: `result.txt`).

## Usage

1. Install Python if not already installed: [Python Installation Guide](https://www.python.org/downloads/)

2. Clone the repository:

   ```bash
   git clone https://github.com/ManuelGehl/ROSALIND-challenges/dna-gc-content-measurer/dna-gc-content-measurer.git
   ```
3. Navigate to the project directory:

   ```bash
   cd dna-gc-content-measurer
   ```
4. Run the script:

```bash

python dna_gc_measurer.py
```

5. Check the results in the output file (result.txt by default).

**Customization**

- Input File: You can specify a different input file by modifying the input_path parameter in the script.

- Output File: You can specify a different output file by modifying the output_path parameter in the script.

**Dependencies**

- Python 3.11.5

**Credits**

- Author: Manuel Gehl

**License**

This project is licensed under the MIT License.
