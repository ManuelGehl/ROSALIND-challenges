from pathlib import Path
import random
import itertools
import logging
from configure_logging import setup_logging

class EulerianPath:
    """
    A class to represent and compute Eulerian paths in a directed graph.

    Attributes:
    ----------
    DEFAULT_INPUT_PATH : Path
        Default path to the input file.
    DEFAULT_OUTPUT_PATH : Path
        Default path to the output file.
    input_path : Path
        Path to the input file specified by the user or default.
    output_path : Path
        Path to the output file specified by the user or default.
    graph : dict
        Dictionary representing the directed graph.
    additional_edge : dict
        Dictionary to keep track of additional edge added to make the graph balanced.
    logger : logging.Logger
        Logger instance for the class.

    Methods:
    -------
    read_input() -> None
        Reads and parses the input file to construct the graph.
    output_path(path: list) -> None
        Writes the Eulerian path to the output file.
    graph_balance() -> dict
        Calculates the balance of each node in the graph.
    graph_cycle() -> None
        Transforms the graph to a cycle by adding an artificial edge if necessary.
    starting_node(walked_path: list, unused_edges: dict) -> str
        Selects the starting node for walking the graph.
    next_node(unused_edges: dict, current_node: str) -> str
        Selects the next node to walk to from the current node.
    remove_edge(unused_edges: dict, walked_path: list) -> dict
        Removes an edge from the graph once it has been walked.
    new_walk(unused_edges: dict, walked_path: list) -> tuple[dict, list]
        Starts a new walk when no further path can be found from the current node.
    walk_graph() -> list
        Walks through the graph to find an Eulerian path.
    linearize_path(walked_path: list) -> list
        Linearizes the Eulerian cycle to form the Eulerian path by removing the artificial edge.
    """
    
    DEFAULT_INPUT_PATH = Path("input.txt")
    DEFAULT_OUTPUT_PATH = Path("output.txt")
    
    def __init__(self, input_path=None, output_path=None):
        """
        Initializes the EulerianPath with input and output paths.

        Parameters:
        ----------
        input_path : str or Path, optional
            Path to the input file (default is None).
        output_path : str or Path, optional
            Path to the output file (default is None).
        """
        
        self.input_path = Path(input_path) if input_path else self.DEFAULT_INPUT_PATH
        self.output_path = Path(output_path) if output_path else self.DEFAULT_OUTPUT_PATH
        self.graph = {}
        self.additional_edge = {}
        self.logger = logging.getLogger(__name__)

    # Input/Output methods
    def read_input(self) -> None:
        """
        Reads and parses the input file to construct the graph.

        Raises:
        ------
        FileNotFoundError
            If the input file is not found or is empty.
        """

        self.logger.debug(f"Reading input from {self.input_path}")
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
                # Line should be in format: Node_1 -> Node_2 (Node_2 can consists of several nodes)
                # Split string at whitespaces and keep first node and second node(s)
                node_1, _, node_2 = line.split()
                # If node_2 has more than 2 elements, split again
                if len(node_2) > 1:
                    self.graph[node_1] = node_2.split(",")
                else:
                    self.graph[node_1] = [node_2]
    
        self.logger.debug(f"Graph loaded: {self.graph}")

    def output_result(self, path: list) -> None:
        """
        Writes the Eulerian path to the output file.

        Parameters:
        ----------
        path : list
            The Eulerian path to be written to the file.
        """
        
        joint_string = "->".join(path)
        with open(self.output_path, "w") as file:
            file.write(joint_string)
        self.logger.info(f"Output written to {self.output_path}")
    
    # Graph Processing Methods
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
    
# ------------------------------------------------------------

def main():
    setup_logging()
    eulerian_path = EulerianPath()
    eulerian_path.read_input()
    eulerian_path.graph_cycle()
    walked_path = eulerian_path.walk_graph()
    linear_path = eulerian_path.linearize_path(walked_path=walked_path)
    eulerian_path.output_result(linear_path)
    logging.info("Finished construction of Eulerian path")
    print("Finished construction of Eulerian path")

if __name__ == "__main__":
    main()