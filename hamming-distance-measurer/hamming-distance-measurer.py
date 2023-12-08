class MutationMeasurer:
    """
    A class for measuring Hamming distance of 2 strings of the same size.
    """
    
    def __init__(self, input_path="data.txt"):
        """
        Initialize the MutationMeasurer object.
        
        Parameters:
            - input_path (str): Path to the input file
        """
        self.input_path = input_path
        self.sequence1 = None
        self.sequence2 = None
       
        
    def read_sequence(self):
        """
        Read DNA sequences from file.
        """
        # Create container for storage of lines
        sequences = []
        with open(self.input_path) as file:
            for line in file:
                sequences.append(line.strip())
        
        # Assign sequences
        if len(sequences) == 2:
            self.sequence1 = sequences[0]
            self.sequence2 = sequences[1]
        else:
            raise ValueError("Input file must contain exactly two sequences")
    
    def hamming_distance(self):
        """
        Measures hamming distance between 2 sequences.
        """
        # Check if sequences are of equal length
        if len(self.sequence1) != len(self.sequence2):
            raise ValueError("Sequences must be of equal length")
        
        counter = 0
        for i in range(len(self.sequence1)):
            if self.sequence1[i] != self.sequence2[i]:
                counter += 1
        print(f"Hamming distance: {counter}")

def main():
    measurer = MutationMeasurer()
    measurer.read_sequence()
    measurer.hamming_distance()


if __name__ == "__main__":
    main()