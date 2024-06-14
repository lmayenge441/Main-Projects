#Name: Lydia Mayenge
#Date: 05/18/2021
#This code allows me to move chess pieces across a chessboard
import turtle

# Constants for the chessboard and pieces
SCREEN_SIZE = 600
GRID_SIZE = 8
SQUARE_SIZE = SCREEN_SIZE // GRID_SIZE

# Initialize the turtle screen
screen = turtle.Screen()
screen.title("Chessboard")
screen.setup(SCREEN_SIZE, SCREEN_SIZE)

# Function to draw the chessboard grid
def draw_chessboard():
    turtle.speed(0)  # Set the turtle's speed to the fastest
    turtle.penup()  # Lift the pen
    turtle.goto(-SCREEN_SIZE // 2, -SCREEN_SIZE // 2)  # Move to the bottom-left corner of the screen
    turtle.pendown()  # Place the pen down

    for _ in range(4):
        turtle.forward(SCREEN_SIZE)
        turtle.left(90)

    for row in range(GRID_SIZE - 1):
        turtle.penup()
        turtle.goto(-SCREEN_SIZE // 2, (row + 1) * SQUARE_SIZE - SCREEN_SIZE // 2)
        turtle.pendown()
        turtle.forward(SCREEN_SIZE)

    turtle.right(90)

    for col in range(GRID_SIZE - 1):
        turtle.penup()
        turtle.goto((col + 1) * SQUARE_SIZE - SCREEN_SIZE // 2, -SCREEN_SIZE // 2)
        turtle.pendown()
        turtle.forward(SCREEN_SIZE)

    turtle.penup()  # Lift the pen at the end
    turtle.hideturtle()  # Hide the turtle

# Function to draw the chess pieces on the board
def draw_pieces():
    turtle.penup()  # Lift the pen
    turtle.goto(-SCREEN_SIZE // 2 + SQUARE_SIZE // 2, -SCREEN_SIZE // 2 + SQUARE_SIZE // 2)  # Move to the first square
    turtle.pendown()  # Place the pen down

    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            piece = chessboard[row][col]
            if piece != '':
                turtle.write(piece, align='center', font=('Arial', 24, 'normal'))

            turtle.forward(SQUARE_SIZE)
        turtle.backward(SCREEN_SIZE)
        turtle.right(90)
        turtle.forward(SQUARE_SIZE)
        turtle.left(90)

    turtle.penup()  # Lift the pen at the end
    turtle.hideturtle()  # Hide the turtle

# Main code
#Initialize  the chessboard
chessboard = [
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['', '', '', '', '', '', '', ''],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
]
draw_chessboard()
draw_pieces()

turtle.done()
# Function to move a chess piece
def move_piece(start_pos, end_pos):
    start_row, start_col = start_pos
    end_row, end_col = end_pos

    piece = chessboard[start_row][start_col]
    chessboard[start_row][start_col] = ''
    chessboard[end_row][end_col] = piece

# Function to print the chessboard
def print_chessboard():
    for row in chessboard:
        for square in row:
            print(square, end=' ')
        print()
# Function to convert algebraic notation to indices
def convert_to_indices(position):
    row = 8 - int(position[1])
    col = ord(position[0].lower()) - ord('a')
    return (row, col)

# Function to convert indices to algebraic notation
def convert_to_algebraic(position):
    row = 8 - position[0]
    col = chr(position[1] + ord('a'))
    return col + str(row)
# Function to check if the user has won
def check_win():
    for row in chessboard:
        if 'k' not in row:
            return True
    return False
# Main game loop
while True:
    print_chessboard()
    print()

    start_input = input("Enter the starting position (e.g., A2): ")
    end_input = input("Enter the ending position (e.g., A4): ")

    start_pos = convert_to_indices(start_input)
    end_pos = convert_to_indices(end_input)

    move_piece(start_pos, end_pos)

    print()
    print("Piece moved from", start_input, "to", end_input)
    print()
    if check_win():
        print("Congratulations! You have won!")
        break

    print()
    print("Piece moved from", start_input, "to", end_input)
    print()
print_chessboard()
