# Import FASTA reading function
import sys
sys.path.append("../Utility")
from fasta_utils import read_fasta


class ConsensusFinder:
    """
    Class for reading multiple DNA sequences from a FASTA file
    and computing the profil matrix and the resulting consensus sequence
    """
    
    def __init__(self, input_path=None, output_path=None):
        """
        Initialize ConsensusFinder with input and output file paths.

        Parameters:
        - input_path (str): Path to the input file containing DNA sequences. Default is None.
        - output_path (str): Path to the output file for storing profil matrix and consensus sequence. Default is None.
        """
        if input_path is None:
            input_path = "data.txt"
        if output_path is None:
            output_path = "result.txt"
        self.input_path = input_path
        self.output_path = output_path
        self.dna_sequences = None
        self.consensus_seq = None
        self.profile_mat = None
        
    def read_sequence(self):
        """
        Read DNA sequences from FASTA file.
        """
        self.dna_sequences = read_fasta(self.input_path)
    
    def profile_matrix(self):
        """
        Compute the profile matrix from the DNA sequences.
        The profile matrix represents the frequency of each nucleotide (A, C, G, T) at each position in the sequences.
       
        """
        # Check if sequence has been read already
        if self.dna_sequences is None:
            raise ValueError("DNA sequences not read. Call read_sequence() first.")
        
        # Compute sequences so that each nucleotide at the same position in
        # all the sequences are combined in one list 
        # e.i. shape = [[Pos_1], [Pos_2], ..., [Pos_i]]
        sequence_list = list(self.dna_sequences.values())
        transposed_seq = ["".join(char) for char in zip(*sequence_list)]
        
        # Create profile matrix with rows A, C, G, T and columns equal to the
        # sequence length
        matrix = {
            "A": [],
            "C": [],
            "G": [],
            "T": []
            }
        
        for pos in transposed_seq:
            count_A = pos.count("A")
            count_C = pos.count("C")
            count_G = pos.count("G")
            count_T = pos.count("T")
            matrix["A"].append(count_A)
            matrix["C"].append(count_C)
            matrix["G"].append(count_G)
            matrix["T"].append(count_T)
        
        self.profile_mat = matrix
        
    def consensus(self):
        """
        Compute the consensus sequence from the profile matrix.
        """
    
        # Check if profile matrix has been computed.
        if self.profile_mat is None:
            raise ValueError("Profile matrix not computed. Call profile_matrix() first.")
        
        # Define dictionary for nucleotide mapping
        map_dict = {0: "A", 1: "C", 2: "G", 3: "T"}
        # Transpose profile matrix to the shape (positions, ACGT)
        transposed_mat = [list(counter) for counter in zip(*self.profile_mat.values())]
        # Compute position in lists with highest value
        max_index = [pos.index(max(pos)) for pos in transposed_mat]
        consensus_seq = [map_dict[pos] for pos in max_index]
        self.consensus_seq = "".join(consensus_seq)
        
    def write_results(self):
        """
        Writes the consensus sequence and profile matrix to the output file.
        """
        if self.consensus_seq is None or self.profile_mat is None:
            raise ValueError("Consensus sequence or profile matrix not computed. Call consensus() and profile_matrix() first.")
            
        with open(self.output_path, "w") as file:
            # Write consensus sequence
            file.write(self.consensus_seq + "\n")
            for key, value in self.profile_mat.items():
                joint_matrix_row = " ".join([str(value) for value in value])
                file.write(str(key) + ": " + joint_matrix_row + "\n")
            
def main():
    consensus_finder = ConsensusFinder()
    consensus_finder.read_sequence()
    consensus_finder.profile_matrix()
    consensus_finder.consensus()
    consensus_finder.write_results()
    
    
if __name__ == "__main__":
    main()