class LongestSubsequences:
    
    def __init__(self):
        self.permutation = None
        self.increasing_seq = list()
        self.decreasing_seq = list()

    def remove_maximum(self, window: list) -> list:
        window.remove(max(window))
        return window
    
    def check_remaining_window(self, window: list, sequence: list) -> bool:
        if len(window) < len(sequence):
            return True
        else:
            return False
        
    def find_increasing_subseq(self):
        # Initialize current window and longest sequence
        current_window = self.permutation
        longest_seq = []
        
        # Iterate as often as numbers are in the permutation sequence
        for _ in range(len(self.permutation)):
            
            # Check if longest_seq is longer than all sequences before
            if len(longest_seq) >= len(self.increasing_seq):
                self.increasing_seq = longest_seq

            # Loop trough window
            longest_seq = [current_window[0]]
            for next_number in current_window[1:]:
                
                # Determine highest number in window
                highest_number = max(current_window)
                
                # Check if number at position 0 is maximum
                if current_window[0] == highest_number:
                    # Remove maximum value and exit loop
                    current_window = self.remove_maximum(window=current_window)
                    break
                
                # Check if next number is greater than numbers in potential sequence
                if longest_seq[-1] < next_number:
                    longest_seq.append(next_number)
    
                # If next number is already maximum of current window, remove maximum value and exit loop
                if next_number == highest_number:
                    current_window = self.remove_maximum(window=current_window)
                    break
        
            
            print(longest_seq)
            # Define current window new by removing the maximum value from array
            
            # Check if the remainind window size can produce a sequence that is longer than the current longest sequence
            #if self.check_remaining_window(window=current_window, sequence=self.increasing_seq):
            #    break
        
            
            
                
    
    

    
    