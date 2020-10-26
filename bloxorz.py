
class Bloxorz:

    #Puzzle indicates the matrix
    #Block intdicates the moving object
    #init_state represents the inital state -> coordinate wise
    #goal_state represents the success/goal state -> coordinate wise
    def __init__(self,puzzle,block,init_state,goal_state):
        self.puzzle = puzzle
        self.block = block
        self.init_state = init_state
        self.goal_state = goal_state

    #Uniform Search Cost Search algorithm for solving the puzzle
    def UCS():

