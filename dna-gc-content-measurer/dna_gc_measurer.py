class GCMeasurer:
    """
    A class for measuring GC content in DNA sequences.
    """
    
    def __init__(self, input_path="data.txt", output_path="result.txt"):
        """
        Initialize the GCMeasurer object.
        
        Parameters:
            - input_path (str): Path to the input file
            - output_path (str): Path to the output file
        """
        self.input_path = input_path
        self.output_path = output_path
        self.sequences = None
        self.gc_content = None
        self.highest_gc = None
       
        
    def read_sequence(self):
        """
        Read DNA sequences from FASTA file.
        """
        
        # Define containers for id and sequence
        current_id = ""
        current_seq = ""
        sequence_dict = {}
        
        
        with open(self.input_path) as file:
            for line in file:
                line = line.strip()
                if line.startswith(">"):
                    # Check if current_id was filled in iteration before
                    if current_id:
                        sequence_dict[current_id] = current_seq.upper()
                    
                    # For first iteration
                    current_id = line.split(">")[-1]
                    current_seq = ""
                # If sequence line concatenate sequences of each line
                else:
                    current_seq += line

            # After the loop, add the last pair
            if current_id:
                sequence_dict[current_id] = current_seq.upper()
                
        self.sequences = sequence_dict
    
    def measure_gc(self):
        """
        Measure GC content for each DNA sequence.
        """
        self.gc_content = {
            seq_id: 100 * ((seq.count("G") + seq.count("C")) / len(seq))
            for seq_id, seq in self.sequences.items()
            }
    
    def evaluate_gc(self):
        """
        Sort dictionary according to highest GC content.
        Highest content on top.
        """
        sorted_dict = dict(sorted(self.gc_content.items(), 
                                  key=lambda item: item[1], 
                                  reverse=True))
        highest_gc = next(iter(sorted_dict.items()))
        self.highest_gc = highest_gc
        
        
    
    def write_file(self):
        """
        Write the result in a txt-file. Sequence_ID from FASTA header
        and in next line GC content.
        """
        with open(self.output_path, "w") as file:
            file.write(f"{self.highest_gc[0]}\n")
            file.write(f"{self.highest_gc[1]}")
            

def main():
    measurer = GCMeasurer()
    measurer.read_sequence()
    measurer.measure_gc()
    measurer.evaluate_gc()
    measurer.write_file()
    


if __name__ == "__main__":
    main()