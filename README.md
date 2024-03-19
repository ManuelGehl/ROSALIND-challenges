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

**Description:**
In this task, we aim to find the indices in a DNA string where another DNA string's symbols appear as a subsequence. This involves comparing the symbols of both strings and recording indices where matches occur.

**[Solution](https://github.com/ManuelGehl/ROSALIND-challenges/tree/main/spliced_motif_finder):**
The script defines a class, SplicedMotifFinder, to identify a spliced motif within a DNA sequence. It reads the sequence from a FASTA file, generates position lists for each character in the motif, finds the spliced motif based on these lists, and writes the result to an output file. The main function executes these methods in sequence.

### Challenge 13: [Calculating Expected Offspring](https://rosalind.info/problems/iev/)

**Description:**
This task involves computing the expected number of offspring with a dominant phenotype in the next generation, given six integers representing the number of couples with specific genotype pairings.

**[Solution](https://github.com/ManuelGehl/ROSALIND-challenges/tree/main/expected_offspring_calculator)**
This script calculates the expected number of offspring displaying the dominant phenotype in the next generation based on given genotype pairings and predefined pairing probabilities.

### Challenge 14: [Overlap Graphs](https://rosalind.info/problems/grph/)

**Description:**
This task involves generating the adjacency list for an overlap graph based on a collection of DNA strings. In an overlap graph, each string corresponds to a node, and a directed edge exists between two nodes if there is an overlap between a length-k suffix of one string and a length-k prefix of another string. The goal is to create an adjacency list representing this graph, specifically for a length-k value of 3.

**[Solution](https://github.com/ManuelGehl/ROSALIND-challenges/tree/main/prefix_suffix_graph)**
The script reads DNA sequences from an input file and creates k-mers (prefixes and suffixes) for each DNA sequence using a specified k-mer length. It constructs an adjacency list representing the overlap relationships between DNA sequences based on their prefixes and suffixes. If the suffix of one sequence matches the prefix of another sequence, they are considered adjacent.

### Challenge 15: [Enumerating Gene Orders](https://rosalind.info/problems/perm/)

**Description:**
This task involves calculating the total number of permutations of length n, where n is a positive integer not exceeding 7. Additionally, we need to generate a list of all such permutations.

**[Solution](https://github.com/ManuelGehl/ROSALIND-challenges/tree/main/enumerating_gene_orders)**
The script takes user input for the number of genes for permutation, ensuring that the input is between 1 and 7 and calculates the total number of permutations using the factorial formula.

### Challenge 16: [Transitions and Transversions](https://rosalind.info/problems/tran/)

**Description:**
This task involves calculating the transition/transversion ratio for two DNA strings of equal length.

**[Solution](https://github.com/ManuelGehl/ROSALIND-challenges/tree/main/transition_transversion_ratio)**
The transition/transversion ratio for two DNA sequences is calculated by comparing corresponding bases in the two sequences to count the number of transitions (purine to purine or pyrimidine to pyrimidine) and transversions (purine to pyrimidine or vice versa) using the `count_transitions_transversions` method. The transition/transversion ratio is computed by dividing the number of transitions by the number of transversions.

### Challenge 17: [Find Patterns Forming Clumps in a Strings](https://rosalind.info/problems/ba1e/)

**Description:**
The Clump Finding Problem involves identifying patterns within a string Genome. A pattern forms an (L, t)-clump within Genome if it appears at least t times in a contiguous interval of length L. The task is to find all distinct k-mers that form (L, t)-clumps within a Genome.


**[Solution](https://github.com/ManuelGehl/ROSALIND-challenges/tree/main/patterns_forming_clumps)**
Key functions include `pattern_frequency` and `pattern_count`, which determine pattern frequencies and count occurrences within the sequence, respectively. Another function, `filter_frequencies`, selects patterns meeting a specified occurrence threshold.

The core function,`find_clumps`, identifies clumped patterns in the sequence based on filtered pattern frequencies. It slides over the sequence, counting occurrences of each pattern within a window, and only includes patterns meeting the occurrence criteria.

### Challenge 18: [Genome Assembly as Shortest Superstring ](https://rosalind.info/problems/long/)

**Description:**
This task involves finding the shortest superstring that contains all the given DNA strings.
To solve this, we need to reconstruct the chromosome by merging pairs of strings that overlap by more than half their length.

**[Solution](https://github.com/ManuelGehl/ROSALIND-challenges/tree/main/genome_assembly):**
The script performs genome assembly using a suffix matrix approach. It first reads the DNA sequences and calculates a suffix matrix to determine the maximum overlapping substrings between all sequences. The suffix_matrix method computes the suffix score, representing the maximum overlapping nucleotides between the 3' end of one sequence and the 5' end of another.

The sequence to be placed at the 3' end is identified based on the lowest sum of passed suffix scores. The assembly process iteratively fuses sequences based on their overlapping suffixes and prefixes. It starts with the terminus sequence and proceeds to merge sequences until a complete genome is assembled.

## Credits
- Author: Manuel Gehl
- ROSALIND: http://rosalind.info/

## License

This project is licensed under the MIT License.
