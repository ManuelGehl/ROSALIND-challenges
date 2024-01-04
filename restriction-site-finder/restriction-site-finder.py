# Import FASTA reading function
import sys
import os
sys.path.append("/home/manuel/coding/projects/Rosalind/Utility")
from fasta_utils import read_fasta

class RestrictionSiteFinder:
    """
    
    """
    # Class constants
    DEFAULT_INPUT_PATH = "14 - Locating Restriction Sites/data.txt"
    DEFAULT_OUTPUT_PATH = "result.txt"
    WINDOW_SIZE = 4
    
    def __init__(self, input_path=None, output_path=None):
        """
        
        """
        self.input_path = input_path or self.DEFAULT_INPUT_PATH
        self.output_path = output_path or self.DEFAULT_OUTPUT_PATH
        self.dna_sequence = []
        self.rev_complement = []
        self.current_motif = None
        self.window_size = 4
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
        # Define empty list
        complement_seq = []
        
        # Map characters in sequence
        for char in self.rev_complement:
            complement_seq.append(mapping_dict[char])
        
        self.rev_complement = "".join(complement_seq)
    
    def find_restriction_site(self):
        # Check if window size is between 4 and 12
        assert self.window_size >= 4 and self.window_size <= 12, f"Window size {self.window_size}, expected 4-12"
        
        # Determine steps 
        steps = len(self.dna_sequence) + 1 - self.window_size
        
        # Scan trough sequence
        for step in range(steps):
            window = self.dna_sequence[0 + step: self.window_size + step] 
            # Check if motif is found in reverse complement
            if window in self.rev_complement:
                self.motifs[step + 1] = window
        
        
    
    def write_result(self):
        """
        Write result to the output file.
        """
        with open(self.output_path, "w") as file:
            file.write(f"{self.longest_motif}")
            
            
#%%
restriction_finder = RestrictionSiteFinder()
restriction_finder.read_sequence()
restriction_finder.reverse_complement()
restriction_finder.find_restriction_site()
 #%%       
def main():
    restriction_finder = RestrictionSiteFinder()
    restriction_finder.read_sequence()

if __name__ == "__main__":
    main()