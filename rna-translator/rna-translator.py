class RNATranslator():
    """
    Class for translating mRNA sequences into protein sequences.

    Attributes:
        input_path (str): Path to the input file containing mRNA sequence.
        output_path (str): Path to the output file to store the resulting protein sequence.
        rna_sequence (str): The mRNA sequence read from the input file.
        protein_sequence (str): The resulting protein sequence after translation.
   """
    # Define dictionary with codons for mapping
    CODON_TABLE = {
        "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L", "CUU": "L",
        "CUC": "L", "CUA": "L", "CUG": "L", "AUU": "I", "AUC": "I",
        "AUA": "I", "AUG": "M", "GUU": "V", "GUC": "V", "GUA": "V",
        "GUG": "V", "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
        "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P", "ACU": "T",
        "ACC": "T", "ACA": "T", "ACG": "T", "GCU": "A", "GCC": "A",
        "GCA": "A", "GCG": "A", "UAU": "Y", "UAC": "Y", "UAA": "Stop",
        "UAG": "Stop", "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
        "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K", "GAU": "D",
        "GAC": "D", "GAA": "E", "GAG": "E", "UGU": "C", "UGC": "C", 
        "UGA": "Stop", "UGG": "W", "CGU": "R", "CGC": "R", "CGA": "R",
        "CGG": "R", "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R", 
        "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
        }
    
    def __init__(self,input_path="data.txt", output_path="result.txt"):
        """
        Initializes the RNATranslator instance.

        Parameters:
            input_path (str, optional): Path to the input file. Default is "data.txt".
            output_path (str, optional): Path to the output file. Default is "result.txt".
        """
        self.input_path = input_path
        self.output_path = output_path
        self.rna_sequence = None
        self.protein_sequence = None
        
    def read_rna(self):
        """
        Reads the mRNA sequence from the input file.
        """
        with open(self.input_path) as file:
            for line in file:
                self.rna_sequence = line.strip()
    
    def translate(self):
        """
        Translates the mRNA sequence into a protein sequence using the codon table.
        """
        # Define list for storage of amino acids
        amino_acid_seq = []
        # Loop trough the rna sequence and map each codon to an amino acid
        num_codons = len(self.rna_sequence) // 3
        for i in range(num_codons):
            current_codon = self.rna_sequence[3 * i: 3 * i + 3]
            current_amino = self.CODON_TABLE.get(current_codon, None)
            # Print a message when unknown codon is in sequence
            if current_amino is None:
                print(f"Unknown codon at position: {3 * i}-{3 * i + 3}")
            # Check for stop codon
            if current_amino != "Stop":
                amino_acid_seq.append(current_amino)
            
        # Combine list to string
        amino_acid_seq = "".join(amino_acid_seq)
        
        # Write amino acid sequence in instance variable
        self.protein_sequence = amino_acid_seq
    
    def write_sequence(self):
        """
        Writes the protein sequence to the output file.
        """
        with open(self.output_path, "w") as file:
            file.write(self.protein_sequence)

def main():
    rna_translator = RNATranslator()
    rna_translator.read_rna()
    rna_translator.translate()
    rna_translator.write_sequence()


if __name__ == "__main__":
    main()
        

