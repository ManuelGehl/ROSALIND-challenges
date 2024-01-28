class ExpectedOffspring:
    """
    Calculate the expected number of offspring displaying the dominant phenotype
    in the next generation based on given genotype pairings.
    """
    
    # Class constants
    DEFAULT_INPUT_PATH = "data.txt"
    DEFAULT_OUTPUT_PATH = "result.txt"
    PAIRING_PROBABILITIES = {
        1: 1, # "AA-AA"
        2: 1, # "AA-Aa"
        3: 1, # "AA-aa"
        4: 0.75, # "Aa-Aa"
        5: 0.5, # "Aa-aa"
        6: 0 # "aa-aa"
    }
   
    def __init__(self, input_path: str = None, output_path:str = None) -> None:
        """
        Initialize ExpectedOffspring object.

        Parameters:
        - input_path (str): Path to the input file.
        - output_path (str): Path to the output file.
        """
        self.input_path = input_path or self.DEFAULT_INPUT_PATH
        self.output_path = output_path or self.DEFAULT_OUTPUT_PATH
        self.genotype_counts = {} # Dictionary to store genotype pair counts
        self.expected_offspring = None # Results placeholder
        
    def read_data(self) -> None:
        """
        Read genotype pair counts from the input file.
        """
        with open(self.input_path, "r") as file:
            line = file.readline().split(" ")
            for counter, elem in enumerate(line):
                self.genotype_counts[counter + 1] = int(elem)
    
    def calculate_offspring(self) -> None:
        """
        Calculate the expected number of offspring displaying the dominant phenotype.
        """
        result = sum([2 * self.genotype_counts[i] * self.PAIRING_PROBABILITIES[i] for i in range(1, 7)])
        self.expected_offspring = result

    def write_result(self) -> None:
        """
        Write the calculated result to the output file.
        """
        with open(self.output_path, "w") as file:
            file.write(str(self.expected_offspring))

def main():
    offspring = ExpectedOffspring()
    offspring.read_data()
    offspring.calculate_offspring()
    offspring.write_result()

if __name__ == "__main__":
    main()