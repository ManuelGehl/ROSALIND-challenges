def generate_direct_neighbours(sequence: str) -> list:
    """
    Generates direct neighbors of a given DNA sequence.

    Parameters:
    - sequence (str): The input DNA sequence.

    Returns:
    - list: A list containing the input sequence and its direct neighbors.
    
    Example:
    >>> generate_direct_neighbours(sequence="ATG")
    ['ATG', 'TTG', 'GTG', 'CTG', 'AAG', 'AGG', 'ACG', 'ATA', 'ATT', 'ATC']
    """
    nucleotide_list = ["A", "T", "G", "C"]
    # Initialize direct neighbours with sequence
    direct_neighbours = [sequence]
    
    # Loop trough every nucleotide in sequence
    for position, nucleotide in enumerate(sequence):
        # Generate list of possible nucleotides to exchange at each position
        candidate_list = [candidate for candidate in nucleotide_list if candidate != nucleotide]
        for candidate in candidate_list:
            # Split sequence and replace nucleotides
            split_sequence = list(sequence)
            split_sequence[position] = candidate
            # Join sequence to string and append to list
            modified_sequence = ''.join(split_sequence)
            direct_neighbours.append(modified_sequence)
    
    return direct_neighbours

def generate_d_neighbourhood(sequence: str, distance: int) -> list:
    """
    Generates a d-neighborhood of a given DNA sequence.

    Parameters:
    - sequence (str): The input DNA sequence.
    - distance (int): The maximum hamming distance of all neighbours relative to the input sequence.

    Returns:
    - list: A list containing the input sequence and its d-neighbors within the specified distance.
    
    Example:
    >> generate_d_neighbourhood(sequence="AT")
    ['AG', 'CG', 'GA', 'TC', 'GG', 'AA', 'AT', 'GT', 'CT', 'CC', 'AC', 'GC', 'TG', 'CA', 'TA', 'TT']
    """
    # Initialize neighbourhood
    neighbourhood = [sequence]
    if distance == 0:
        return neighbourhood
    
    for _ in range(distance):
        # Initialize temporary storage
        current_neighbours = []
        # Iterrate over sequences in neighbourhood
        for seq in neighbourhood:
            direct_neighbours = generate_direct_neighbours(sequence=seq)
            current_neighbours += direct_neighbours
        
        # Add current neighbours to neighbourhood
        neighbourhood += current_neighbours
        # Remove duplicates
        neighbourhood = list(set(neighbourhood))
    
    return neighbourhood

def neighbourhood_dictionary(k_mers: list, distance: int) -> dict:
    """
    Generates a dictionary of k-mers and their corresponding d-neighbourhoods.
    
    Parameters:
    
    - k_mers (list): A list of k-mers.
    - distance (int): The maximum Hamming distance for generating d-neighbourhoods.

    Returns:
    
    - dict: A dictionary where keys are k-mers and values are their d-neighbourhoods.
    """
    # Initialize empty neighbourhood dictionary
    neighbourhood_dict = {}
    # Iterate over all k-mers, use them as keys and generate the corresponding d-neighbourhood
    for k_mer in k_mers:
        neighbourhood_dict[k_mer] = generate_d_neighbourhood(sequence=k_mer, distance=distance)
        
    return neighbourhood_dict