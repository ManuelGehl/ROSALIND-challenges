from pathlib import Path

class BruijnGraphString:
    
    DEFAULT_INPUT_PATH = Path("input.txt")
    DEFAULT_OUTPUT_PATH = Path("output.txt")
    
    def __init__(self, input_path=None, output_path=None):
        """
        Initializes the BruijnGraphString with specified input and output paths.
        
        Args:
            input_path (str, optional): Path to the input file. Defaults to "input.txt".
            output_path (str, optional): Path to the output file. Defaults to "output.txt".
        """

        self.input_path = Path(input_path) if input_path else self.DEFAULT_INPUT_PATH
        self.output_path = Path(output_path) if output_path else self.DEFAULT_OUTPUT_PATH
        self.sequence = None
        self.k_mer_size = None
        
    def read_sequence(self) -> None:
        """
        Reads the sequence and k-mer size from the input file.
        
        Raises:
            FileNotFoundError: If the input file does not exist or is empty.
        """

        # Check if file exists
        if not self.input_path.exists():
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        # Check if file is not empty
        if self.input_path.stat().st_size == 0:
            raise FileNotFoundError(f"Empty file")
            
        # Read sequence and k-mer size from file
        with open(self.input_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()
                # If line starts with number, assign k-mer size
                if line[0].isdigit():
                    self.k_mer_size = int(line)
                elif line[0].isalpha():
                    self.sequence = line
        
    def create_k_mers(self) -> set:
        """
        Creates a set of unique k-mers from the sequence.
        
        Returns:
            set: A set of k-mers.
        """
        
        # Raise error if inputs are missing
        if self.sequence is None or self.k_mer_size is None:
            raise ValueError("Sequence or k-mer size not initialized")
        
        # Create k_mers
        k_mer_pool = set()
        for position in range(len(self.sequence) - self.k_mer_size + 1):
            k_mer_pool.add(self.sequence[position:position + self.k_mer_size])

        return k_mer_pool
    
    def construct_graph(self, k_mers: set) -> list:
        """
        Constructs the De Bruijn graph from the k-mers.
        
        Args:
            k_mers (set): A set of k-mers.
        
        Returns:
            list: The adjacency list representing the De Bruijn graph.
        """
        
        # Construct nodes from unique fragments
        nodes = set()
        for k_mer in k_mers:
            nodes.add(k_mer[:-1])
            nodes.add(k_mer[1:])

        # Construct edges
        adjacency_list = []
        # Loop trough nodes
        for node in nodes:
            # Determine suffix of current node and find matching nodes with suffix = prefix
            suffix = node[1:]
            matched_nodes = sorted([matched_node for matched_node in nodes if matched_node.startswith(suffix)])
            # Only add edge if overlap occured
            if matched_nodes:
                adjacency_list.append(tuple([node] + matched_nodes))

        # Return sorted adjacency list
        return sorted(adjacency_list)
        
    def output(self, adjacency_list: list) -> None:
        """
        Writes the adjacency list to the output file.
        
        Args:
            adjacency_list (list): The adjacency list to be written to the output file.
        """
        
        with open(self.output_path, "w") as file:
            for counter, edge in enumerate(adjacency_list):
                node_1, node_2 = edge[0], ",".join(edge[1:])
                if counter < len(adjacency_list) - 1:
                    file.write(f"{node_1} -> {node_2}\n")
                else:
                    # Write without final line break
                    file.write(f"{node_1} -> {node_2}")
                    
# ------------------------------------------------------------

def main():
    
    de_bruijn_graph = BruijnGraphString()
    de_bruijn_graph.read_sequence()
    k_mers = de_bruijn_graph.create_k_mers()
    graph = de_bruijn_graph.construct_graph(k_mers)
    de_bruijn_graph.output(graph)
    print("Finished construction of De Bruijn graph")

if __name__ == "__main__":
    main()