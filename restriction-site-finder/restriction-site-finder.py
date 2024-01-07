# Import FASTA reading function
import sys
import os
from typing import Tuple

# Adding the path to the Utility directory to sys.path
sys.path.append("../Utility")
# Importing the read_fasta function from fasta_utils module
from fasta_utils import read_fasta

class RestrictionSiteFinder:
    """
    A class for finding palindromic DNA substrings and writing the results to an output file.

    Attributes:
        DEFAULT_INPUT_PATH (str): The default input file path if not provided during instance creation.
        DEFAULT_OUTPUT_PATH (str): The default output file path if not provided during instance creation.

    Raises:
        FileNotFoundError: If the specified input file is not found during sequence reading.

    """
    # Class constants
    DEFAULT_INPUT_PATH = "data.txt"
    DEFAULT_OUTPUT_PATH = "result.txt"
    
    def __init__(self, input_path: str = None, output_path: str = None, window_range: Tuple[int, int] = (4, 12)) -> None:
        """
        Initialize the class.

        Args:
            input_path (str, optional): Path to the input file. Defaults to None.
            output_path (str, optional): Path to the output file. Defaults to None.
            window_range (Tuple[int, int], optional): Range of window sizes (min, max). Defaults to (4, 12).
        """
        self.input_path = input_path or self.DEFAULT_INPUT_PATH
        self.output_path = output_path or self.DEFAULT_OUTPUT_PATH
        self.dna_sequence = [] # Initialize an empty list for the DNA sequence
        self.window_range = window_range
        self.results = {} # Initialize an empty dictionary for results
        
        
    def read_sequence(self) -> None:
        """
        Read DNA sequences from a FASTA file and store them in the object.

        The DNA sequences are read from the FASTA file
        using the read_fasta function and stored as a single string in the 'dna_sequence'
        attribute of the object.

        Raises:
            FileNotFoundError: If the specified input file is not found.

        Returns:
            None
        """
        # Check if file exists
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        
        # Read all sequences from file
        seq_dict = read_fasta(self.input_path)
        # Put sequences in string
        self.dna_sequence = "".join(seq_dict.values())
    
    def create_substrings(self) -> None:
        """
        Generates substrings from the DNA sequence and stores them as nested dictionaries.

        Creates substrings of varying window sizes from the DNA sequence. The substrings are
        stored in a nested dictionary structure:
        {
            window_size_1: {position_1: substring_1, position_2: substring_2, ...},
            window_size_2: {position_1: substring_1, position_2: substring_2, ...},
            ...
        }

        The generated substrings are stored in the 'substrings' attribute of the object.

        Returns:
            None
        """
        # Determine lenght of sequence
        sequence_length = len(self.dna_sequence)
        # Generate empty dictionary to store window size and nested dictionary
        window_dict = {}
        # Unpack window_size tuple to get minimum and maximum window size
        min_window, max_window = self.window_range
        # Loop trough different window sizes
        for window_size in range(min_window, max_window):
            # Determine how many steps for given window size
            step_size = sequence_length - (window_size - 1)
            # Generate empty dictionary to store positions and substrings
            pos_substrings = {}
            # Iterate over whole sequence and store positions and substrings
            for step in range(step_size):
                substring = self.dna_sequence[step:step + window_size]
                pos_substrings[step + 1] = substring
            # Store values in dictionary
            window_dict[window_size] = pos_substrings
        self.substrings = window_dict
    
    def reverse_complement(self, sequence: str) -> None:
        """
        Compute the reverse complement of a DNA sequence.

        Args:
            sequence (str): The input DNA sequence for which the reverse complement is calculated.

        Returns:
            str: The reverse complement of the input DNA sequence.

        Takes a DNA sequence as input and computes its reverse complement.
        The reverse complement is obtained by reversing the input sequence and mapping
        each nucleotide to its complement (A to T, T to A, G to C, and C to G).

        Example:
            If the input sequence is 'ATGC', the reverse complement will be 'GCAT'.
        """
        # Reverse DNA sequence
        rev_seq = sequence[::-1]
        # Define mapping dictionary
        mapping_dict = {"A": "T",
                        "T": "A",
                        "G": "C",
                        "C": "G"}
        # Map characters in sequence
        complement_seq = [mapping_dict[char] for char in rev_seq]
        return "".join(complement_seq)
    
    def find_palindrom(self) -> None:
        """
        Check for palindromic DNA substrings and store results in the 'results' attribute.

        Iterates through the generated DNA substrings of different window sizes
        and checks if each substring is equal to its reverse complement. If a palindromic
        sequence is found, the window size and position are stored in the 'results'
        attribute as key-value pairs.

        The 'results' attribute has the following format:
        {
            position_1: window_size_1,
            position_2: window_size_2,
            ...
        }

        The method uses the 'reverse_complement' method internally to compute the reverse
        complement of each DNA substring.

        Returns:
            None
        """
        for window_size in self.substrings:
            for pos in self.substrings[window_size]:
                # Take one subsequence
                forward_seq = self.substrings[window_size][pos]
                # Reverse complement that sequence
                rev_seq = self.reverse_complement(sequence=forward_seq)
                # Check if forward sequence matches reverse complement
                if forward_seq == rev_seq:
                    self.results[pos] = window_size
                    
    def write_result(self) -> None:
        """
        Write palindromic DNA substring results to an output file.

        First sorts the palindromic results based on their positions. The sorted
        results are then written to the specified output file. Each line in the output file
        contains a position and its corresponding palindromic window size.

        The 'results' attribute, containing positions and window sizes, is expected to be
        populated by the 'find_palindrom' method before calling this method.

        Example output file content:
        ```
        10 3
        25 5
        36 2
        ```

        Returns:
            None
        """
        # First sort results based on positions
        self.results = dict(sorted(self.results.items()))
        with open(self.output_path, "w") as file:
            for pos, size in self.results.items():
                file.write(f"{pos} {size}\n")      

def main():
    """
    Execute the main workflow for finding palindromic DNA substrings.

    This function initializes a RestrictionSiteFinder, reads a DNA sequence from a file,
    generates substrings, checks for palindromic sequences, and writes the results to an
    output file.

    Usage:
        python restriction-site-finder.py

    Returns:
        None
    """
    restriction_finder = RestrictionSiteFinder()
    restriction_finder.read_sequence()
    restriction_finder.create_substrings()
    restriction_finder.find_palindrom()
    restriction_finder.write_result()

if __name__ == "__main__":
    main()