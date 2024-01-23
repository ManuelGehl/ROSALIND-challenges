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
        # Output first sequence as sequence and second sequence as motif
        self.sequence, self.motif = seq_dict.values()
    
    def generate_positions(self):
        # Generate empty dictionary to store position lists
        pos_dictionary = []
        #position_list = []
        
        for char_number, char_mot in enumerate(self.motif):
            
            position_list = []
            for pos, char_seq in enumerate(self.sequence):
                if char_mot == char_seq:
                    position_list.append(pos)
            
            pos_dictionary.append(position_list)
        
        return pos_dictionary
    
    def padding(self, positions):
        # Check what is the longest list in positions
        max_len = 0
        for element in positions:
            current_len = len(element)
            if current_len > max_len:
                max_len = current_len
        
        # Iterate over lists and fill up values with 0s
        padded_positions = []
        for element in positions:
            diff = int(max_len - len(element))
            for _ in range(diff):
                element.append(0)
        
            padded_positions.append(element)
        
        return padded_positions
        
        
                    
        
    
    
    #def write_result(self) -> None:
        
        #with open(self.output_path, "w") as file:
            #for orf in self.translated_orf:
             #   file.write(f"{orf}\n")
    

def tester():
    tester = SplicedMotifFinder()
    tester.read_sequence()
    pos_dict = tester.generate_positions()
    tester.padding(pos_dict)
    return tester       

def main():
    spliced_motif_finder = SplicedMotifFinder()
    spliced_motif_finder.read_sequence()

#if __name__ == "__main__":
#    main()