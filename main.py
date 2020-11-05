import bloxorz


def create_matrix():
    puzzle = []
    puzzle_file = open("input_matrix.txt")
    for line in puzzle_file:
        puzzle.append(line.split())

    return puzzle

def main() :
    puzzle = create_matrix()


if __name__ == "__main__" : 
    main()
