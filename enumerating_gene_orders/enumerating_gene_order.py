import math
from typing import List

class PermutationList:
    
    def __init__(self):
        self.gene_number = None
        self.total_perm = None
        self.freq = None
        self.stock = None
    
    def input(self) -> int:
        gene_number =  int(input("Please enter a number of genes for permutation between 0 and 7: "))
        assert gene_number <= 7, "Please enter a number less or equal to 7"
        assert gene_number > 0, "Please enter a number greater or equal to 1"
        self.gene_number = gene_number
    
    def total_permutations(self) -> None:
        self.total_perm = math.factorial(self.gene_number)
    
    def generate_stock(self) -> List[int]:
        self.stock = list(range(1, self.gene_number+1)) * self.total_perm
    
    #def generate_permutations(self):
    #    for _ in range(self.total_perm):
    #        first_pos = self.total_perm.pop()
    #        second_pos = [num for num in self.total_perm]
            
            

"""  
tester = PermutationList()
tester.input()
tester.total_permutations()
tester.generate_stock()
"""