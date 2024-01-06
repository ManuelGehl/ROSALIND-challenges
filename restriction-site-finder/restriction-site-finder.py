# Import FASTA reading function
import sys
import os
sys.path.append("../Utility")
from fasta_utils import read_fasta

class RestrictionSiteFinder:
    """
    
    """
    # Class constants
    DEFAULT_INPUT_PATH = "data.txt"
    DEFAULT_OUTPUT_PATH = "result.txt"
    WINDOW_SIZE = 4
    
    def __init__(self, input_path=None, output_path=None):
        """
        
        """
        self.input_path = input_path or self.DEFAULT_INPUT_PATH
        self.output_path = output_path or self.DEFAULT_OUTPUT_PATH
        self.dna_sequence = []
        self.rev_complement = []
        self.window_size = self.WINDOW_SIZE
        self.motifs = {}
        self.results = {}
        
        
    def read_sequence(self):
        """
        Read DNA sequences from FASTA file.
        """
        # Check if file exists
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        
        # Read all sequences from file
        seq_dict = read_fasta(self.input_path)
        # Put sequences in string
        self.dna_sequence = "".join(seq_dict.values())
    
    def create_substrings(self):
        """
        Generates substrings from DNA sequence and reverse complement sequence.
        Window size ranges from 4 to 12.
        Stores substrings as 2 nested dictionaries of shape {window_size:{positions:substrings}}
        
        """
        # Determine lenght of sequence
        sequence_length = len(self.dna_sequence)
        # Generate empty dictionary to store window size and nested dictionary
        window_dict = {}
        # Loop trough different window sizes
        for window_size in range(4, 13):
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
    
    def reverse_complement(self, sequence):
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
    
    def find_palindrom(self):
        """
        Checks if DNA substring is equal to its reverse complement.
        """
        for window_size in self.substrings:
            for pos in self.substrings[window_size]:
                # Take one subsequence
                for_seq = self.substrings[window_size][pos]
                # Reverse complement that sequence
                rev_seq = self.reverse_complement(sequence=for_seq)
                # Check if forward sequence matches reverse complement
                if for_seq == rev_seq:
                    self.results[pos] = window_size
                    
    def write_result(self):
        """
        Write result to the output file.
        """
        # First sort results based on positions
        self.results = dict(sorted(self.results.items()))
        with open(self.output_path, "w") as file:
            for pos, size in self.results.items():
                file.write(f"{pos} {size}\n")      

def main():
    restriction_finder = RestrictionSiteFinder()
    restriction_finder.read_sequence()
    restriction_finder.create_substrings()
    restriction_finder.find_palindrom()
    restriction_finder.write_result()

if __name__ == "__main__":
    main()