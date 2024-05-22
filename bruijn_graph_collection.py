from pathlib import Path

class BruijnGraphCollection:
    """
    A class to represent and process De Bruijn graphs from DNA sequences.

    Attributes
    ----------
    DEFAULT_INPUT_PATH : Path
        Default path to the input file containing sequences.
    DEFAULT_OUTPUT_PATH : Path
        Default path to the output file for storing graph edges.
    input_path : Path
        Path to the input file containing sequences.
    output_path : Path
        Path to the output file for storing graph edges.
    sequences : list
        List of sequences read from the input file.
    """
    
    DEFAULT_INPUT_PATH = Path("input.txt")
    DEFAULT_OUTPUT_PATH = Path("output.txt")
    
    def __init__(self, input_path=None, output_path=None):
        """
        Initialize the BruijnGraphCollection with optional input and output paths.

        Parameters
        ----------
        input_path : str or Path, optional
            Path to the input file. Defaults to 'input.txt'.
        output_path : str or Path, optional
            Path to the output file. Defaults to 'output.txt'.
        """
        
        self.input_path = Path(input_path) if input_path else self.DEFAULT_INPUT_PATH
        self.output_path = Path(output_path) if output_path else self.DEFAULT_OUTPUT_PATH
        self.sequences = []
        
    def read_sequences(self) -> None:
        """
        Read sequences from the input file and store them in the sequences attribute.

        Raises
        ------
        FileNotFoundError
            If the input file does not exist or is empty.
        """

        # Check if file exists
        if not self.input_path.exists():
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        # Check if file is not empty
        if self.input_path.stat().st_size == 0:
            raise FileNotFoundError(f"Empty file")
            
        # Read sequences from file
        with open(self.input_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                self.sequences.append(line)
        
    def create_edges(self) -> set:
        """
        Create edges of the De Bruijn graph from the sequences.

        Returns
        -------
        dict
            Dictionary representing the edges of the graph where keys are nodes and values are lists of connected nodes.

        Raises
        ------
        ValueError
            If sequences are not initialized.
        """
        
        # Raise error if inputs are missing
        if self.sequences is None:
            raise ValueError("Sequence not initialized")
        
        edges = {}
        for sequence in self.sequences:
            node_1, node_2 = sequence[:-1], sequence[1:]
            edges.setdefault(node_1, []).append(node_2)
        
        # Return sorted edges
        return {key: sorted(values) for key, values in sorted(edges.items())}

    def output(self, edges: dict) -> None:
        """
        Output the edges of the De Bruijn graph to the output file.

        Parameters
        ----------
        edges : dict
            Dictionary representing the edges of the graph where keys are nodes and values are lists of connected nodes.
        """
        
        with open(self.output_path, "w") as file:
            for counter, edge in enumerate(edges.items()):
                node_1, node_2 = edge[0], ",".join(edge[1])
                if counter < len(edges) - 1:
                    file.write(f"{node_1} -> {node_2}\n")
                else:
                    # Write without final line break
                    file.write(f"{node_1} -> {node_2}")
                    
# ------------------------------------------------------------

def main():
    """
    Main function to construct the De Bruijn graph from input sequences and output the edges.
    """
    
    de_bruijn_graph = BruijnGraphCollection()
    de_bruijn_graph.read_sequences()
    nodes = de_bruijn_graph.create_edges()
    de_bruijn_graph.output(nodes)
    print("Finished construction of De Bruijn graph")

if __name__ == "__main__":
    main()