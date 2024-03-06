def pattern_frequency(sequence: str, pattern_length: int) -> dict:
    """
    Calculate the frequency of patterns of a given length in a DNA sequence.

    Parameters:
    - sequence (str): The DNA sequence to analyze.
    - pattern_length (int): The length of patterns to count.

    Returns:
    dict: A dictionary where keys are patterns and values are their frequencies.

    Example:
    >>> pattern_frequency("ATGATGCTAGTAGT", 3)
    {'ATG': 2, 'TGA': 1, 'GAT': 1, 'ATC': 1, 'GCT': 1, 'CTA': 1, 'TAG': 2, 'AGT': 1, 'GTA': 1}
    """
    # Initialize frequency dictionary
    frequency_dict = {}

    # Define scanning range
    scanning_range = len(sequence) - pattern_length

    # Slide a window over the sequence
    for pos in range(scanning_range + 1):
        # Extract the current window
        current_window = sequence[pos:pos + pattern_length]

        # If current_window not in dictionary, initialize with key = 0
        frequency_dict.setdefault(current_window, 0)
        # If current_window occured, increase by 1
        frequency_dict[current_window] += 1

    return frequency_dict
