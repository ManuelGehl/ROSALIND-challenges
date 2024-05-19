from pathlib import Path

class OverlapGraph:
    
    DEFAULT_INPUT_PATH = Path("input.txt")
    DEFAULT_OUTPUT_PATH = Path("output.txt")
    
    def __init__(self, input_path=None, output_path=None):
        """
        Initializes the OverlapGraph object with optional input and output file paths.
        
        Args:
            input_path (str or Path, optional): Path to the input file containing sequences. Defaults to 'input.txt'.
            output_path (str or Path, optional): Path to the output file for the adjacency list. Defaults to 'output.txt'.
        """

        self.input_path = Path(input_path) if input_path else self.DEFAULT_INPUT_PATH
        self.output_path = Path(output_path) if output_path else self.DEFAULT_OUTPUT_PATH
        self.sequences = []
        self.overlap_length = None
        
    def read_sequences(self) -> None:
        """
        Reads sequences from the input file and sets the overlap length.
        
        Raises:
            FileNotFoundError: If the input file does not exist or is empty.
        """
            
        # Check if file exists
        if not self.input_path.exists():
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        # Check if file is not empty
        if self.input_path.stat().st_size == 0:
            raise FileNotFoundError(f"Empty file")
            
        # Read all sequences from file
        with open(self.input_path, "r") as file:
            lines = file.readlines()
            self.sequences = [sequence.strip() for sequence in lines]
        
        # Save overlap length of sequences (k - 1)
        self.overlap_length = len(self.sequences[0]) - 1
    
    def construct_graph(self) -> list:
        """
        Constructs the overlap graph as an adjacency list.
        
        Returns:
            list: A sorted adjacency list where each element is a tuple (sequence, matching_sequences).
        """
        
        # Initialize adjacency list
        adjacency_list = []
        # Loop trough sequences
        for sequence in self.sequences:
            # Determine suffix of current sequence and find matchin sequences with suffix = prefix
            suffix = sequence[-self.overlap_length:]
            matched_sequences = [sequence for sequence in self.sequences if sequence.startswith(suffix)]
            # If current sequence has a matching sequence, add to graph
            if matched_sequences:
                adjacency_list.append((sequence, " ".join(matched_sequences)))
            else:
                continue
        
        # Sort adjacency list
        sorted_adjacency_list = sorted(adjacency_list, key=lambda x: x[0])
        return sorted_adjacency_list
    
    def output(self, adjacency_list: list) -> None:
        """
        Writes the adjacency list to the output file.
        
        Args:
            adjacency_list (list): The adjacency list to be written to the output file.
        """
        
        with open(self.output_path, "w") as file:
            for edge in adjacency_list:
                file.write(f"{edge[0]} -> {edge[1]}\n")
        
# ------------------------------------------------------------

def main():
    """
    Main function to execute the OverlapGraph operations: read sequences, construct the graph, and output the result.
    """
    
    overlap_graph = OverlapGraph()
    overlap_graph.read_sequences()
    graph = overlap_graph.construct_graph()
    overlap_graph.output(graph)
    print("Done")


if __name__ == "__main__":
    main()