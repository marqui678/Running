class Goal():
    """This class creates and initialize the distance and difficulty variables"""
 

    VALID_DISTANCES = ['10','21','42']
    VALID_DIFFICULTY = ['Beginner','Intermediate','Advance']
 
    def __init__(self):
        self.name = None
        self.date = None
        self.reward = None
        self.distance = None
        self.difficulty = None
        self.query_for_parameters();
 
 
 
    def query_for_parameters(self):
        self.name = raw_input('Goal Name: ')
        self.date = goal_date = raw_input('Goal date: ')
        self.reward = raw_input('Reward: ')
        while True:
            distance_input = raw_input('Distance: ')
            if distance_input in self.VALID_DISTANCES:
                self.distance = distance_input
                break
            print("Not a valid distance")
        while True:
            difficulty_input = raw_input('Difficulty: ')
            if difficulty_input in self.VALID_DIFFICULTY:
                self.difficulty = difficulty_input
                break
            print("Not a valid difficulty")
            
        
 
 
    def __str__(self):
        return "Goal: {0} to be done by {1} Reward: {2} Distance {3} Difficulty {4}".format(self.name, self.date, self.reward, self.distance, self.difficulty)
 
        
        
def main():
    new_goal = Goal()
    print new_goal
 
 
if __name__=='__main__':
    main()
