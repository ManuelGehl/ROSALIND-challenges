import os

class MonoisotopicMassCalculator():
    """
     A class for calculating the monoisotopic mass of a peptide sequence.
    """
    
    # Class constants
    DEFAULT_INPUT_PATH = "data.txt"
    DEFAULT_OUTPUT_PATH = "result.txt"
    
    # Mapping dictionary for amino acid weights
    amino_acid_weights = {
        'A': 71.03711,
        'C': 103.00919,
        'D': 115.02694,
        'E': 129.04259,
        'F': 147.06841,
        'G': 57.02146,
        'H': 137.05891,
        'I': 113.08406,
        'K': 128.09496,
        'L': 113.08406,
        'M': 131.04049,
        'N': 114.04293,
        'P': 97.05276,
        'Q': 128.05858,
        'R': 156.10111,
        'S': 87.03203,
        'T': 101.04768,
        'V': 99.06841,
        'W': 186.07931,
        'Y': 163.06333
        }

    
    def __init__(self, input_path: str = None, output_path: str = None) -> None:
        """
        Initialize the MonoisotopicMassCalculator.

        Parameters:
        - input_path (str): Path to the input file containing the peptide sequence.
        - output_path (str): Path to the output file where the result will be written.
        """
        self.input_path = input_path or self.DEFAULT_INPUT_PATH
        self.output_path = output_path or self.DEFAULT_OUTPUT_PATH
        self.peptide_sequence = None
        self.mass = 0
        
        
    def read_sequence(self) -> None:
        """
        Read the peptide sequence from the input file.
        Raises FileNotFoundError if the input file is not found.
        """
        # Check if file exists
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        # Check if file is empty
        if os.path.getsize(self.input_path) == 0:
            raise FileNotFoundError(f"Input file is empty: {self.input_path}")
        
        # Read peptide sequence from file
        with open(self.input_path, "r") as file:
            for line in file:
                self.peptide_sequence = line.upper()
    
    def calculate_mass(self) -> None:
        """
        Calculate the monoisotopic mass of the peptide sequence.
        """
        for residue in self.peptide_sequence:
            self.mass += self.amino_acid_weights[residue]
    
    def write_result(self) -> None:
        """
        Write the calculated mass to the output file.
        """
        with open(self.output_path, "w") as file:
            file.write(f"{round(self.mass, 3)}")
    
def main():
    """
    Main function for executing the monoisotopic mass calculation.
    """
    calculator = MonoisotopicMassCalculator()
    calculator.read_sequence()
    calculator.calculate_mass()
    calculator.write_result()

if __name__ == "__main__":
    main()