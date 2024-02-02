class PermutationList:
    
    def __init__(self):
        pass
    
    def input(self):
        gene_number =  int(input("Please enter a number of genes for permutation between 0 and 7: "))
        assert gene_number <= 7, "Please enter a number less or equal to 7"
        assert gene_number > 0, "Please enter a number greater or equal to 1"
        return gene_number