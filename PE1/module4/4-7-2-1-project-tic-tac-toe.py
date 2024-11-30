from random import randrange

# Define constant values 
line = "+-------+-------+-------+"
empty_line = "|       |       |       |"
computer = "X"
user = "O"

# Define initial board
board = [
    ["1", "2", "3"],
    ["4", "5", "6"],
    ["7", "8", "9"]
]

def display_board(board):
    for row in range(3):
        print(line)
        print(empty_line)
        print(f"|   {board[row][0]}   |   {board[row][1]}   |   {board[row][2]}   |")
        print(empty_line)
    print(line)

# Call the function to display initial board
display_board(board)


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    pass


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    pass


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    pass


def draw_move(board):
    # The function draws the computer's move and updates the board.
    pass
