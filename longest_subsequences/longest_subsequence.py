class LongestSubsequences:
    
    def __init__(self):
        self.permutation = None
        self.increasing_seq = list()
        self.decreasing_seq = list()

    def remove_maximum(self, window: list) -> list:
        window.remove(max(window))
        return window

    def increasing_series(self, window: list) -> bool:
        for step in range(len(window) - 1):
            number1, number2 = window[step: step + 2]
            if number1 > number2:
                return False
        
        return True
      
    def remove_minimum(self, window: list) -> list:
        window.remove(min(window))
        return window

        
    def find_increasing_subseq(self):
        # Initialize current window and longest sequence
        current_window = self.permutation
        
        while self.increasing_series(current_window) == False:
            current_window = self.remove_maximum(current_window)
        
        self.increasing_seq = current_window        
           

        
            
            
                
    
    

    
    