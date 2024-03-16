from utility.fasta_reader import read_fasta
import os


class GenomeAssembly:
    
    def __init__(self, input_path="data.txt"):

        self.input_path = input_path
        self.matrix = None
        
    def read_sequences(self) -> list:
            
        # Check if file exists
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        # Check if file is not empty
        if os.stat(self.input_path).st_size == 0:
            raise FileNotFoundError(f"Empty file")
            
        # Read all sequences from file
        seq_dict = read_fasta(self.input_path)
        
        # Output sequences
        return [sequence for sequence in seq_dict.values()]
    
    def suffix_matrix(self, sequences: list) -> dict:
        """
        Calculate the suffix matrix to determine the maximum overlapping substrings between all sequences.
        The entries are the suffix score, which is the maximum number of overlapping nucleotides from the 
        3' end of the sequence in the column with the 5' end of the sequence in the row.

        Args:
            sequences (list): A list of input sequences.

        Returns:
            dict: A suffix matrix with all sequences as columns and rows and the suffix score indicating the maximum overlapping substring length.
            
        Example:
        >>> sequences = ['ATTAGACCTG', 'AGACCTGCCG']
        >>> suffix_matrix(sequences)
            {'ATTAGACCTG': [0, 7], 'AGACCTGCCG': [0, 0]}
            # That means the 2nd sequence has a suffix score of 7 since AGACCTG overlapps with 1st sequence.
        """
        # Initialize suffix matrix with 0s
        suffix_matrix = {sequence: 0 for sequence in sequences}
        
        # Iterate over sequences
        for matrix_sequence in suffix_matrix.keys():
            suffix_score = []
            for sequence in sequences:
                # If sequences are identical set suffix score to 0
                if matrix_sequence == sequence:
                    suffix_score.append(0)
                else:
                    for position in range(len(sequence), 0, -1):
                        current_window = sequence[:position]
                        # Check if the current window matches the suffix of the matrix sequence
                        if current_window == matrix_sequence[-position:]:
                            suffix_score.append(position)
                            break
                        # If sequences have no overlap at all, score 0
                        if position == 1:
                            suffix_score.append(0)
            suffix_matrix[matrix_sequence] = suffix_score
        
        return suffix_matrix

def main():
    tester = GenomeAssembly()
    seq = tester.read_sequences()
    seq = [seq[0], seq[2]]
    matrix = tester.suffix_matrix(sequences=seq)
    print(matrix)

if __name__ == "__main__":
    main()