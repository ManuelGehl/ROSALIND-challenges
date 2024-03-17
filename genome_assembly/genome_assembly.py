from utility.fasta_reader import read_fasta
import os


class GenomeAssembly:
    
    def __init__(self, input_path="data.txt"):

        self.input_path = input_path
        self.sequences = None
        self.matrix = None
        self.transposed_matrix = None
        
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
    
    def suffix_matrix(self) -> None:
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
        
        self.matrix = suffix_matrix
    
    def transpose_suffix_matrix(self) -> None:
        self.transposed_matrix = [list(row) for row in zip(*self.matrix.values())]
     
    def find_terminus(self):
        # First find the read will be placed at the 3' end since it has the lowest sum of passed suffix scores
        suffix_sums = {sequence: sum(suffix_score) for sequence, suffix_score in self.matrix.items()}
        terminus = min(suffix_sums, key=lambda seq: suffix_sums[seq])
        # Determine id of terminus
        terminus_id = self.sequences.index(terminus)
        return terminus_id
    
    def next_prefix(self, identifier):
        max_score = max(self.transposed_matrix[identifier])
        prefix_id = self.transposed_matrix[identifier].index(max_score)
        
        return prefix_id, max_score
    
    def assemble(self):
        
        for step in range(len(self.sequences) - 1):
            if step == 0:
                # Start with terminus of sequence
                term_id = self.find_terminus()
                term_seq = self.sequences[term_id]
                prefix_id, max_score = self.next_prefix(identifier=term_id)
                # Trim 3' part of prefix according to score
                trimmed_prefix = self.sequences[prefix_id][:-max_score]
                # Fuse sequences
                fused_seq = trimmed_prefix + term_seq
            else:
                # Change prefix_id to suffix_id
                suffix_id = prefix_id
                # Determine next prefix
                prefix_id, max_score = self.next_prefix(identifier=suffix_id)
                # Trim 3' part of prefix according to score
                trimmed_prefix = self.sequences[prefix_id][:-max_score]
                # Fuse sequences
                fused_seq = trimmed_prefix + fused_seq
        
        print(fused_seq)
                
                



def main():
    tester = GenomeAssembly()
    tester.read_sequences()
    tester.suffix_matrix()
    tester.transpose_suffix_matrix()
    tester.assemble()

if __name__ == "__main__":
    main()