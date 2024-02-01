from Utility. fasta_reader import read_fasta
import os
from typing import Dict

class PrefixSuffixGraph:
    
     # Class constants
    DEFAULT_INPUT_PATH = "data.txt"
    DEFAULT_OUTPUT_PATH = "result.txt"
   
    def __init__(self, input_path: str = None, output_path:str = None) -> None:

        self.input_path = input_path or self.DEFAULT_INPUT_PATH
        self.output_path = output_path or self.DEFAULT_OUTPUT_PATH

    
    def read_sequences(self) -> Dict:
        # Check if file exists
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        # Check if file is not empty
        if os.stat(self.input_path).st_size == 0:
            raise FileNotFoundError(f"Empty file")
        
        # Read all sequences from file
        seq_dict = read_fasta(self.input_path)
        
        return seq_dict
    