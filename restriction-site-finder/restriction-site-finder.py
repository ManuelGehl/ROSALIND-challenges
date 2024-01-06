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
    
    def reverse_complement(self):
        # Reverse DNA sequence
        self.rev_complement = self.dna_sequence[::-1]
        # Define mapping dictionary
        mapping_dict = {"A": "T",
                        "T": "A",
                        "G": "C",
                        "C": "G"}
        # Map characters in sequence
        complement_seq = [mapping_dict[char] for char in self.rev_complement]
        self.rev_complement = "".join(complement_seq)
    
    def create_substrings(self, sequence):
        """
        Generates substrings from DNA sequence and reverse complement sequence.
        Window size ranges from 4 to 12.
        Stores substrings as 2 nested dictionaries of shape {window_size:{positions:substrings}}
        
        """
        # Determine lenght of sequence
        sequence_length = len(sequence)
        # Generate empty dictionary to store window size and nested dictionary
        window_dict = {}
        # Loop trough different window sizes
        for window_size in range(4, 13):
            # Determine how many steps for given window size
            step_size = sequence_length - window_size
            # Generate empty dictionary to store positions and substrings
            pos_substrings = {}
            # Iterate over whole sequence and store positions and substrings
            for step in range(step_size):
                substring = sequence[step:step + window_size]
                pos_substrings[step + 1] = substring
            # Store values in dictionary
            window_dict[window_size] = pos_substrings
        
        return window_dict
        
    
    def find_palindrom(self, dna_substrings, rev_substrings):
        """
        Checks if DNA substring is equal to its reverse complement at same position.
        """
        for window_size in range(4, 13):
            for pos in dna_substrings[window_size]:
                if dna_substrings[window_size][pos] == rev_substrings[window_size][pos]:
                    print(f"Pos1 {pos}")
                    print(f"DNA {dna_substrings[pos]}")
                    print(f"Rev {rev_substrings[pos]}")
                    

        
    def write_result(self):
        """
        Write result to the output file.
        """
        with open(self.output_path, "w") as file:
            file.write(f"{self.longest_motif}")      
""""
restriction_finder = RestrictionSiteFinder()
restriction_finder.read_sequence()
restriction_finder.reverse_complement()
dna_substrings = restriction_finder.create_substrings(sequence=restriction_finder.dna_sequence)
rev_substrings = restriction_finder.create_substrings(sequence=restriction_finder.rev_complement)
restriction_finder.find_palindrom(dna_substrings=dna_substrings, rev_substrings=rev_substrings)

if __name__ == "__main__":
    main()
"""