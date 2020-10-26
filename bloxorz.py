

class coordinate:

    def __init__(self,x,y):
        self.x = x
        self.y = y

class Bloxorz:

    #Puzzle indicates the matrix
    #Block intdicates the moving object
    #init_state represents the inital state -> coordinate wise
    #goal_state represents the success/goal state -> coordinate wise
    def __init__(self,puzzle,init_state,goal_state,curr_state,position):
        self.puzzle = puzzle
        self.init_state = init_state
        self.curr_state = curr_state
        self.goal_state = goal_state
        self.position = position
        self.XSIZE = len(puzzle)
        self.YSIZE =  len(puzzle[0])


    '''
        is_vertical returns true if current state of block is vertical
        assume curr_state consists two coordinates for each part of block
    '''
    def is_vertical(self):
        x1,y1 = self.curr_state[0].x, self.curr_state[0].y
        x2,y2 = self.curr_state[1].x, self.curr_state[1].y

        if x1==x2 and y1==y2: #if all coordinates of half blocks match, one can assume that block is in a vertical position
            return True
        else:
            return False

    
    '''
        this function checks if the block is vertical and can move right
    '''
    def v_right_movable(self):
        if self.is_vertical == True:
            if self.curr_state[1].y + 2 < self.YSIZE : # block can move right
                return True
            else:
                return False
        else: # block is not vertical at all
            return False

    '''
        this function checks if the block is vertical and can move to left
    '''
    def v_left_movable(self):
        if self.is_vertical == True:
            if self.curr_state[1].y-2 >= 0 :
                return True
            else:
                return False
        else:
            return False 


    '''
        this function checks if the block is vertical and can move upwards
    '''
    def v_up_movable(self): 
        if self.is_vertical == True: 
            if self.curr_state[1].x -2 >= 0:
                return True
            else:
                return False
        else:
            return False


    def v_down_movable(self):
        if self.is_vertical == True:
            if self.curr_state[1].x+2 < self.XSIZE :
                return True
            else:
                return False
        else:
            return False

    


    '''
        returns true if the blocks current state is the goal state
    '''
    def is_goal_state(self):
        return (self.curr_state[0].x == self.goal_state[0].x and
                self.curr_state[1].x == self.goal_state[1].x and
                self.curr_state[0].y == self.goal_state[0].y and
                self.curr_state[1].y == self.goal_state[1].y)


    

    #Uniform Search Cost Search algorithm for solving the puzzle
    def UCS():
        pass 

    def A_Star():
        pass

