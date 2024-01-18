import os

# Import helper functions
# Can be found in my GitHub repository "Codetoolbox".
from Utility.fasta_reader import read_fasta
from Utility.condon_mapper import codon_mapping

class RNASplicer:
    """
    Class for splicing DNA sequences and mapping to proteins.

    Attributes:
        DEFAULT_INPUT_PATH (str): Default path to the input data file.
        DEFAULT_OUTPUT_PATH (str): Default path to the output result file.
        input_path (str): Path to the input data file.
        output_path (str): Path to the output result file.
        raw_sequence (str): Raw DNA sequence.
        introns (list): List of introns to be removed from the sequence.
        spliced_seq (str): DNA sequence after splicing.
        protein_seq (str): Protein sequence mapped from the spliced DNA.

    Methods:
        __init__: Initializes a RNASplicer object.
        read_sequence: Reads a sequence from the specified input file in FASTA format.
        splice_sequence: Splices the raw RNA sequence by removing introns.
        express: Maps the spliced DNA sequence to a protein sequence using codon mapping.
        write_result: Writes the protein sequence to the specified output file.
    """
    # Class constants
    DEFAULT_INPUT_PATH = "data.txt"
    DEFAULT_OUTPUT_PATH = "result.txt"
    
    def __init__(self, input_path: str = None, output_path:str = None) -> None:
        """
        Initializes a RNASplicer object with optional custom input and output paths.

        Args:
            input_path (str, optional): Path to the input data file. Defaults to None.
            output_path (str, optional): Path to the output result file. Defaults to None.

        Returns:
            None
        """
        self.input_path = input_path or self.DEFAULT_INPUT_PATH
        self.output_path = output_path or self.DEFAULT_OUTPUT_PATH
        self.raw_sequence = None
        self.introns = []
        self.spliced_seq = None
    
    def read_sequence(self) -> None:
        """
        Reads a sequence from the specified input file in FASTA format.

        Raises:
            FileNotFoundError: If the specified input file does not exist.
            FileNotFoundError: If the specified input file is empty.

        Reads the sequence from the file using the 'read_fasta' function and stores
        the concatenated sequence in the 'raw_sequence' attribute of the class.

        Returns:
            None
        """
        # Check if file exists
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        # Check if file is not empty
        if os.stat(self.input_path).st_size == 0:
            raise FileNotFoundError(f"Empty file")
        # Read all sequences from file
        seq_dict = read_fasta(self.input_path)
        self.raw_sequence, *self.introns = seq_dict.values()
        
    def splice_sequence(self) -> None:
        """
        Splices the raw DNA sequence by removing introns.

        Raises:
            ValueError: If no introns are found in the sequence.

        Modifies the 'spliced_seq' attribute of the class by removing introns
        from the 'raw_sequence' attribute.

        Returns:
            None
        """
        # Check if introns are present
        if not self.introns:
            raise ValueError("No introns found in the sequence.")
        seq = self.raw_sequence
        for intron in self.introns:
            seq = seq.split(intron)
            seq = "".join(seq)
        self.spliced_seq = seq
    
    def express(self) -> None:
        """
        Maps the spliced DNA sequence to a protein sequence using codon mapping.

        Modifies the 'protein_seq' attribute of the class using the 'codon_mapping'
        function with "DNA" mode.

        Returns:
            None
        """
        self.protein_seq = codon_mapping(
            sequence=self.spliced_seq,
            mode="DNA")
    
    def write_result(self) -> None:
        """
        Writes the protein sequence to the specified output file.

        Creates or overwrites the output file with the 'protein_seq' attribute content.

        Returns:
            None
        """
        with open(self.output_path, "w") as file:
            file.write(self.protein_seq)

def main() -> None:
    """
    Main function to execute the RNASplicer class operations.

    Returns:
        None
    """
    splicer = RNASplicer()
    splicer.read_sequence()
    splicer.splice_sequence()
    splicer.express()
    splicer.write_result()
    
if __name__ == "__main__":
    main()