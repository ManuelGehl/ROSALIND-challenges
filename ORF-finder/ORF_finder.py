import os
from typing import Tuple, List, Dict

# Import helper functions
# Can be found in my GitHub repository "Codetoolbox".
from Utility.fasta_reader import read_fasta
from Utility.reverse_complement import reverse_complement
from Utility.condon_mapper import codon_mapping

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
        self.sequences = {}
        self.start_dictionary = {}
        self.stop_dictionary = {}
        self.orf_positions = {}
        self.translated_orf = []
    
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
    
    def generate_reading_frames(self) -> None:
        # Create reading frames on forward strand
        self.sequences["for_1"] = self.raw_sequence
        self.sequences["for_2"] = self.raw_sequence[1:]
        self.sequences["for_3"] = self.raw_sequence[2:]
        # Create reading frames on reverse strand
        self.sequences["rev_1"] = self.rev_complement
        self.sequences["rev_2"] = self.rev_complement[1:]
        self.sequences["rev_3"] = self.rev_complement[2:]
    
    def find_start(self) -> None:
        for name, sequence in self.sequences.items():
            start_positions = [step for step in range(0, len(sequence), 3) if sequence[step:step+3] == self.START_CODON]
            self.start_dictionary[name] = start_positions
    
    def find_stop(self) -> None:
        for name, sequence in self.sequences.items():
            stop_positions = [step for step in range(0, len(sequence), 3) if sequence[step:step+3] in self.STOP_CODONS]
            self.stop_dictionary[name] = stop_positions
    
    def find_orf(self) -> None:
        for key in self.sequences:
            orf_dict = {}
             # Sort start and stop positions
            start_pos = sorted(self.start_dictionary[key])
            stop_pos = sorted(self.stop_dictionary[key])
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
            self.orf_positions[key] = orf_dict
        
    def translate_orf(self) -> None:
        # Iterate over orf dictionary and continue only with filled dictionaries
        for seq, orf in self.orf_positions.items():
            for start_pos, stop_pos in orf.items():
                dna_sequence = self.sequences[seq][start_pos:stop_pos]
                protein_sequence = codon_mapping(sequence=dna_sequence, mode="DNA")
                
                self.translated_orf.append(protein_sequence)
    
    def remove_duplicates(self) -> None:
        self.translated_orf = set(self.translated_orf)
    
    def write_result(self) -> None:
        with open(self.output_path, "w") as file:
            for orf in self.translated_orf:
                file.write(f"{orf}\n")
    

        
"""
def main():
    restriction_finder = RestrictionSiteFinder()
    restriction_finder.read_sequence()
    restriction_finder.create_substrings()
    restriction_finder.find_palindrom()
    restriction_finder.write_result()

if __name__ == "__main__":
    main()
    
    
tester = ORFFinder()
tester.read_sequence()
tester.transform_sequence()
tester.generate_reading_frames()
tester.find_start()
tester.find_stop()
tester.find_orf()
tester.translate_orf()

tester.write_result()
"""