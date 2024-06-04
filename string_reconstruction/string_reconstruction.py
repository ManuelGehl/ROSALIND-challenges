from pathlib import Path
import random
import itertools
import logging
from log_files.configure_logging import setup_logging

class StringReconstruction:
    
    
    DEFAULT_INPUT_PATH = Path("input.txt")
    DEFAULT_OUTPUT_PATH = Path("output.txt")
    
    def __init__(self, input_path=None, output_path=None):
        """
        Initialize the StringReconstruction object with input and output file paths.

        Parameters:
        ----------
        input_path : str or Path, optional
            Path to the input file containing sequences (default is "input.txt").
        output_path : str or Path, optional
            Path to the output file to write the reconstructed string (default is "output.txt").
        """
        
        # Setup logging
        setup_logging()
    
        self.input_path = Path(input_path) if input_path else self.DEFAULT_INPUT_PATH
        self.output_path = Path(output_path) if output_path else self.DEFAULT_OUTPUT_PATH
        self.sequences = []
        self.graph = {}
        self.additional_edge = {}
        self.logger = logging.getLogger(__name__)

    def read_sequences(self) -> None:
        """
        Read sequences from the input file and store them in the sequences list.

        Raises:
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
                if line.isalpha():
                    self.sequences.append(line)
        self.logger.debug(f"Sequences read: {self.sequences}")
        
    def create_edges(self) -> set:
        """
        Create edges for the De Bruijn graph from the sequences and store them in the graph dictionary.

        Raises:
        ------
        ValueError
            If sequences are not initialized.
        """
        
        # Raise error if inputs are missing
        if self.sequences is None:
            raise ValueError("Sequence not initialized")
        
        edges = {}
        for sequence in self.sequences:
            prefix, suffix = sequence[:-1], sequence[1:]
            edges.setdefault(prefix, []).append(suffix)
            self.logger.debug(f"Edge found: {prefix, suffix}")
        
        # Return sorted edges
        self.graph = {key: sorted(values) for key, values in sorted(edges.items())}
    
    
    def graph_balance(self) -> dict:
        """
        Calculates the balance of each node in the graph.

        Returns:
        -------
        dict
            A dictionary with nodes as keys and their balance (incoming and outgoing edges) as values.
        """
        
        self.logger.debug("Calculating graph balance")
        # Identify all unique nodes in the graph
        nodes = set(list(self.graph.keys()) + list(itertools.chain(*self.graph.values())))
        # Setup dictionary to count incoming edges and outgoing edges
        balance_dict = {node: [0, 0] for node in nodes}
        
        # Count incoming edges in concatenated list
        concatenated_nodes = list(itertools.chain(*self.graph.values()))
        for node in balance_dict.keys():
            incoming_nodes = concatenated_nodes.count(node)
            balance_dict[node][0] = incoming_nodes
        
        # Count outgoing edges
        for node in balance_dict.keys():
            outgoing_nodes = len(self.graph.get(node, []))
            balance_dict[node][1] = outgoing_nodes
        self.logger.debug(f"Balance dictionary: {balance_dict}")
        return balance_dict
    
    def graph_cycle(self) -> None:
        """
        Transforms the graph to a cycle by adding an artificial edge if necessary.
        """
        
        self.logger.debug("Transform graph to cycle")
        # Find first and last node
        balance_dictionary = self.graph_balance()
        # Initialize variables
        first_node = None
        last_node = None
        for key, values in balance_dictionary.items():
            # Determine last node
            if values[1] < values[0]:
                last_node = key
                self.logger.debug(f"Found last_node : {last_node}")
            # Determine first node
            elif values[1] > values[0]:
                first_node = key
                self.logger.debug(f"Found first_node : {first_node}")

        # Add artifical edge to connect last node with first node to create balanced graph
        self.graph[last_node] = [first_node]
        self.additional_edge[last_node] = [first_node]
        self.logger.debug(f"Additional edge found: {self.additional_edge}")
        self.logger.debug(f"Graph after adding artificial edge: {self.graph}")   
    
    # Path Construction Methods   
    def starting_node(self,walked_path: list, unused_edges: dict) -> str:
        """
        Selects the starting node for walking the graph.

        Parameters:
        ----------
        walked_path : list
            List of nodes in the walked path.
        unused_edges : dict
            Dictionary of unused edges in the graph.

        Returns:
        -------
        str
            The starting node.
        """
        
        # Pick starting node
        if len(walked_path) == 0:
            # Pick first node in graph
           return list(unused_edges.keys())[0]
        else:
            # Take second node of last walk
            return walked_path[1]
    
    def next_node(self, unused_edges: dict, current_node: str) -> str:
        """
        Selects the next node to walk to from the current node.

        Parameters:
        ----------
        unused_edges : dict
            Dictionary of unused edges in the graph.
        current_node : str
            The current node in the walk.

        Returns:
        -------
        str
            The next node to walk to.
        """
        
        # Pick next node from graph and check if there are multiple possibilities
        next_node = unused_edges.get(current_node, None)
        if next_node is None:
            return None
        elif len(next_node) == 1:
            return "".join(next_node)
        else:
            # Pick one path randomly
            return random.choice(next_node)
    
    def remove_edge(self, unused_edges: dict, walked_path: list) -> dict:
        """
        Removes an edge from the graph once it has been walked.

        Parameters:
        ----------
        unused_edges : dict
            Dictionary of unused edges in the graph.
        walked_path : list
            List of nodes in the walked path.

        Returns:
        -------
        dict
            Updated dictionary of unused edges.
        """
        
        # Remove one edge based on the last 2 nodes in walked path
        # Determine if input node has several output nodes
        node_1, node_2 = walked_path[-2:]
        if len(unused_edges[node_1]) == 1:
            del unused_edges[node_1]
            #unused_edges.pop(node_1, None)
        else:
            unused_edges[node_1].remove(node_2)
        self.logger.debug(f"Removed edge from {node_1} to {node_2}. Remaining edges: {unused_edges}")
        return unused_edges
    
    def new_walk(self, unused_edges: dict, walked_path: list) -> tuple[dict, list]:
        """
        Starts a new walk when no further path can be found from the current node.

        Parameters:
        ----------
        unused_edges : dict
            Dictionary of unused edges in the graph.
        walked_path : list
            List of nodes in the walked path.

        Returns:
        -------
        tuple
            Updated dictionary of unused edges and walked path.
        """
        # Determine first node in walked path that still has unexplored edges
        new_starting_node = None
        for node in walked_path:
            if node in unused_edges:
                new_starting_node = node
                break
        
        # Raise error if there is no unexplored edge
        if new_starting_node is None:
            raise ValueError("No unexplored edge found!")
        
        # Rearange walked_path so that new_starting_node is first element in list
        # and all former elements before new_starting_node are pushed to the end of the list
        starting_index = walked_path.index(new_starting_node)
        modified_path = walked_path[starting_index:] + walked_path[1:starting_index + 1]
        
        self.logger.debug(f"New walk started. Unused edges: {unused_edges}, Walked path: {walked_path}")
        return (unused_edges, modified_path)
    
    def walk_graph(self) -> list:
        """
        Walks through the graph to find an Eulerian path.

        Returns:
        -------
        list
            List of nodes representing the walked Eulerian path.
        """
        
        self.logger.debug("Walking the graph")
        # Initialize a dictionary with unused edges
        unused_edges = self.graph.copy()
        # Initialize a list to track walked path with first node
        walked_path = [list(unused_edges.keys())[0]]
        # Initialize next node as empty string
        next_node = str()
        
        while len(unused_edges) != 0:
            current_node = walked_path[-1]
            next_node = self.next_node(unused_edges=unused_edges, current_node=current_node)
            # If next node = None, then an early stop is reached
            if next_node is None:
                # Update unused_edges and walked_path
                self.logger.debug(f"Early stopp: {walked_path}")
                unused_edges, walked_path = self.new_walk(unused_edges=unused_edges, walked_path=walked_path)
            else:
                walked_path.append(next_node)
                self.logger.debug(f"Walked path: {walked_path}")
                # Remove edge from unused eges
                unused_edges = self.remove_edge(unused_edges=unused_edges, walked_path=walked_path)
        
        return walked_path
    
    def linearize_path(self, walked_path: list) -> list:
        """
        Linearize a walked path in a graph.

        Args:
            walked_path (list): A list representing the walked path in the graph.

        Returns:
            list: A linearized path obtained by splitting the walked path at the position of the ending node,
                and reordering the segments to ensure overlap.

        Raises:
            ValueError: If the walked path cannot be split into left and right parts due to lack of overlap.
        """
        self.logger.debug(f"Start linearizing graph.")
        # Split walked path at position of ending node
        ending_node_position = walked_path.index(str(*list(self.additional_edge.keys())))
        self.logger.debug(f"Ending node position: {ending_node_position}")
        left_part = walked_path[:ending_node_position+1]
        right_part = walked_path[ending_node_position+1:]
        self.logger.debug(f"left_part: {left_part}")
        self.logger.debug(f"right_part: {right_part}")
        # Check that right part and left part overlap
        if right_part[-1] != left_part[0]:
            raise ValueError("Walked path cannot be split!")
        linearized_path = right_part + left_part[1:]
        self.logger.debug(f"Linearized path: {linearized_path}")
        
        return linearized_path
    
    def sequence_reconstruction(self, linearized_path: list) -> str:
        """
        Reconstruct the sequence from the linearized path.

        Parameters:
        ----------
        linearized_path : list
            A list representing the linearized path in the graph.

        Returns:
        -------
        str
            The reconstructed sequence.
        """
        
        reconstruction_list = []
        for counter, node in enumerate(linearized_path):
            if counter == 0:
                reconstruction_list.append(node)
            else:
                reconstruction_list.append(node[-1])
        
        self.logger.debug(f"Reconstruction list: {reconstruction_list}")
        
        # Join to string
        reconstructed_string = "".join(reconstruction_list)
        self.logger.debug(f"Reconstructed string: {reconstructed_string}")
        
        return reconstructed_string
    
    def output_reconstructed_string(self, reconstructed_string:str) -> None:
        """
        Write the reconstructed string to the output file.

        Parameters:
        ----------
        reconstructed_string : str
            The reconstructed string to be written to the file.
        """
        
        with open(self.output_path, "w") as file:
            file.write(reconstructed_string)
        self.logger.info(f"Output written to {self.output_path}")
            
            

    
                    
# ------------------------------------------------------------

def main():
    """
    Main function to construct the De Bruijn graph from input sequences and output the edges.
    """
    
    string_reconstructor = StringReconstruction()
    string_reconstructor.read_sequences()
    string_reconstructor.create_edges()
    string_reconstructor.graph_cycle()
    walked_path = string_reconstructor.walk_graph()
    linear_path = string_reconstructor.linearize_path(walked_path=walked_path)
    reconstructed_string = string_reconstructor.sequence_reconstruction(linear_path)
    string_reconstructor.output_reconstructed_string(reconstructed_string)
    logging.info("Finished construction of Eulerian path")
    print("Finished assembly!")

if __name__ == "__main__":
    main()