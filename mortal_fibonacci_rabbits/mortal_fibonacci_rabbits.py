class MortalFibonacciRabbits:
    
    def __init__(self, months: int, lifespan:int):
        self.months = months
        self.lifespan = lifespan
    
    def recursion(self, timestep):
        # Define base cases
        month1 = 1
        month2 = 1
        # Distinguish between Fibonacci series and non-Fibonacci series
        if self.timestep < self.lifespan:
            # Normal Fibonacci sequence
            population = self.recursion(timestep=self.timestep-1) + self.recursion(timestep=self.timestep-2)
        return population
        