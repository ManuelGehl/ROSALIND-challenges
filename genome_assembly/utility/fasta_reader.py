from typing import Dict

def read_fasta(file_path: str) -> Dict:
    """
    Read DNA sequences from a FASTA file and return a dictionary of sequence identifiers and sequences.

    Parameters:
    - file_path (str): The path to the FASTA file.

    Returns:
    dict: A dictionary where keys are sequence identifiers (without the '>' symbol) and values are
          corresponding DNA sequences in uppercase.
    """
    
    # Define containers for id and sequence
    current_id = ""
    current_seq = ""
    sequence_dict = {}
    
    
    with open(file_path) as file:
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
            
    return sequence_dict