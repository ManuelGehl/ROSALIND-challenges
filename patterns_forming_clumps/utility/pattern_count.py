def pattern_count(sequence: str, pattern: str) -> int:
    """
    Count the occurrences of a pattern in a given sequence.

    Parameters:
    - sequence (str): The input sequence to search for the pattern.
    - pattern (str): The pattern to count within the sequence.

    Returns:
    int: The count of occurrences of the pattern in the sequence.

    Example:
    >>> pattern_count("ATATAT", "AT")
    3
    """
    pattern_length = len(pattern)
    counter = 0

    for pos in range(len(sequence) - pattern_length + 1):
        if sequence[pos:pos + pattern_length] == pattern:
            counter += 1

    return counter
