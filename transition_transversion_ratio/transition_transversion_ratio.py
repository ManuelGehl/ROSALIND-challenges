import os
# Import helper functions
# Can be found in my GitHub repository "Codetoolbox".
from Utility.fasta_reader import read_fasta

PURINE_PYRIMIDINE_MAPPING = {
    "A": "U",
    "G": "U",
    "C": "Y",
    "T": "Y",
    "U": "Y"}

class TransitionTransversionMeasurer:
    
    

    
    def __init__(self, input_path="data.txt"):

        self.input_path = input_path
        self.sequence1 = None
        self.sequence2 = None
        self.transversion_counter = 0
        self.transition_counter = 0
        self.transition_transversion_ratio = None
       
        
    def read_sequences(self) -> None:
            
        # Check if file exists
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        # Check if file is not empty
        if os.stat(self.input_path).st_size == 0:
            raise FileNotFoundError(f"Empty file")
            
        # Read all sequences from file
        seq_dict = read_fasta(self.input_path)
        # Output sequences
        self.sequence1, self.sequence2 = seq_dict.values()
        
    def count_transitions_transversions(self, sequence1, sequence2) -> None:
        # Initialize counters
        transition_counter = 0
        transversion_counter = 0
        # Check if sequences are of equal length
        if len(sequence1) != len(sequence2):
            raise ValueError("Sequences must be of equal length")
        
        for i in range(len(sequence1)):
            # First check if bases are equal
            if sequence1[i] != sequence2[i]:
                # Then check if transition or transversion
                if PURINE_PYRIMIDINE_MAPPING[sequence1[i]] == PURINE_PYRIMIDINE_MAPPING[sequence2[i]]:
                    transition_counter += 1
                else:
                    transversion_counter += 1
        # Output results
        self.transition_counter = transition_counter
        self.transversion_counter = transversion_counter
    
    def calculate_ratio(self) -> None:
        # Calculate ratio
        self.transition_transversion_ratio = self.transition_counter / self.transversion_counter
        # Print result
        print(f"Transition/Transversion ratio: {self.transition_transversion_ratio}")
        

def main():
    measurer = TransitionTransversionMeasurer()
    measurer.read_sequences()
    seq1, seq2 = measurer.sequence1, measurer.sequence2
    measurer.count_transitions_transversions(seq1, seq2)
    measurer.calculate_ratio()

if __name__ == "__main__":
    main()