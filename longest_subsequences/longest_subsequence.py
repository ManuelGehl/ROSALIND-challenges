class LongestSubsequences:
    
    def __init__(self):
        self.permutation = None
        self.increasing_seq = None
        self.decreasing_seq = None

    def remove_maximum(self, window: list) -> list:
        window.remove(max(window))
        return window

    def increasing_series(self, window: list) -> bool:
        for step in range(len(window) - 1):
            number1, number2 = window[step: step + 2]
            if number1 > number2:
                return False
        
        return True
    
    def decreasing_series(self, window: list) -> bool:
        for step in range(len(window) - 1):
            number1, number2 = window[step: step + 2]
            if number1 < number2:
                return False
        
        return True
      
    def remove_minimum(self, window: list) -> list:
        window.remove(min(window))
        return window

        # 1, 2, 3
    def find_increasing_subseq(self):
        # Initialize current window and longest sequence
        current_window = self.permutation.copy()
        
        while self.increasing_series(current_window) == False:
            current_window = self.remove_maximum(current_window)
        
        self.increasing_seq = current_window
    
    def find_decreasing_subseq(self):
        # Initialize current window and longest sequence
        current_window = self.permutation.copy()
        
        while self.decreasing_series(current_window) == False:
            current_window = self.remove_minimum(current_window)
        
        self.decreasing_seq = current_window

def main():
    subsequence_finder = LongestSubsequences()
    subsequence_finder.permutation = [5, 1, 4, 2, 3]
    subsequence_finder.find_increasing_subseq()
    subsequence_finder.find_decreasing_subseq()
    print(subsequence_finder.increasing_seq)
    print(subsequence_finder.decreasing_seq)

if __name__ == "__main__":
    main()
           

        
            
            
                
    
    

    
    