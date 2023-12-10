# ROSALIND-challenges

## Overview

This repository contains my solutions to various bioinformatics challenges from [ROSALIND](http://rosalind.info/). 
Each subdirectory represents a specific ROSALIND problem that I found particularly interesting at the time of solving it.

## ROSALIND Profile

Visit my [ROSALIND profile](https://rosalind.info/users/ManuelGehl/) to track my progress and view additional information.

## List of Challenges

### Challenge 1: [Computing GC Content](https://rosalind.info/problems/gc/)

**Description:** 
The task involves analyzing DNA strings in FASTA format to determine the string with the highest GC-content. The goal is to identify and return the ID of the DNA string with the highest GC-content, along with the corresponding GC-content value.

**[Solution](https://github.com/ManuelGehl/ROSALIND-challenges/tree/main/dna-gc-content-measurer):** 
The script defines a `GCMeasurer` class that reads DNA sequences from a FASTA file, measures their GC content, and writes the sequence ID with the highest GC content to an output file. 
It stores the IDs from the header and the corresponding sequences in a dictionary. From this, the GC content (occurrence of the letters "G" and "C" in the DNA sequence (string) relative to its length) is calculated and stored in another dictionary with the corresponding IDs as keys. This dictionary is then sorted by its values and the highest value is written together with its ID to a txt file.

### Challenge 2: [Hamming distance](https://rosalind.info/problems/hamm/)

**Description:**
The DNA Mutation Measurer project focuses on calculating the Hamming distance between two DNA sequences provided in a file. The Hamming distance is a metric that quantifies the dissimilarity between two strings of equal length, representing the number of differing positions.

**[Solution](https://github.com/ManuelGehl/ROSALIND-challenges/tree/main/hamming-distance-measurer):**
The project introduces a `MutationMeasurer` class to handle the process. It begins by reading DNA sequences from an input file, ensuring the presence of at least two sequences. The Hamming distance is then computed by comparing corresponding positions in the two sequences. The result is displayed as the number of differing positions.

### Challenge 3: [Translating RNA into Protein ](https://rosalind.info/problems/prot/)

**Description:**
The goal was to design a translator that takes an mRNA sequence as input and outputs the translated amino acid sequence.

**[Solution](https://github.com/ManuelGehl/ROSALIND-challenges/tree/main/rna-translator):**
The project uses an `RNATranslator` class. It starts by reading one RNA sequence from an input file and then uses a dictionary to map the sequence triplets to the corresponding amino acids using the standard genetic code.

## Credits
- Author: Manuel Gehl
- ROSALIND: http://rosalind.info/

## License

This project is licensed under the MIT License.
