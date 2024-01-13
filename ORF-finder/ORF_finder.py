import os
import sys
from typing import Tuple, List, Dict

# Import helper functions
# Can be found in my GitHub repository "Codetoolbox".
sys.path.append("../Utility")
from fasta_reader import read_fasta
from reverse_complement import reverse_complement
from codon_mapper import codon_mapping

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
        self.rev_complement = None
        self.forward_1 = None
        self.forward_2 = None
        self.forward_3 = None
        self.reverse_1 = None
        self.reverse_2 = None
        self.reverse_3 = None
    
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
        self.rev_complement = reverse_complement(dna_sequence=self.raw_sequence)
    
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
            codon = sequence[3 * step : 3 * step + 3]
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
        # Sort start and stop positions
        start_pos = sorted(start_pos)
        stop_pos = sorted(stop_pos)
        # Iterate over start positions
        for st_pos in start_pos:
            # Iterate over stop positions
            for sp_pos in stop_pos:
                # Check if stop position is greater than start position
                if sp_pos > st_pos:
                    # Save ORF
                    orf_dict[st_pos] = sp_pos
                    # Break loop to only save the first start-stop-codon pair
                    break
        return orf_dict

    def translate_orf(self, reading_frame_dict: Dict, sequence: str) -> List:
        # Iterate over dictionary
        for start_pos, stop_pos in reading_frame_dict.items():
            dna_sequence = sequence[start_pos:stop_pos]
            protein_sequence = codon_mapping(sequence=dna_sequence, mode="DNA")
            
        
    
                    
        
    
    
    
    
    def write_result(self) -> None:
        """
        """
        # First sort results based on positions
        self.results = dict(sorted(self.results.items()))
        with open(self.output_path, "w") as file:
            for pos, size in self.results.items():
                file.write(f"{pos} {size}\n")
    
    def run_rest(self):
        tester = ORFFinder()
        tester.read_sequence()
        tester.transform_sequence()
        tester.create_reading_frames()
        starts = tester.find_start(tester.forward_1)
        stops = tester.find_stop(tester.forward_1)
        tester.find_orf(start_pos=starts, stop_pos=stops)
        
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