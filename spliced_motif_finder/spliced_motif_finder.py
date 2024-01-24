import os
from typing import List

# Import helper functions
# Can be found in my GitHub repository "Codetoolbox".
from Utility.fasta_reader import read_fasta

class SplicedMotifFinder:
    """
    A class for finding a spliced motif in a sequence.

    Attributes:
        DEFAULT_INPUT_PATH (str): Default path to the input data file.
        DEFAULT_OUTPUT_PATH (str): Default path to the output result file.
        input_path (str): Path to the input data file.
        output_path (str): Path to the output result file.
        sequence (str): The input sequence.
        motif (str): The motif to be found in the sequence.
    """
    
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
    
    def read_sequence(self) -> None:
        """
        Reads a sequence from the specified input file in FASTA format.

        Raises:
            FileNotFoundError: If the specified input file does not exist or is empty.

        Reads the sequence from the file using the 'read_fasta' function and stores
        the sequence in the 'sequence' attribute of the class and the motif in the 'motif' attribute.

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
    
    def generate_positions(self) -> List[List[int]]:
        """
        Generates a list of position lists for each character in the motif.

        Returns:
            List with positions as values.
        """
        # Generate empty list to store position lists
        position_list = []
        
        # Iterate over each character of the motif
        for char_mot in self.motif:
            character_list = []
            # Iterate over each character of the sequence
            for pos, char_seq in enumerate(self.sequence):
                # Check if characters are equal and append position in sequence
                if char_mot == char_seq:
                    character_list.append(pos+1)
            # Append complete list for each character in motif
            position_list.append(character_list)
    
        return position_list
    
    def find_spliced_motif(self, pos_lists: List[List[int]]) -> None:
        """
        Finds the spliced motif based on the generated position lists.

        Args:
            pos_lists (List[List[int]]): List of position lists for each character in the motif.

        Returns:
            None
        """
        # Define empty list for storage of firs spliced motif
        motif = []
        # Compute how many lists are in pos_lists
        length_lists = len(pos_lists)
        # Iterate over nested lists
        for i in range(length_lists):
            # Special case for first element
            if i == 0:
                motif.append(pos_lists[i][0])
            else:
                # Filter for all positions that are greater than last position
                pos_lists_filtered = [pos for pos in pos_lists[i] if pos > motif[i-1]]
                # Append first position that is greater than last position of last motif character
                motif.append(pos_lists_filtered[0])
        
        self.motif = motif
        
    
    
    def write_result(self) -> None:
        """
        Writes the spliced motif to the specified output file.

        Returns:
            None
        """
        with open(self.output_path, "w") as file:
            for pos in self.motif:
                file.write(f"{pos} ")
    


def main():
    """
    Main function to execute the SplicedMotifFinder application.
    
    Returns:
        None
    """
    spliced_motif_finder = SplicedMotifFinder()
    spliced_motif_finder.read_sequence()
    pos_lists = spliced_motif_finder.generate_positions()
    spliced_motif_finder.find_spliced_motif(pos_lists=pos_lists)
    spliced_motif_finder.write_result()
    
if __name__ == "__main__":
    main()