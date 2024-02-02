from Utility. fasta_reader import read_fasta
import os
from typing import Dict, Tuple

class PrefixSuffixGraph:
    """Class to represent a Prefix-Suffix Graph for a collection of DNA strings."""
    
     # Class constants
    DEFAULT_INPUT_PATH = "data.txt"
    DEFAULT_OUTPUT_PATH = "result.txt"
    K_MER_LENGTH = 3
   
    def __init__(self, input_path: str = None, output_path:str = None) -> None:
        """
        Initialize PrefixSuffixGraph object.

        Parameters:
        - input_path (str): Path to the input file containing DNA sequences in FASTA format.
        - output_path (str): Path to the output file where the results will be written.
        """
        self.input_path = input_path or self.DEFAULT_INPUT_PATH
        self.output_path = output_path or self.DEFAULT_OUTPUT_PATH

    
    def read_sequences(self) -> Dict[str, str]:
        """
        Read DNA sequences from the input file in FASTA format.

        Returns:
        - Dict[str, str]: A dictionary mapping sequence IDs to their respective DNA sequences.
        """
        # Check if file exists
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        # Check if file is not empty
        if os.stat(self.input_path).st_size == 0:
            raise FileNotFoundError(f"Empty file")
        
        # Read all sequences from file
        seq_dict = read_fasta(self.input_path)
        
        return seq_dict
    
    def create_k_mers(self, seq_dict: Dict[str, str]) -> Tuple[Dict[str, str], Dict[str, str]]:
        """
        Create k-mers (prefixes and suffixes) for each DNA sequence.

        Parameters:
        - seq_dict (Dict[str, str]): A dictionary mapping sequence IDs to their respective DNA sequences.

        Returns:
        - Tuple[Dict[str, str], Dict[str, str]]: Tuple containing dictionaries of prefixes and suffixes.
        """
        suffix_dict = {seq_id: seq[:self.K_MER_LENGTH] for seq_id, seq in seq_dict.items()}
        prefix_dict = {seq_id: seq[-self.K_MER_LENGTH:] for seq_id, seq in seq_dict.items()}
        
        return prefix_dict, suffix_dict
    
    def create_adjacency_list(self, prefix_dict: Dict[str, str], suffix_dict: Dict[str, str]) -> Dict[str, list]:
        """
        Create an adjacency list representing the overlap relationships between DNA sequences.

        Parameters:
        - prefix_dict (Dict[str, str]): A dictionary mapping sequence IDs to their respective prefixes.
        - suffix_dict (Dict[str, str]): A dictionary mapping sequence IDs to their respective suffixes.

        Returns:
        - Dict[str, list]: A dictionary mapping sequence IDs to a list of IDs of sequences that overlap.
        """
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
    
    def write_results(self, adj_list: Dict[str, list]) -> None:
        """
        Write the adjacency list to the output file.

        Parameters:
        - adj_list (Dict[str, list]): A dictionary mapping sequence IDs to a list of IDs of sequences that overlap.
        """
        with open(self.output_path, "w") as file:
            for key in adj_list.keys():
                for value in adj_list[key]:
                    file.write(f"{key} {value}\n")

def main():
    """
    Main function to execute the PrefixSuffixGraph algorithm.
    """
    overlap_graphs = PrefixSuffixGraph()
    seq_dict = overlap_graphs.read_sequences()
    prefix_dict, suffix_dict = overlap_graphs.create_k_mers(seq_dict)
    adjacency_list = overlap_graphs.create_adjacency_list(prefix_dict, suffix_dict)
    overlap_graphs.write_results(adjacency_list)
    print("Process completed successfully")     
    
if __name__ == "__main__":
    main()   