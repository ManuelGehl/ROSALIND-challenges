class MotifFinder():
    """
    MotifFinder class for finding a motif in a DNA sequence.
    """
    
    def __init__(self, input_path="data.txt", output_path="result.txt"):
        """
        Initialize MotifFinder with input and output file paths.
        
        Parameters:
        - input_path (str): Path to the input file containing DNA sequence and motif.
        - output_path (str): Path to the output file for storing positions of the motif.
        """
        self.input_path = input_path
        self.output_path = output_path
        self.dna_sequence = None
        self.motif = None
        self.positions = None
        
    def read_sequence(self):
        """
        Read DNA sequence and motif from the input file.
        """
        with open(self.input_path) as file:
            # Read the first line as DNA sequence
            self.dna_sequence = file.readline().strip()
            # Read the second line as the motif
            self.motif = file.readline().strip()
    
    def find_motif(self):
        """
        Find positions of the motif in the DNA sequence.
        """
        # Define length of motif and sequence
        length_mot = len(self.motif)
        length_seq = len(self.dna_sequence)
        # Define difference between 2 strings as maximal step size
        length_diff = length_seq - length_mot
        # Define list for storing starting positions of found motifs
        starting_pos = []
        
        # Iterate over sequence
        for i in range(length_diff):
            frame = self.dna_sequence[i:i + length_mot]
            if frame == self.motif:
                starting_pos.append(i + 1)
        
        # Save results in instance variable
        self.positions = starting_pos
        
    def write_positions(self):
        """
        Writes the positions to the output file.
        """
        with open(self.output_path, "w") as file:
            # Write positions separated by space
            for pos in self.positions:
                file.write(str(pos) + " ")

def main():
    """
    Main function to run the MotifFinder.
    """
    motif_finder = MotifFinder()
    motif_finder.read_sequence()
    motif_finder.find_motif()
    motif_finder.write_positions()


if __name__ == "__main__":
    main()