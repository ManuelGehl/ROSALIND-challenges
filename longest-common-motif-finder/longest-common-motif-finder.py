# Import FASTA reading function
import sys
import os
sys.path.append("../Utility")
from fasta_utils import read_fasta


class LongestCommonMotifFinder:
    """
    LongestCommonMotifFinder is a class designed for finding the longest common motif
    among a collection of DNA sequences provided in a FASTA file.

    Attributes:
        DEFAULT_INPUT_PATH (str): Default path to the input file containing DNA sequences.
        DEFAULT_OUTPUT_PATH (str): Default path to the output file for storing the result.
        START_POSITION (int): Default start position for extracting motifs from sequences.
        END_POSITION (int): Default end position for extracting motifs from sequences.
        LOOP_TOGGLE (bool): Default loop toggle to control motif extraction process.

        input_path (str): Path to the input FASTA file containing DNA sequences.
        output_path (str): Path to the output file for storing the longest common motif.
        dna_sequences (list): Contains DNA strings read from FASTA.
        reference_seq (str): Per default first DNA sequence from FASTA file.
        current_motif (str): Current motif being evaluated during the search process.
        longest_motif (str): Longest common motif found among all sequences.
        start_pos (int): Current start position for motif extraction.
        end_pos (int): Current end position for motif extraction.
        loop_toggle (bool): Toggle to control the loop for motif extraction.

    Methods:
        __init__(self, input_path=None, output_path=None):
            Initializes the LongestCommonMotifFinder instance.
        
        read_sequence(self):
            Reads DNA sequences from the input FASTA file.

        initialize_motif(self):
            Initializes the motif extraction process by setting the current motif
            to the first nucleotide of the reference sequence.

        check_motif(self):
            Checks if the current motif is present in all DNA sequences and updates
            the longest motif if needed. Calls methods to extend or shift the motif.

        extend_motif(self):
            Extends the current motif by one nucleotide if the current motif
            was found in all DNA sequences.

        shift_motif(self):
            Shifts the current motif by one nucleotide to the right if the current
            motif was NOT found in all DNA sequences.

        write_result(self):
            Writes the longest common motif to the output file.
    """
    # Class constants
    DEFAULT_INPUT_PATH = "data.txt"
    DEFAULT_OUTPUT_PATH = "result.txt"
    START_POSITION = 0
    END_POSITION = 1
    LOOP_TOGGLE = True
    
    def __init__(self, input_path=None, output_path=None):
        """
        Initialize LongestCommonMotifFinder with input and output file paths.

        Parameters:
        - input_path (str): Path to the input file containing DNA sequences. Default is None.
        - output_path (str): Path to the output file for storing longest common motif. Default is None.
        """
        self.input_path = input_path or self.DEFAULT_INPUT_PATH
        self.output_path = output_path or self.DEFAULT_OUTPUT_PATH
        self.dna_sequences = []
        self.reference_seq = None
        self.current_motif = None
        self.longest_motif = ""
        self.start_pos = self.START_POSITION
        self.end_pos = self.END_POSITION
        self.loop_toggle = self.LOOP_TOGGLE
        
        
    def read_sequence(self):
        """
        Read DNA sequences from FASTA file.
        """
        # Check if file exists
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        
        # Read all sequences from file
        seq_dict = read_fasta(self.input_path)
        # Put sequences in list
        self.dna_sequences = list(seq_dict.values())
        # Use first sequence as reference sequence
        self.reference_seq = self.dna_sequences[0]
    
    def initialize_motif(self):
        """
        If no motif present, start with first character of first sequence
        as motif.
        If motif present raise exception
        """
        # Check if motif is empty
        if self.current_motif:
            raise ValueError("Motif has to be empty string")
        else:
            self.current_motif = self.reference_seq[self.start_pos:self.end_pos]
    
    def check_motif(self):
        """
        Checks if current motif is found in all DNA strings. If that is the case
        check if the current motif is the longest motif.
        """
        # Loop trough all sequences and set common_mot to True when found in all
        common_mot = all([self.current_motif in seq for seq in self.dna_sequences])
        
        # Execute when motif was found in all sequences
        if common_mot:
            print(f"Current motif {self.current_motif} found in all sequences")
            # Check if current motif is equal or longer to longest motif and save
            if len(self.current_motif) >= len(self.longest_motif):
                print(f"Longest current motif {self.current_motif}")
                self.longest_motif = self.current_motif
            
            # Call function to extend motif
            self.extend_motif()
        else:
            # Call function to shift current motif
            self.shift_motif()
    
    
    def extend_motif(self):
        """
        Extent the motif by one nucleotide.
        """
        # Check if end position is at the end of the sequence
        if len(self.reference_seq) ==  self.end_pos:
            print("End of sequence reached")
            # Set loop toggle to False
            self.loop_toggle = False
            # Write result in file
            self.write_result()
        else:
            self.end_pos += 1
            self.current_motif = self.reference_seq[self.start_pos:self.end_pos]
    
    def shift_motif(self):
        """
        Shift the current motif by one nucleotide to the right in the reference
        sequence.
        """
        self.start_pos += 1
        self.end_pos = self.start_pos + 1
        self.current_motif = self.reference_seq[self.start_pos:self.end_pos]
        print("Motif shifted")
    
    def write_result(self):
        """
        Write result to the output file.
        """
        with open(self.output_path, "w") as file:
            file.write(f"{self.longest_motif}")
        
def main():
    motif_finder = LongestCommonMotifFinder()
    motif_finder.read_sequence()
    motif_finder.initialize_motif()
    
    while motif_finder.loop_toggle:
        motif_finder.check_motif()

if __name__ == "__main__":
    main()