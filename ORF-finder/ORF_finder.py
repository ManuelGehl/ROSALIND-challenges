import os
import sys
from typing import Tuple, List, Dict

# Import helper functions
# Can be found in my GitHub repository "Codetoolbox".
sys.append("/Utility")
from fasta_reader import read_fasta
from reverse_complement import reverse_complement

class ORFFinder:
    
    # Class constants
    DEFAULT_INPUT_PATH = "data.txt"
    DEFAULT_OUTPUT_PATH = "result.txt"
    START_CODON ="ATG"
    STOP_CODONS = ["TAG", "TGA", "TAA"]
    
    def __init__(self, input_path: str = None, output_path:str = None) -> None:
        self.input_path = input_path or self.DEFAULT_INPUT_PATH
        self.output_path = output_path or self.DEFAULT_OUTPUT_PATH
        self.raw_sequence = None
    
    def read_sequence(self) -> None:
        # Check if file exists
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        
        # Read all sequences from file
        seq_dict = read_fasta(self.input_path)
        # Put sequences in string
        self.raw_sequence = "".join(seq_dict.values())
    
    def transform_sequence(self) -> None:
        # Transform DNA sequence in reverse complement
        self.rev_complement = reverse_complement(self.raw_sequence)
    
    def create_reading_frames(self) -> None:
        # Create reading frames on forward strand
        self.forward_1 = self.raw_sequence
        self.forward_2 = self.raw_sequence[1:]
        self.forward_3 = self.raw_sequence[2:]
        # Create reading frames on reverse strand
        self.reverse_1 = self.rev_complement
        self.reverse_2 = self.rev_complement[1:]
        self.reverse_3 = self.rev_complement[2:]
    
    def find_start(self, sequence: str) -> List:
        step_size = len(sequence) // 3
        start_positions = []
        for step in range(step_size):
            codon = sequence[step:step + 3]
            if codon == self.START_CODON:
                start_positions.append(step)
        return start_positions
    
    def find_stop(self, sequence: str) -> List:
        step_size = len(sequence) // 3
        stop_positions = []
        for step in range(step_size):
            codon = sequence[step:step + 3]
            if codon in self.STOP_CODONS:
                stop_positions.append(step)
        return stop_positions
    
    def find_orf(self, start_pos: List, stop_pos: List) -> Dict:
        orf_dict = {}
        for stop_codon in stop_pos:
            for start_codon in start_pos:
                if stop_codon > start_codon:
                    orf_dict[]
    ############### Continue here
                    
        
    
    
    
    
    def write_result(self) -> None:
        """
        """
        # First sort results based on positions
        self.results = dict(sorted(self.results.items()))
        with open(self.output_path, "w") as file:
            for pos, size in self.results.items():
                file.write(f"{pos} {size}\n")      
"""
def main():
    restriction_finder = RestrictionSiteFinder()
    restriction_finder.read_sequence()
    restriction_finder.create_substrings()
    restriction_finder.find_palindrom()
    restriction_finder.write_result()

if __name__ == "__main__":
    main()
"""
