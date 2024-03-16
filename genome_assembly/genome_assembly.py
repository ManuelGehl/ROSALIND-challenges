from utility.fasta_reader import read_fasta
import os


class GenomeAssembly:
    
    def __init__(self, input_path="data.txt"):

        self.input_path = input_path
        
    def read_sequences(self) -> dict:
            
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
            # Initialize longest motif as None
            longest_motif = None
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
            # Initialize longest motif as None
            longest_motif = None
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
    
    def check_motifs(self, for_motif, back_motif):
        # If forward motif does not exist, insert placeholder
        if for_motif is None:
            for_motif = "X"
        # If backward motif does not exist, insert placeholder
        if back_motif is None:
            back_motif = "X"
        
        return for_motif, back_motif
    
    def fuse_reads(self, sequence1:str, sequence2:str) -> str:
        # Get longest common motifs
        forward_motif = self.forward_path(sequence1=sequence1, sequence2=sequence2)
        backward_motif = self.backward_path(sequence1=sequence1, sequence2=sequence2)
        
        # Check motifs
        forward_motif, backward_motif = self.check_motifs(for_motif=forward_motif,back_motif=backward_motif)
        
        # If both motifs were empty, return sequences
        if forward_motif == "X" and backward_motif == "X":
            return sequence1, sequence2      
            
        # Keep the longer motif and determine if prefix or suffix for sequence 1
        if len(forward_motif) > len(backward_motif):
            # Means that sequence 1 has a prefix in sequence 2
            # and sequence 2 will be fused 5' to sequence 1
            seq2_fragment = sequence2.removesuffix(forward_motif)
            fused_sequence = seq2_fragment + sequence1
        elif len(forward_motif) < len(backward_motif):
            # Means that sequence 2 is a suffix to sequence 1
            # and will be fused 3' to sequence 1
            seq2_fragment = sequence2.removeprefix(backward_motif)
            fused_sequence = sequence1 + seq2_fragment
        
        return fused_sequence

""" 
tester = GenomeAssembly()
dicti = tester.read_sequences()
seq1, seq2, seq3, seq4 = dicti.values()
tester.fuse_reads(seq1, seq2)
"""