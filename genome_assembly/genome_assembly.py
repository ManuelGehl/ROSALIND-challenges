from fasta_reader import read_fasta
from typing import Dict
import os


class GenomeAssembly:
    
    def __init__(self, input_path="data.txt"):

        self.input_path = input_path
        
    def read_sequences(self) -> Dict:
            
        # Check if file exists
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        # Check if file is not empty
        if os.stat(self.input_path).st_size == 0:
            raise FileNotFoundError(f"Empty file")
            
        # Read all sequences from file
        seq_dict = read_fasta(self.input_path)
        # Output sequences
        return seq_dict
    
    def forward_path(self, sequence1:str, sequence2:str) -> str:
        """
        Takes 2 sequences and scans the first sequence from 5' to 3' to find
        the longest common motif between the 2 sequences.
        """
        for position in range(1, len(sequence1)+1):
            # Define current window
            current_window = sequence1[0:position]
            # Check if current window occurs in sequence 2
            if current_window in sequence2:
                # Update longest common motif
                longest_motif = current_window
            # If current window not part of sequence 2 break loop
            else:
                break
        
        return longest_motif
    
    def backward_path(self, sequence1:str, sequence2:str) -> str:
        """
        Takes 2 sequences and scans the first sequence from 3' to 5' to find
        the longest common motif between the 2 sequences.
        """
        for position in range(2, len(sequence1)+1):
            # Define current window
            current_window = sequence1[-position:]
            # Check if current window occurs in sequence 2
            if current_window in sequence2:
                # Update longest common motif
                longest_motif = current_window
            # If current window not part of sequence 2 break loop
            else:
                break
        
        return longest_motif