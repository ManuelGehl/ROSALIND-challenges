import argparse

class LongestSubsequences:
    
    def __init__(self):
        self.permutation = None
        self.increasing_seq = None
        self.decreasing_seq = None
    
    def parse_arguments(self):
        # Create ArgumentParser object
        parser = argparse.ArgumentParser(description="Description of your script")

        # Add arguments
        parser.add_argument('arg1', type=str, help='Description of arg1')

        # Parse the command line arguments
        args = parser.parse_args()

        # Access the arguments and do something with them if needed
        self.permutation = args.arg1
    
    def move_window(self, window: list) -> list:
        return window[1:]
    
    def remove_maximum(self, window: list) -> list:
        return window.remove(max(window))
    
    def check_remaining_window(self, window: list, sequence: list) -> bool:
        if len(window) < len(sequence):
            return True
        else:
            return False
        
    def find_increasing_subseq(self):
        # Initialize current window
        current_window = self.permutation

        # Determine highest number in window
        highest_number = max(current_window)
        # Check if number at position 0 is maximum
        if current_window[0] == highest_number:
            current_window = self.move_window(window=current_window)
            
        # Loop trough window
        longest_seq = [current_window[0]]
        for next_number in current_window[1:]:
            # Check if next number is greater than numbers in potential sequence
            if longest_seq[-1] < next_number:
                longest_seq.append(next_number)
            # If next number is already maximum of current window, exit loop
            elif next_number == highest_number:
                continue
        
        # Check if longest_seq is longer than all sequences before
        if len(longest_seq) >= self.increasing_seq:
            self.increasing_seq = longest_seq
        
        # Check if the remainind window size can produce a sequence that is longer than the current longest sequence
        
            
            
                
    
    

    
    