from bloxorz import coordinate,Bloxorz



def create_matrix():
    puzzle = []
    puzzle_file = open("input_matrix.txt")
    for line in puzzle_file:
        puzzle.append(line.split())

    return puzzle

def main() :
    puzzle = create_matrix()
    current_state = []
    goal_state = []
    #find starting state a.k.a first current state 
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 'S' :
                current_state.append(coordinate(i,j))
            elif puzzle[i][j] == 'G':
                goal_state.append(coordinate(i,j))

    #puzzle,goal_state,curr_state
    initial_state = current_state # beginning current state = initial state
    Game = Bloxorz(puzzle,initial_state,goal_state,current_state)
    Game.move_up()
    print(Game.curr_state[0].x,Game.curr_state[0].y)
    print(Game.curr_state[1].x,Game.curr_state[1].y)
    new_puzzle = Game.puzzle
    for row in new_puzzle : 
        print(row)



if __name__ == "__main__" : 
    main()
