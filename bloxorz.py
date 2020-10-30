

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
        purpose is to always fix relative coordinates of b1 && b2
    '''
    def update_b1_b2(self) :
        x1,y1 = self.curr_state[0].x, self.curr_state[0].y
        x2,y2 = self.curr_state[1].x, self.curr_state[1].y

        if x1+y1 <= x2+y2 :
            pass
        else:
            self.curr_state[0].x = x2 
            self.curr_state[0].y = y2
            
            self.curr_state[1].x = x1
            self.curr_state[1].y = y1 


    
    '''
        this function checks if the block is vertical and can move right
    '''
    def v_right_movable(self):
        if self.curr_state[1].y + 2 < self.YSIZE and self.puzzle[self.curr_state[0].x,self.curr_state[0].y+1] != 'X' and self.puzzle[self.curr_state[1].x,self.curr_state[1].y+2] != 'X' : # block can move right
            return True
        else:
            return False
        

    '''
        this function checks if the block is vertical and can move to left
    '''
    def v_left_movable(self):
        if self.curr_state[1].y-2 >= 0 and self.puzzle[self.curr_state[0].x,self.curr_state[0].y-1] != 'X' and self.puzzle[self.curr_state[1].x,self.curr_state[1].y-2] != 'X'  :
            return True
        else:
            return False


    '''
        this function checks if the block is vertical and can move upwards
    '''
    def v_up_movable(self): 
        if self.curr_state[1].x -2 >= 0 and self.puzzle[self.curr_state[0].x-1,self.curr_state[0].y] != 'X' and self.puzzle[self.curr_state[1].x-2,self.curr_state[1].y] != 'X':
            return True
        else:
            return False


    def v_down_movable(self):
        if self.curr_state[1].x+2 < self.XSIZE and self.puzzle[self.curr_state[0].x+1,self.curr_state[0].y] != 'X' and self.puzzle[self.curr_state[1].x+2,self.curr_state[1].y] != 'X' :
            return True
        else:
            return False


    '''
        check if the block is horizontal and can move to right
    '''
    def h_right_movable(self):
        #understand the position of the horizontal block
        if self.curr_state[0].x == self.curr_state[1].x-1:
            if self.curr_state[0].y+1 < self.YSIZE and self.curr_state[1].y+1 < self.YSIZE and self.puzzle[self.curr_state[0].x,self.curr_state[0].y+1] != 'X' and self.puzzle[self.curr_state[1].x, self.curr_state[1].y+1] != 'X' :
                return True
            else :
                return False
        #no need to check the position but for the sake of readability, let's write
        elif self.curr_state[0].y == self.curr_state[1].y-1 :
            if self.curr_state[0].y+2 < self.YSIZE and self.curr_state[1].y+1 < self.YSIZE and self.puzzle[self.curr_state[0].x,self.curr_state[0].y+2] != 'X' and self.puzzle[self.curr_state[1].x, self.curr_state[1].y+1] != 'X' :
                return True
            else:
                return False

    
    '''
        check if the block is horizontal and can move to left
    '''
    def h_left_movable(self):
        if self.curr_state[0].x == self.curr_state[1].x-1: # means y coordinates are constant
            if self.curr_state[0].y-1 >= 0 and self.curr_state[1].y-1 >= 0 and self.puzzle[self.curr_state[0].x,self.curr_state[0].y-1] != 'X' and self.puzzle[self.curr_state[1].x,self.curr_state[1].y-1] != 'X' :
                return True
            else :
                return False
        
        elif self.curr_state[0].y == self.curr_state[1].y-1 : # means x coordinates are constant
            if self.curr_state[0].y-1 >= 0 and self.curr_state[1].y-2 >= 0 and self.puzzle[self.curr_state[0].x,self.curr_state[0].y-1] != 'X' and self.puzzle[self.curr_state[1].x,self.curr_state[1].y-2] != 'X' :
                return True
            else : 
                return False

    '''
        check if the block is horizontal and can move upwards
    '''
    def h_up_movable(self):
        if self.curr_state[0].x == self.curr_state[1].x :
            if self.curr_state[0].x-1 >= 0 and self.curr_state[1].x-1 >= 0 and self.puzzle[self.curr_state[0].x-1,self.curr_state[0].y] != 'X' and self.puzzle[self.curr_state[1].x-1,self.curr_state[1].y] != 'X' :
                return True
            else : 
                return False

        elif self.curr_state[0].y  == self.curr_state[1].y :
            if self.curr_state[0].x-1 >= 0 and self.curr_state[1].x-2 >= 0 and self.puzzle[self.curr_state[0].x-1,self.curr_state[0].y] != 'X' and self.puzzle[self.curr_state[1].x-2,self.curr_state[1].y] != 'X' : 
                return True
            else :
                return False
       
        
    '''
        check if the block is horizontal and can move downwards 
    '''
    def h_down_movable(self):
        if self.curr_state[0].x == self.curr_state[1].x :
            if self.curr_state[0].x+1 < self.XSIZE and self.curr_state[1].x+1 < self.XSIZE and self.puzzle[self.curr_state[0].x+1,self.curr_state[0].y] != 'X' and self.puzzle[self.curr_state[1].x+1,self.curr_state[1].y] != 'X' :
                return True
            else : 
                return False

        elif self.curr_state[0].y  == self.curr_state[1].y :
            if self.curr_state[0].x+2 < self.XSIZE and self.curr_state[1].x+1 < self.XSIZE and self.puzzle[self.curr_state[0].x+2,self.curr_state[0].y] != 'X' and self.puzzle[self.curr_state[1].x+1,self.curr_state[1].y] != 'X' : 
                return True
            else :
                return False
     




    '''
        returns true if the blocks current state is the goal state
    '''
    def is_goal_state(self):
        return (self.curr_state[0].x == self.goal_state[0].x and
                self.curr_state[1].x == self.goal_state[1].x and
                self.curr_state[0].y == self.goal_state[0].y and
                self.curr_state[1].y == self.goal_state[1].y)


    
    '''
        function to move right 
    '''
    def move_right(self): 

        
        if self.is_vertical() :  # block is vertical
            if self.v_right_movable():
                #change 'O' and 'S' 
                self.puzzle[self.curr_state[0].x,self.curr_state[0].y] = 'O' # no need to update self[1].x since they are equal
                self.curr_state[0].y+=1 # update current state for block 1
                self.curr_state[1].y+=2 # update current state for block 2
                self.puzzle[self.curr_state[0].x,self.curr_state[0].y] = 'S'
                self.puzzle[self.curr_state[1].x,self.curr_state[1].y] = 'S'
            else:
                print("Block can't move to right")
                
        else : # block is horizontal 
            if self.h_right_movable():
                #2 horizontal options -> x's are constant || y's are constant 
                if self.curr_state[0].y == self.curr_state[1].y :
                    self.puzzle[self.curr_state[0].x, self.curr_state[0].y] == 'O'
                    self.puzzle[self.curr_state[1].x, self.curr_state[1].y] == 'O'
                    #update current state
                    self.curr_state[0].y+=1 
                    self.curr_state[1].y+=1
                    # update puzzle coordinates
                    self.puzzle[self.curr_state[0].x, self.curr_state[0].y] == 'S'
                    self.puzzle[self.curr_state[1].x, self.curr_state[1].y] == 'S'
                
                 # no need to mention but this time x's are constant, so a simple else would do the job.
                 #for the sake of simplicity, I'll put an elif to state the condition 
                 elif self.curr_state[0].x == self.curr_state[1].x : 
                    self.puzzle[self.curr_state[0].x, self.curr_state[0].y] == 'O'
                    self.puzzle[self.curr_state[1].x, self.curr_state[1].y] == 'O'
                    #update current state
                    self.curr_state[0].y+=2
                    self.curr_state[1].y+=1
                    #update puzzle coordinates
                    self.puzzle[self.curr_state[0].x, self.curr_state[0].y] == 'S'
                    self.puzzle[self.curr_state[1].x, self.curr_state[1].y] == 'S'
          
            else:
                print("Block can't move to right")

        #update relative coordinates of blocks. --NEEDED END OF EVERY MOVEMENT FUNCTION!!!!
        self.update_b1_b2() 
                



    def move_left(self): 
        if self.is_vertical() :  # block is vertical
            if self.v_left_movable():
                #change 'O' and 'S' 
                self.puzzle[self.curr_state[0].x,self.curr_state[0].y] = 'O' # no need to update self[1].x since they are equal
                self.curr_state[0].y-=1 # update current state for block 1 -- notice b1-b2 relatively changed, don't forget to update the relative coordinates, b1 <= b2 always
                self.curr_state[1].y-=2 # update current state for block 2
                self.puzzle[self.curr_state[0].x,self.curr_state[0].y] = 'S'
                self.puzzle[self.curr_state[1].x,self.curr_state[1].y] = 'S'
            else:
                print("Block can't move to left")
                
        else : # block is horizontal 
            if self.h_left_movable():
                #2 horizontal options -> x's are constant || y's are constant 
                if self.curr_state[0].y == self.curr_state[1].y :
                    self.puzzle[self.curr_state[0].x, self.curr_state[0].y] == 'O'
                    self.puzzle[self.curr_state[1].x, self.curr_state[1].y] == 'O'
                    #update current state
                    self.curr_state[0].y-=1 
                    self.curr_state[1].y-=1
                    # update puzzle coordinates
                    self.puzzle[self.curr_state[0].x, self.curr_state[0].y] == 'S'
                    self.puzzle[self.curr_state[1].x, self.curr_state[1].y] == 'S'
                
                 # no need to mention but this time x's are constant, so a simple else would do the job.
                 #for the sake of simplicity, I'll put an elif to state the condition 
                 elif self.curr_state[0].x == self.curr_state[1].x : 
                    self.puzzle[self.curr_state[0].x, self.curr_state[0].y] == 'O'
                    self.puzzle[self.curr_state[1].x, self.curr_state[1].y] == 'O'
                    #update current state
                    self.curr_state[0].y-=1
                    self.curr_state[1].y-=2
                    #update puzzle coordinates
                    self.puzzle[self.curr_state[0].x, self.curr_state[0].y] == 'S'
                    self.puzzle[self.curr_state[1].x, self.curr_state[1].y] == 'S'
          
            else:
                print("Block can't move to left")

        #update relative coordinates of blocks. --NEEDED END OF EVERY MOVEMENT FUNCTION!!!!
        self.update_b1_b2() 


    def move_up(self): 

        if self.is_vertical():
            if self.v_up_movable():
                self.puzzle[self.curr_state[0].x,self.curr_state[0].y] = 'O' # no need to update self[1].x since they are equal
                #update current state 
                self.curr_state[0].x-=1
                self.curr_state[1].x-=2
                #update puzzle coordinates
                self.puzzle[self.curr_state[0].x, self.curr_state[0].y] == 'S'
                self.puzzle[self.curr_state[1].x, self.curr_state[1].y] == 'S'
            else:
                print("Block can't move upwards")
        else : # blocks are in a horizontal position 
            if self.h_up_movable() :
                if self.curr_state[0].y == self.curr_state[1].y :
                    self.puzzle[self.curr_state[0].x,self.curr_state[0].y] = 'O'
                    self.puzzle[self.curr_state[1].x,self.curr_state[1].y] = 'O'
                    #update current state
                    self.curr_state[0].x-=1
                    self.curr_state[1].x-=2
                    #update puzzle coordinates
                    self.puzzle[self.curr_state[0].x, self.curr_state[0].y] == 'S'
                    self.puzzle[self.curr_state[1].x, self.curr_state[1].y] == 'S'

                elif self.curr_state[0].x == self.curr_state[1].x:
                    self.puzzle[self.curr_state[0].x,self.curr_state[0].y] = 'O'
                    self.puzzle[self.curr_state[1].x,self.curr_state[1].y] = 'O'
                    #update current state
                    self.curr_state[0].x-=1
                    self.curr_state[1].x-=1
                    #update puzzle coordinates
                    self.puzzle[self.curr_state[0].x, self.curr_state[0].y] == 'S'
                    self.puzzle[self.curr_state[1].x, self.curr_state[1].y] == 'S'
            else :
                print("Block can't move upwards")

        #update relative coordinates of blocks. --NEEDED END OF EVERY MOVEMENT FUNCTION!!!!
        self.update_b1_b2() 


    def move_down(self): 

        if self.is_vertical():
            if self.v_down_movable():
                self.puzzle[self.curr_state[0].x,self.curr_state[0].y] = 'O' # no need to update self[1].x since they are equal
                #update current state 
                self.curr_state[0].x+=1
                self.curr_state[1].x+=2
                #update puzzle coordinates
                self.puzzle[self.curr_state[0].x, self.curr_state[0].y] == 'S'
                self.puzzle[self.curr_state[1].x, self.curr_state[1].y] == 'S'
            else:
                print("Block can't move downwards")
        else : # blocks are in a horizontal position 
            if self.h_down_movable():
                if self.curr_state[0].y == self.curr_state[1].y :
                    self.puzzle[self.curr_state[0].x,self.curr_state[0].y] = 'O'
                    self.puzzle[self.curr_state[1].x,self.curr_state[1].y] = 'O'
                    #update current state
                    self.curr_state[0].x+=1
                    self.curr_state[1].x+=2
                    #update puzzle coordinates
                    self.puzzle[self.curr_state[0].x, self.curr_state[0].y] == 'S'
                    self.puzzle[self.curr_state[1].x, self.curr_state[1].y] == 'S'

                elif self.curr_state[0].x == self.curr_state[1].x:
                    self.puzzle[self.curr_state[0].x,self.curr_state[0].y] = 'O'
                    self.puzzle[self.curr_state[1].x,self.curr_state[1].y] = 'O'
                    #update current state
                    self.curr_state[0].x+=1
                    self.curr_state[1].x+=1
                    #update puzzle coordinates
                    self.puzzle[self.curr_state[0].x, self.curr_state[0].y] == 'S'
                    self.puzzle[self.curr_state[1].x, self.curr_state[1].y] == 'S'
            else :
                print("Block can't move downwards")

        #update relative coordinates of blocks. --NEEDED END OF EVERY MOVEMENT FUNCTION!!!!
        self.update_b1_b2() 

        

    #Uniform Search Cost Search algorithm for solving the puzzle
    '''
    def UCS():
        pass  #TODO

    def A_Star():
        pass  #TODO
    '''

