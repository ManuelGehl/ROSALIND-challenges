import os
from typing import Tuple, List, Dict

# Import helper functions
# Can be found in my GitHub repository "Codetoolbox".
from Utility.fasta_reader import read_fasta

class SplicedMotifFinder:
   
    
    # Class constants
    DEFAULT_INPUT_PATH = "data.txt"
    DEFAULT_OUTPUT_PATH = "result.txt"
   
    def __init__(self, input_path: str = None, output_path:str = None) -> None:
        """
        Initializes an SplicedMotifFinder object with optional custom input and output paths.

        Args:
            input_path (str, optional): Path to the input data file. Defaults to None.
            output_path (str, optional): Path to the output result file. Defaults to None.

        Returns:
            None
        """
        self.input_path = input_path or self.DEFAULT_INPUT_PATH
        self.output_path = output_path or self.DEFAULT_OUTPUT_PATH
        self.sequence = None
        self.motif = None
        self.subsequences = []
    
    def read_sequence(self) -> None:
        """
        Reads a sequence from the specified input file in FASTA formate.

        Raises:
            FileNotFoundError: If the specified input file does not exist.
            FileNotFoundError: If the specified input file is empty.

        Reads the sequence from the file using the 'read_fasta' function and stores
        the concatenated sequence in the 'raw_sequence' attribute of the class.

        Returns:
            None
        """
        # Check if file exists
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        # Check if file is not empty
        if os.stat(self.input_path).st_size == 0:
            raise FileNotFoundError(f"Empty file")
        
        # Read all sequences from file
        seq_dict = read_fasta(self.input_path)
    
    
    def write_result(self) -> None:
        
        with open(self.output_path, "w") as file:
            #for orf in self.translated_orf:
             #   file.write(f"{orf}\n")
    

        

def main():
    
    spliced_motif_finder = SplicedMotifFinder()
    spliced_motif_finder.read_sequence()

if __name__ == "__main__":
    main()