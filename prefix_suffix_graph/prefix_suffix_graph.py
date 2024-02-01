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
    
    def create_3_mers(self, seq_dict: Dict):
        suffix_dict = {}
        prefix_dict = {}
        for seq_id, seq in seq_dict.items():
            prefix, suffix = seq[:3], seq[-3:]
            prefix_dict[seq_id] = prefix
            suffix_dict[seq_id] = suffix
        
        return prefix_dict, suffix_dict
    
    def create_adjacency_list(self, prefix_dict: Dict, suffix_dict: Dict):
        adjacency_list = {}
        # Iterate over suffixes
        for seq_id_suf, suffix in suffix_dict.items():
            # Initialize empty list for seq_ids
            adjacent_ids = []
            for seq_id_pre, prefix in prefix_dict.items():
                # Check if seq_id is not the same
                if seq_id_suf != seq_id_pre:
                    if suffix == prefix:
                        adjacent_ids.append(seq_id_pre)
                        
            # Append only hits           
            if adjacent_ids:            
                adjacency_list[seq_id_suf] = adjacent_ids
        
        return adjacency_list
                        
             


"""
tester = PrefixSuffixGraph()
seq_dict = tester.read_sequences()
prefix_dict, suffix_dict = tester.create_3_mers(seq_dict)
tester.create_adjacency_list(prefix_dict, suffix_dict)
"""            