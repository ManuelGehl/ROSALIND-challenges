from utility.fasta_reader import read_fasta
import os


class GenomeAssembly:
    
    def __init__(self, input_path="data.txt"):

        self.input_path = input_path
        self.matrix = None
        self.sequences = None
        
    def read_sequences(self) -> None:
            
        # Check if file exists
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        # Check if file is not empty
        if os.stat(self.input_path).st_size == 0:
            raise FileNotFoundError(f"Empty file")
            
        # Read all sequences from file
        seq_dict = read_fasta(self.input_path)
        
        # Output sequences
        self.sequences = [sequence for sequence in seq_dict.values()]
    
    def suffix_matrix(self) -> dict:
        """
        Calculate the suffix matrix to determine the maximum overlapping substrings between all sequences.
        The entries are the suffix score, which is the maximum number of overlapping nucleotides from the 
        3' end of the sequence in the column with the 5' end of the sequence in the row.

        Returns:
            dict: A suffix matrix with all sequences as columns and rows and the suffix score indicating the maximum overlapping substring length.
            
        Example:
        >>> sequences = ['ATTAGACCTG', 'AGACCTGCCG']
        >>> suffix_matrix(sequences)
            {'ATTAGACCTG': [0, 7], 'AGACCTGCCG': [0, 0]}
            # That means the 2nd sequence has a suffix score of 7 since AGACCTG overlapps with 1st sequence.
        """
        # Initialize suffix matrix with 0s
        suffix_matrix = {sequence: 0 for sequence in self.sequences}
        
        # Iterate over sequences
        for matrix_sequence in suffix_matrix.keys():
            suffix_score = []
            for sequence in self.sequences:
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
    
    def assemble(self, suffix_matrix: dict) -> str:
        pass
        

        
    def find_terminus(self, suffix_matrix):
        # First find the read will be placed at the 3' end since it has the lowest sum of passed suffix scores
        suffix_sums = {sequence: sum(suffix_score) for sequence, suffix_score in suffix_matrix.items()}
        terminus = min(suffix_sums, key=lambda seq: suffix_sums[seq])
        # Determine id of terminus
        terminus_id = self.sequences.index(terminus)
    
    # TO do 
    def next_prefix(self, identifier):
               # Find the highest suffix score for terminus
        highest_score = 0
        for seq, scores in suffix_matrix.items():
            if scores[terminus_id] > highest_score:
                highest_score = scores[terminus_id]
                next_prefix = seq
    
    
    
    # Find next prefix
    # Fuse sequences
                
            
     




def main():
    tester = GenomeAssembly()
    tester.read_sequences()
    matrix = tester.suffix_matrix()
    tester.assemble(matrix)

if __name__ == "__main__":
    main()