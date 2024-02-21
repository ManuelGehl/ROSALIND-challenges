"""
Task: 
    Given: Positive integers n≤100 and m≤20 and k=1.
    Return: The total number of pairs of rabbits that will remain after the 
            n-th month if all rabbits live for m months and produce one pair
            of litter.
            
    Rules: Starts with 1 pair of rabbits in first month
           Newborn rabbits need 1 month to become adult
           Adult rabbits mate every month. Rabbits die after 3 months.
"""

class Rabbit:
    """ Describes a rabbit"""
    def __init__(self, age=1):
        self.age = age
    
    def grow(self):
        self.age += 1
    

class RabbitPopulation:
    """
    Class to describe a population of rabbit pairs.
    """
    def __init__(self, life_span):
        """
        Initializes population with one baby pair.

        """
        # Initialize with a list of 1 Rabbit instance
        self.population = [Rabbit()]
        self.pop_age = 1
        self.adults = 0
        self.children = 0
        self.offspring = 0
        self.life_span = life_span + 1
    
    def count_adults(self):
        """Count rabbits with age >= 2"""
        self.adults = sum( 1 for rabbit in self.population if rabbit.age >= 2)
        #print(f"Adults: {self.adults}")
        
    def count_children(self):
        """Count rabbits with age == 1"""
        self.children = sum(1 for rabbit in self.population if rabbit.age == 1)
        #print(f"Children: {self.children}")

    def count_offspring(self):
        """Counts offspring that will be born next month"""
        self.offspring = self.adults
        #print(f"Offspring: {self.offspring}")
    
    def filter_adults(self):
        """Filters out all adult rabbits that turned 4"""
        self.population = [rabbit for rabbit in self.population if rabbit.age < self.life_span]
        #print(f"Population after filtering: {len(self.population)}")
    
    def grow_rabbits(self):
        """Let all existing rabbits grow"""
        for rabbit in self.population:
            rabbit.grow()
    
    def add_offspring(self):
        """Adds offspring to the population"""
        self.population.extend([Rabbit() for _ in range(self.offspring)])

    def simulate_month(self):
        """Simulates one month"""
        #Count all types of rabbits
        self.count_adults()
        self.count_children()
        self.count_offspring()
        #Let rabbits grow and filter out dying ones
        self.grow_rabbits()
        self.filter_adults()
        #Add offspring to population
        self.add_offspring()
        #Add 1 month to counter
        self.pop_age += 1
        print(f"Current month: {self.pop_age}")
        print(f"Current population: {len(self.population)}")
    
    def simulate_time_period(self, months):
        """Simulates given period of months"""
        counter = months - 1
        for _ in range(counter):
            self.simulate_month()


if __name__ == "__main__":
    population = RabbitPopulation(life_span=10)
    population.simulate_time_period(months=10)