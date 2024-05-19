from pathlib import Path
import os
from functions.neighbourhood import generate_d_neighbourhood as neighbourhood_func

class MotifEnumeration:
    """
    A class to perform motif enumeration with given k-mer size and Hamming distance.

    Attributes:
        input_path (str): Path to the input file.
        sequences (list): List of DNA sequences.
        k_size (int): Size of the k-mers.
        distance (int): Maximum Hamming distance.
        neighbourhood (dict): Dictionary of sequences and their k-mers.
        motifs (list): List of found motifs.
    """
    
    DEFAULT_INPUT_PATH = Path("data.txt")
    
    def __init__(self, input_path: str = None):
        """
        Initialize the MotifEnumeration class with default or provided input path.
        
        Args:
            input_path (str, optional): Path to the input file. Defaults to None.
        """
        
        # Initialize with default input path for input data
        self.input_path = input_path or self.DEFAULT_INPUT_PATH
        self.sequences = []
        self.k_size = None
        self.distance = None
        self.neighbourhood = {}
        self.motifs = []
    
    def input(self, ) -> None:
        """
        Read input file and parse k-size, distance, and DNA sequences.
        
        Raises:
            FileNotFoundError: If the input file is not found or is empty.
        """
        
        # Check if file exists
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"Input file not found: {self.input_path}")
        # Check if file is not empty
        if os.stat(self.input_path).st_size == 0:
            raise FileNotFoundError(f"Empty file")
        
        # Read lines
        with open(self.input_path, "r") as file:
            lines = file.readlines()
        
        for line in lines:
            line = line.strip()
            # Check if line harbors parameters or sequences
            if line[0].isdigit():
                self.k_size, self.distance = map(int, line.split(" "))
            elif line[0].isalpha():
                self.sequences.append(line)
    
    def create_k_mers(self) -> None:
        """
        Create k-mers for each sequence and store them in a dictionary.
        """
        
        # Create k_mers and save them as dictionary with original sequence as key
        for sequence in self.sequences:
            k_mer_pool = []
            for position in range(len(sequence) - self.k_size + 1):
                k_mer_pool.append(sequence[position:position + self.k_size])
            self.neighbourhood[sequence] = k_mer_pool

    def create_neighbours(self) -> None:
        """
        Create d-neighbourhood for each k-mer and update the neighbourhood dictionary.
        """
        
        # Loop trough k-mers and create d-neighbourhood for each k-mer
        for sequence, k_mers in self.neighbourhood.items():
                neighbour_pool = []
                for k_mer in k_mers:
                    neighbour_pool.extend(neighbourhood_func(sequence=k_mer, distance=self.distance))

                self.neighbourhood[sequence] = list(set(neighbour_pool))
    
    def find_motif(self) -> None:
        """
        Find motifs that appear in all sequences by counting occurrences in the neighbourhood pool.
        """
        
        # Generate pool of k-mers including d-neighbours
        pool = []
        for neighbours in self.neighbourhood.values():
            pool.extend(neighbours)
        # Loop trough pool and determine which k-mer occured in all sequencces
        for k_mer in pool:
            if pool.count(k_mer) == len(self.neighbourhood.keys()):
                self.motifs.append(k_mer)
        # Sort motifs alphabetically remove duplicates
        self.motifs = sorted(set(self.motifs))
                            
def main():
    """
    Main function to execute motif enumeration and print the found motifs.
    """
    motif_enumerator = MotifEnumeration()
    motif_enumerator.input()
    motif_enumerator.create_k_mers()
    motif_enumerator.create_neighbours()
    motif_enumerator.find_motif()
    print(" ".join(motif_enumerator.motifs))


if __name__ == "__main__":
    main()