#Name: Lydia Mayenge
#Date: 05/18/2021
#This code allows me to move chess pieces across a chessboard

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