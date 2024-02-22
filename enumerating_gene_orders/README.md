# Permutation List Generator

This Python script generates unique permutations for a given number of genes. It utilizes the `PermutationList` class to handle the input, calculation, and generation of permutations.

## Usage

Run the script:

```bash
python enumerating_gene_order.py
```
Follow the prompts to enter the number of genes for permutation.

## PermutationList Class


The PermutationList class has the following methods:

    
`input`: Takes user input for the number of genes for permutation.

`total_permutations`: Calculates the total number of permutations based on the gene number.

`generate_stock`: Generates the stock of available numbers for permutations.

`generate_permutations`: Generates unique permutations using the available stock.

`output`: Outputs the total number of permutations and the generated permutations.
