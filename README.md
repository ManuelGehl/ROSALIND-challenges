# ROSALIND-challenges

<img src="https://github.com/ManuelGehl/ROSALIND-challenges/blob/main/Rosalind%20image.png?raw=true" height=300>

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

### Challenge 3: [Translating RNA into Protein](https://rosalind.info/problems/prot/)

**Description:**
The goal was to design a translator that takes an mRNA sequence as input and outputs the translated amino acid sequence.

**[Solution](https://github.com/ManuelGehl/ROSALIND-challenges/tree/main/rna-translator):**
The project uses an `RNATranslator` class. It starts by reading one RNA sequence from an input file and then uses a dictionary to map the sequence triplets to the corresponding amino acids using the standard genetic code.

### Challenge 4: [Finding a Motif in DNA](https://rosalind.info/problems/subs/)

**Description:**
The goal was to find a given DNA motif in a given DNA sequence and output the positions of the found motif.

**[Solution](https://github.com/ManuelGehl/ROSALIND-challenges/tree/main/dna-motif-finder):**
A `MotifFinder` class is used to first read the DNA sequence and the given motif. Then a window of the length of the motif is moved over the DNA sequence and the positions where the motif sequence matches the window sequence are stored and output.

### Challenge 5: [Consensus and Profile](https://rosalind.info/problems/cons/)

**Description:**
The goal was to construct a profile matrix from several given DNA sequences of equal length. Based on this profile matrix, the consensus sequence should be determined.

**[Solution](https://github.com/ManuelGehl/ROSALIND-challenges/tree/main/consensus-finder):**
A `ConsensusFinder` class is introduced that reads the sequences from a FASTA file and in a first step creates for each position in the DNA sequences a list containing the nucleotide from each sequence at that position, e.g. [Position 1] contains the first nucleotide from all DNA sequences. Then, the nucleotides for each list are simply counted and used to construct the profile matrix of the shape nucleotides x positions. From the profile matrix at each position, the most counted nucleotide is selected to build the consensus sequence.

### Challenge 6: [Finding a Protein Motif](https://rosalind.info/problems/mprt/)

**Description:**
The goal was to read Uniprot identifiers from a file and use them to access the Uniprot database and extract the protein sequences. In these sequences the N-glycosylation motif N{P}[ST]{P} should be searched for and it should be determined which of the given Uniprot entries contain the motif and at which positions.

**[Solution](https://github.com/ManuelGehl/ROSALIND-challenges/tree/main/protein-motif-finder):**
The `ProteinMotifFinder` class uses the Uniprot API to extract the protein sequences associated with the given identifiers. Then, a window of the size of the given motif is moved over each sequence and it is checked if the motif is found in this window.

### Challenge 7: [Finding a Shared Motif](https://rosalind.info/problems/lcsm/)

**Description:**
The goal was to find the longest common motif for a set of given DNA sequences.

**[Solution](https://github.com/ManuelGehl/ROSALIND-challenges/tree/main/longest-common-motif-finder):**
The `LongestCommonMotifFinder` class reads sequences from a FASTA file and sets the first sequence as a reference. It then initializes the first motif by setting the motif to the first nucleotide of the reference sequence. If this motif is found in all other sequences, it is extended by one nucleotide, including the next nucleotide from the reference sequence. However, if the motif is not found in at least one other DNA sequence, the start position in the reference sequence is shifted downstream by 1 nucleotide and the process starts over. The current motif length is saved, and if it is at least as long as any motif before it, it is saved. In effect, the longest motif is stored and output.

### Challenge 8: [Locating Restriction Sites](https://rosalind.info/problems/revp/)

**Description:**
The challenge was to read a DNA string in fasta format and find all reverse palindromic motifs from size 4 to size 12.

**[Solution](https://github.com/ManuelGehl/ROSALIND-challenges/tree/main/restriction-site-finder):**
The `RestrictionSiteFinder` class reads a sequence from a FASTA file and creates all possible substrings of size 4 to 12 with a step size of 1 and stores them together with their starting position in the DNA sequence. These substrings are then converted to their reverse complementary sequences and checked to see if they occur in the DNA sequence. If they do, the start position and length of the substring are written to a file.

### Challenge 9: [Calculating Protein Mass](https://rosalind.info/problems/prtm/)

**Description:**
The aim was to calculate the monoisotopic mass of a peptide given as a string.

**[Solution](https://github.com/ManuelGehl/ROSALIND-challenges/tree/main/monoisotopic-mass-calculator):**
The `MonoisotopicMassCalculator` class reads an amino acid sequence from an input file and maps the monoisotopic mass to all characters in the sequence.

### Challenge 10: [Open Reading Frames](https://rosalind.info/problems/orf/)

**Description:**
The problem was to find all unique candidate protein sequences that can be translated from the open reading frames (ORFs) of a given DNA string. The DNA string was provided in FASTA format and can be up to 1 kbp in length. An ORF begins at the start codon and ends at a stop codon with no other stop codons in between.

**[Solution](https://github.com/ManuelGehl/ROSALIND-challenges/tree/main/ORF-finder):**
The `ORFFinder` class is designed to identify Open Reading Frames (ORFs) in DNA sequences. After converting the DNA sequence to its reverse complement sequence, both sequences are used to generate all possible frames (6 in total). For each frame, the positions of the start and stop codons are determined. The start and stop positions are iterated over to determine which combinations of start and stop positions satisfy both that the stop position is greater than the start position and that no other stop position lies between them.

### Challenge 11: [RNA-Splicer](https://rosalind.info/problems/splc/)

**Description:**
Several DNA strings in FASTA format were provided, with the first string considered as the DNA sequence and the subsequent ones as introns. The task involved returning a protein string obtained by transcribing and translating only the exons of the DNA sequence.Several DNA strings in FASTA format were provided, with the first string considered as the DNA sequence and the subsequent ones as introns. The task involved returning a protein string obtained by transcribing and translating only the exons of the DNA sequence.

**[Solution](https://github.com/ManuelGehl/ROSALIND-challenges/tree/main/RNA_splicer):**
The script is a Python program designed to process DNA sequences in FASTA format by splicing introns and mapping the resulting DNA sequence to a protein sequence using codon mapping. It utilizes a class named `RNASplicer`, where the `splice_sequence` method removes introns from the raw DNA sequence, and the `express` method maps the spliced DNA sequence to a protein sequence using codon mapping in "DNA" mode.

### Challenge 12: [Finding a Spliced Motif](https://rosalind.info/problems/sseq/)

### Challenge 13: [Calculating Expected Offspring](https://rosalind.info/problems/iev/)

### Challenge 14: [Overlap Graphs](https://rosalind.info/problems/grph/)

### Challenge 15: [Enumerating Gene Orders](https://rosalind.info/problems/perm/)

### Challenge 16: [Transitions and Transversions](https://rosalind.info/problems/tran/)

### Challenge 17: [Genome Assembly as Shortest Superstring ](https://rosalind.info/problems/long/)

## Credits
- Author: Manuel Gehl
- ROSALIND: http://rosalind.info/

## License

This project is licensed under the MIT License.
