from pattern_frequency import pattern_frequency
from pattern_count import pattern_count

def filter_frequencies(frequency_dict: dict, occurence: int) -> dict:
    """
    Filter a dictionary of pattern frequencies, keeping only patterns with frequencies equal or greater than a given occurrence.

    Parameters:
    - frequency_dict (dict): Dictionary containing patterns as keys and their frequencies as values.
    - occurrence (int): The minimum frequency required to include a pattern.

    Returns:
    dict: Filtered dictionary with patterns meeting the occurrence criteria.
    """
    return {pattern: frequency for pattern, frequency in frequency_dict.items() if frequency >= occurence}

def find_clumps(sequence: str, filtered_dict: dict, occurence: int, clump_length: int) -> list:
    """
    Find clumped patterns in a DNA sequence based on a filtered dictionary of pattern frequencies.

    Parameters:
    - sequence (str): The DNA sequence to analyze.
    - filtered_dict (dict): Filtered dictionary of pattern frequencies.
    - occurrence (int): The desired frequency for a pattern to be considered part of a clump.
    - clump_length (int): The length of the clump.

    Returns:
    list: List of patterns that form clumps in the sequence.
    """
    # Initialize pattern list
    clumped_patterns = []
    
    # Loop trough filtered dictionary
    for current_pattern in filtered_dict.keys():
        # Slide over the sequence with a given window size and count all occurences of pattern
        for pos in range(len(sequence) - clump_length):
            current_window = sequence[pos:pos + clump_length + 1]
            counter = pattern_count(sequence=current_window, pattern=current_pattern)
            if counter == occurence:
                clumped_patterns.append(current_pattern)
                # Exit the inner loop
                break
            
    return clumped_patterns

def main():
    seq = "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
    pattern_len = 5
    clump_len = 75
    occurence = 4
    freq_dict = pattern_frequency(sequence=test_seq, pattern_length=pattern_len)
    filtered = filter_frequencies(frequency_dict=freq_dict, occurence=occ)
    clumps = find_clumps(sequence=test_seq, filtered_dict=filtered, occurence=occ, clump_length=window)



