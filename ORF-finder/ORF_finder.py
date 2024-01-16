import os
from typing import Tuple, List, Dict

# Import helper functions
# Can be found in my GitHub repository "Codetoolbox".
from Utility.fasta_reader import read_fasta
from Utility.reverse_complement import reverse_complement
from Utility.condon_mapper import codon_mapping

class ORFFinder:
    """
    Class for finding Open Reading Frames (ORFs) in DNA sequences.

    This class provides methods to process DNA sequences, identify ORFs, and
    translate them into protein sequences. It includes default constants for
    input and output paths, start and stop codons.

    Attributes:
        DEFAULT_INPUT_PATH (str): Default path for input data file.
        DEFAULT_OUTPUT_PATH (str): Default path for output result file.
        START_CODON (str): Start codon used to identify the beginning of ORFs.
        STOP_CODONS (List[str]): List of stop codons to identify the end of ORFs.
        input_path (str): Path to the input data file.
        output_path (str): Path to the output result file.
        raw_sequence (str): Raw DNA sequence read from the input file.
        rev_complement (str): Reverse complement of the raw DNA sequence.
        sequences (Dict[str, str]): Dictionary to store sequence names and their respective DNA sequences.
        start_dictionary (Dict[str, List[int]]): Dictionary to store start codon positions for each sequence.
        stop_dictionary (Dict[str, List[int]]): Dictionary to store stop codon positions for each sequence.
        orf_positions (Dict[str, Dict[int, int]]): Dictionary to store ORF positions for each sequence.
        translated_orf (List[str]): List to store translated protein sequences from identified ORFs.
    """
    
    # Class constants
    DEFAULT_INPUT_PATH = "data.txt"
    DEFAULT_OUTPUT_PATH = "result.txt"
    START_CODON ="ATG"
    STOP_CODONS = ["TAG", "TGA", "TAA"]
   
    
    def __init__(self, input_path: str = None, output_path:str = None) -> None:
        """
        Initializes an ORFFinder object with optional custom input and output paths.

        Args:
            input_path (str, optional): Path to the input data file. Defaults to None.
            output_path (str, optional): Path to the output result file. Defaults to None.

        Returns:
            None
        """
        self.input_path = input_path or self.DEFAULT_INPUT_PATH
        self.output_path = output_path or self.DEFAULT_OUTPUT_PATH
        self.raw_sequence = None
        self.rev_complement = None
        self.sequences = {}
        self.start_dictionary = {}
        self.stop_dictionary = {}
        self.orf_positions = {}
        self.translated_orf = []
    
    def read_sequence(self) -> None:
        """
        Reads a sequence from the specified input file in FASTA formate.

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
        # Put sequences in string
        self.raw_sequence = "".join(seq_dict.values())
    
    def transform_sequence(self) -> None:
        """
        Transforms the DNA sequence in reverse complement.

        Updates the 'rev_complement' attribute of the class with the reverse complement
        of the 'raw_sequence' attribute.

        Returns:
            None
        """
        # Transform DNA sequence in reverse complement
        self.rev_complement = reverse_complement(dna_sequence=self.raw_sequence)
    
    def generate_reading_frames(self) -> None:
        """
        Generates reading frames for both forward and reverse strands.

        Updates the 'sequences' attribute of the class with reading frames on the
        forward and reverse strands.

        Returns:
            None
        """
        # Create reading frames on forward strand
        self.sequences["for_1"] = self.raw_sequence
        self.sequences["for_2"] = self.raw_sequence[1:]
        self.sequences["for_3"] = self.raw_sequence[2:]
        # Create reading frames on reverse strand
        self.sequences["rev_1"] = self.rev_complement
        self.sequences["rev_2"] = self.rev_complement[1:]
        self.sequences["rev_3"] = self.rev_complement[2:]
    
    def find_start(self) -> None:
        """
        Finds start codon positions in each reading frame.

        Updates the 'start_dictionary' attribute of the class with the positions of
        start codons in each reading frame.

        Returns:
            None
        """
        for name, sequence in self.sequences.items():
            start_positions = [step for step in range(0, len(sequence), 3) if sequence[step:step+3] == self.START_CODON]
            self.start_dictionary[name] = start_positions
    
    def find_stop(self) -> None:
        """
        Finds stop codon positions in each reading frame.

        Updates the 'stop_dictionary' attribute of the class with the positions of
        stop codons in each reading frame.

        Returns:
            None
        """
        for name, sequence in self.sequences.items():
            stop_positions = [step for step in range(0, len(sequence), 3) if sequence[step:step+3] in self.STOP_CODONS]
            self.stop_dictionary[name] = stop_positions
    
    def find_orf(self) -> None:
        """
        Finds Open Reading Frames (ORFs) in each reading frame and stores their positions in the 'orf_positions' attribute.

        Uses the sorted lists of start and stop positions from 'start_dictionary' and 'stop_dictionary' respectively.
        Iterates through start and stop positions to identify the first valid start-stop codon pair for each reading frame.

        Returns:
            None
        """
        for key in self.sequences:
            orf_dict = {}
             # Sort start and stop positions
            start_pos = sorted(self.start_dictionary[key])
            stop_pos = sorted(self.stop_dictionary[key])
            # Iterate over start positions
            for st_pos in start_pos:
                # Iterate over stop positions
                for sp_pos in stop_pos:
                    # Check if stop position is greater than start position
                    if sp_pos > st_pos:
                        # Save ORF
                        orf_dict[st_pos] = sp_pos
                        # Break loop to only save the first start-stop-codon pair
                        break
            self.orf_positions[key] = orf_dict
        
    def translate_orf(self) -> None:
        """
        Translate Open Reading Frames (ORFs) in amino acid sequences using codon mapping.

        This method iterates over the ORF dictionary stored in the object and translates
        each ORF sequence to a protein sequence using codon mapping. The translated
        protein sequences are appended to the `translated_orf` list in the object.

        Returns:
            None
        """
        # Iterate over orf dictionary and continue only with filled dictionaries
        for seq, orf in self.orf_positions.items():
            for start_pos, stop_pos in orf.items():
                dna_sequence = self.sequences[seq][start_pos:stop_pos]
                protein_sequence = codon_mapping(sequence=dna_sequence, mode="DNA")
                
                self.translated_orf.append(protein_sequence)
    
    def remove_duplicates(self) -> None:
        """
        Remove duplicate protein sequences from the translated ORF list.

        This method utilizes a set to remove duplicate protein sequences from the
        `translated_orf` list in the object. After applying this method, the list
        will only contain unique protein sequences.

        Returns:
            None
        """
        self.translated_orf = set(self.translated_orf)
    
    def write_result(self) -> None:
        """
        Write translated ORF protein sequences to a specified output file.

        This method opens the specified output file in write mode and writes each
        translated ORF protein sequence to a new line in the file.

        Returns:
            None
        """
        with open(self.output_path, "w") as file:
            for orf in self.translated_orf:
                file.write(f"{orf}\n")
    

        

def main():
    """
    Main function to execute the Open Reading Frame (ORF) analysis pipeline.

    This function creates an instance of the ORFFinder class, reads the DNA sequence
    from the input file, transforms the sequence, generates reading frames, identifies
    start and stop codons, finds ORFs, translates ORFs into protein sequences, and
    writes the results to the output file.

    Returns:
        None
    """
    orf_finder = ORFFinder()
    orf_finder.read_sequence()
    orf_finder.transform_sequence()
    orf_finder.generate_reading_frames()
    orf_finder.find_start()
    orf_finder.find_stop()
    orf_finder.find_orf()
    orf_finder.translate_orf()
    orf_finder.remove_duplicates()
    orf_finder.write_result()

if __name__ == "__main__":
    main()