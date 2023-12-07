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

**Solution:** 

The script defines a `GCMeasurer` class that reads DNA sequences from a FASTA file, measures their GC content, and writes the sequence ID with the highest GC content to an output file. 
It stores the IDs from the header and the corresponding sequences in a dictionary. From this, the GC content (occurrence of the letters "G" and "C" in the DNA sequence (string) relative to its length) is calculated and stored in another dictionary with the corresponding IDs as keys. This dictionary is then sorted by its values and the highest value is written together with its ID to a txt file.


## Credits
- Author: Manuel Gehl
- ROSALIND: http://rosalind.info/

## License

This project is licensed under the MIT License.
