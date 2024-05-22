from pathlib import Path

class BruijnGraphCollection:
    
    DEFAULT_INPUT_PATH = Path("input.txt")
    DEFAULT_OUTPUT_PATH = Path("output.txt")
    
    def __init__(self, input_path=None, output_path=None):


        self.input_path = Path(input_path) if input_path else self.DEFAULT_INPUT_PATH
        self.output_path = Path(output_path) if output_path else self.DEFAULT_OUTPUT_PATH
        self.sequences = []
        self.k_mer_size = None
        
    def read_sequences(self) -> None:


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
    
    de_bruijn_graph = BruijnGraphCollection()
    de_bruijn_graph.read_sequences()
    nodes = de_bruijn_graph.create_edges()
    de_bruijn_graph.output(nodes)
    print("Finished construction of De Bruijn graph")

if __name__ == "__main__":
    main()