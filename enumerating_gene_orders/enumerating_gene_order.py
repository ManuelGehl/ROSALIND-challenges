from typing import List
import random

class PermutationList:
    """
    A class to represent a permutation list.

    Attributes:
    - gene_number: int, the number of genes for permutation.
    - total_perm: int, the total number of permutations.
    - stock: List[int], the stock of available numbers for permutations.
    - permutations: List[List[int]], the generated permutations.
    """
    
    def __init__(self):
        """
        Initializes a PermutationList object with default values.
        """
        self.gene_number = None
        self.total_perm = None
        self.stock = None
        self.permutations = None
    
    def input(self) -> None:
        """
        Takes user input for the number of genes for permutation.
        Ensures the input is between 1 and 7.
        """
        gene_number =  int(input("Please enter a number of genes for permutation between 0 and 7: "))
        assert (gene_number <= 7), "Please enter a number less or equal to 7"
        assert (gene_number > 0), "Please enter a number greater or equal to 1"
        self.gene_number = gene_number
    
    def total_permutations(self) -> None:
        """
        Calculates the total number of permutations based on the gene number.
        """
        # Calculate the factorial
        factorial = 1
        for factor in range(2, self.gene_number+1):
            factorial *= factor
        self.total_perm = factorial
    
    def generate_stock(self) -> None:
        """
        Generates the stock of available numbers for permutations.
        """
        self.stock = list(range(1, self.gene_number+1)) * self.total_perm
    
    def generate_permutations(self) -> None:
        """
        Generates unique permutations using the available stock.
        """
        permutation_list = []
        while len(self.stock) != 0:
            current_permutation = []
            while len(current_permutation) != self.gene_number:
                # Draw random number from stock
                current_num = random.choice(self.stock)
                # Check if current number is already in list
                if current_num not in current_permutation:
                    current_permutation.append(current_num)
                    self.stock.remove(current_num)
            # Append current permutation to permutation list
            if current_permutation in permutation_list:
                for elem in current_permutation:
                    self.stock.append(elem)
            else:
                permutation_list.append(current_permutation)
        
        self.permutations = permutation_list
    
    def output(self) -> None:
        """
        Outputs the total number of permutations and the generated permutations.
        """
        print(self.total_perm)
        for permutation in self.permutations:
            print(" ".join(map(str, permutation)))
    
def main():
    """
    The main function to execute the permutation generation and output.
    """
    permutation_list_instance = PermutationList()
    permutation_list_instance.input()
    permutation_list_instance.total_permutations()
    permutation_list_instance.generate_stock()
    permutation_list_instance.generate_permutations()
    permutation_list_instance.output()

if __name__ == "__main__":
    main()
