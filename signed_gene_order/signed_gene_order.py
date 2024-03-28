class PermutationList:
    """
    A class to represent a permutation list.

    Attributes:
    - input_n: int, the number of genes for permutation.
    - genes: List[int], the stock of available numbers for permutations.
    - results: List[List[int]], the generated permutations.
    """
    
    def __init__(self) -> None:
        """
        Initializes a PermutationList object with default values.
        """
        self.input_n = None
        self.genes = None
        self.results = None
       
    def input(self) -> None:
        """
        Takes user input for the number of genes for permutation.
        Ensures the input is between 1 and 6.

        Raises:
        - AssertionError: If the input is not between 1 and 6.
        """
        
        self.input_n =  int(input("Please enter a number of genes for permutation between 0 and 6: "))
        assert (self.input_n <= 6), "Please enter a number less or equal to 6"
        assert (self.input_n > 0), "Please enter a number greater or equal to 1"
        
        # Generate possible integers for input n
        self.genes = list(range(self.input_n, 0, -1)) + list(range(-self.input_n, 0))

    def next_gene(self, partial_sequence: list) -> list:
        """
        Generates possible next gene sequences based on the given partial sequence.

        Args:
        - partial_sequence (list): The partial sequence of genes.

        Returns:
        - completed_sequence (list): A list of possible next gene sequences.

        Example:
        If partial_sequence = [1, -2], and self.genes = [4, 3, 2, 1, -4, -3, -2, -1],
        this method will return [[1, -2, 3], [1, -2, -3], [1, -2, 4], [1, -2, -4]].
        """
        completed_sequence = []
        # Create lookup array
        absolute_values = [abs(value) for value in partial_sequence]
        # Filter possible next values based on absolute values
        for next_gene in self.genes:
            if abs(next_gene) not in absolute_values:
                completed_sequence.append(partial_sequence + [next_gene])
                
        return completed_sequence
    
    def generate_permuations(self) -> None:
        """
        Generates all possible permutations of genes based on the number of genes specified.

        Returns:
        - None

        Example:
        If self.input_n = 3 and self.genes = [3, 2, 1, -3, -2, -1],
        this method will generate all possible permutations of length 3,
        such as [[3, 2, 1], [2, 3, 1], [-1, 3, -2], ...].
        """
        # Check for necessary instance variables
        if self.input_n is None:
            raise ValueError("input_n is not initialized")
        if not self.genes:
            raise ValueError("genes list is empty")
        
        # Initialize sequences
        sequences = self.genes
        
        # Iterate n - 1 times
        for _ in range(self.input_n - 1):
            # Initialize added sequence with empy list
            add_seq = []
            # Iterate over partial sequences
            for seq in sequences:
                # Check if seq is a list
                if type(seq) != list:
                    seq = [seq]
                # Add filled up sequences to list
                add_seq = add_seq + self.next_gene(partial_sequence=seq)
            # Update sequences to fill up also newly generated sequences
            sequences = add_seq
        # Save complete permutations
        self.results = sequences
    
    def print_results(self) -> None:
        """
        Prints the generated permutations to a file named "results.txt".

        Returns:
        - None
        """
        # Check for absence of results
        if not self.results:
            print("No results to print.")
            return 

        try:
            with open("results.txt", "w") as file:
                file.write(f"{len(self.results)}\n")
                for result in self.results:
                    file.write(' '.join(map(str, result)) + '\n')
                    
            print("Results printed to 'results.txt'.")
            
        except IOError as e:
            print(f"Error writing to file: {e}")
        
def main() -> None:
    """
    Orchestrates the process of generating permutations and printing results.

    Returns:
    - None
    """
    
    permutation_list = PermutationList()
    permutation_list.input()
    permutation_list.generate_permuations()
    permutation_list.print_results()
    

if __name__ == "__main__":
    main()