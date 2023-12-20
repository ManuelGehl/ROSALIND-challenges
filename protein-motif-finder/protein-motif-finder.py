import requests

class ProteinMotifFinder:
    """
    Class to read Uniprot Identifiers from text file, access sequence from
    Uniprot and search for N-glycosylation motif N{P}[ST]{P} in sequence.
    
    Attributes:
    - STANDARD_URI (str): URI for accessing Uniprot API.
    - MOTIF_LENGTH (int): Length of the N-glycosylation motif.
    """
    STANDARD_URI = "https://www.ebi.ac.uk/proteins/api/proteins"
    MOTIF_LENGTH = 4
    
    
    def __init__(self, input_path=None, output_path=None):
        """
        Initialize ProteinMotifFinder with input and output file paths.

        Parameters:
        - input_path (str): Path to the input file containing Uniprot Identifiers. Default is None.
        - output_path (str): Path to the output file. Default is None.
        """
        if input_path is None:
            input_path = "data.txt"
        if output_path is None:
            output_path = "result.txt"
        self.input_path = input_path
        self.output_path = output_path
        # Dictionary of type short ID: long ID
        self.identifiers = {}
        self.sequences = {}
        self.results = {}
        
    def read_identifiers(self):
        """
        Read Uniprot identifiers from input file.
        """
        with open(self.input_path) as file:
            # Read Uniprot ID
            for line in file:
                # Check if provided identifier is of type ID_Accession or
                # only of type ID
                line = line.strip()
                fragment_count = len(line.split("_"))
                if fragment_count == 1:
                    self.identifiers[line] = line
                else:
                    self.identifiers[line.split("_")[0]] = line
                    
    
    def get_sequence(self):
        """
        Use Uniprot IDs to receive protein sequences from database.
        """
        
        for uniprot_acc in self.identifiers.keys():
            path = f"{self.STANDARD_URI}/{uniprot_acc}"
            response = requests.get(path)
            
            # Check response
            if response.status_code == 200:
                print(f"Uniprot access successful for {uniprot_acc}")
                data = response.json()
                sequence = data["sequence"]["sequence"]
                # Convert short accession number to long accession number
                long_acc = self.identifiers[uniprot_acc]
                self.sequences[long_acc] = sequence.upper()
            else:
                print(f"Unitprot access failed for ID: {uniprot_acc}")
                print(f"Status code: {response.status_code}")
    
    def find_motif(self):
        """
       Search for the N-glycosylation motif in protein sequences.

       Constraints:
       - The motif starts with "N" and is followed by a non-"P" amino acid,
         then either "S" or "T," and finally, another non-"P" amino acid.
        """
        
        for identifer, sequence in self.sequences.items():
            # Define length of motif and sequence
            length_seq = len(sequence)
            # Define difference between 2 strings as maximal step size
            length_diff = length_seq - self.MOTIF_LENGTH
            # Define list for storing starting positions of found motifs
            starting_pos = []
            
            # Iterate over sequence
            for i in range(length_diff):
                frame = sequence[i:i + self.MOTIF_LENGTH]
                
                # Check if motif is in frame
                if frame[0] == "N" and frame[1] != "P" and frame[2] in {"S", "T"} and frame[3] != "P":
                    # Motif found
                    starting_pos.append(i + 1)
                
            # Check if motif was found at all
            if starting_pos:
                # Write long identifier as key and startings positions
                # as values
                self.results[identifer] = starting_pos
    
    def write_results(self):
        """
        Write results to the output file.
        """
        with open(self.output_path, "w") as file:
            # Write accession number as one line and positions as one line
            for accession, positions in self.results.items():
                file.write(f"{accession}\n")
                # Write positions
                for pos in positions:
                    # Check if last positions is reached to add line break
                    if pos == positions[-1]:
                        file.write(f"{pos}\n")
                    else:
                        file.write(f"{pos} ")
            
def main():
    glycosylation_finder = ProteinMotifFinder()
    glycosylation_finder.read_identifiers()
    glycosylation_finder.get_sequence()
    glycosylation_finder.find_motif()
    glycosylation_finder.write_results()
    
    
if __name__ == "__main__":
    main()