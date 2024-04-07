import random

def create_board():
    """Creates the initial 4x4 board with two random '2' tiles"""
    board = [[0 for _ in range(4)] for _ in range(4)]
    add_new_tile(board)
    add_new_tile(board)
    return board

def add_new_tile(board):
    """Adds a new '2' tile to a random empty spot on the board"""
    empty_cells = [(r, c) for r in range(4) for c in range(4) if board[r][c] == 0]
    if empty_cells:
        row, col = random.choice(empty_cells)
        board[row][col] = 2

def print_board(board):
    """Prints the board in a grid format"""
    for row in board:
        print(" ".join(str(tile).center(5) for tile in row))

def shift_row(row):
    """Shifts tiles in a row to the left, combining matching tiles"""
    # Filter out zeros 
    tiles = [tile for tile in row if tile != 0]

    # Merge tiles
    i = 0
    while i < len(tiles) - 1:
        if tiles[i] == tiles[i + 1]:
            tiles[i] *= 2
            del tiles[i + 1]
        i += 1

    # Append zeros to fill in the row
    tiles.extend([0] * (4 - len(tiles)))
    return tiles

def shift_board_left(board):
    """Shifts all rows left"""
    for i in range(4):
        board[i] = shift_row(board[i])
    return board

def transpose(board):
    """Transposes the board (swaps rows and columns)"""
    return [list(row) for row in zip(*board)]

def shift_board_up(board):
    """Shifts the board up"""
    board = transpose(board)
    board = shift_board_left(board)
    board = transpose(board)
    return board

def shift_board_down(board):
    """Shifts the board down"""
    board = transpose(board)
    board = shift_board_right(board)
    board = transpose(board)
    return board

def shift_board_right(board):
    """Shifts the board right"""
    for i in range(4):
        board[i] = shift_row(board[i][::-1])[::-1]  # Reverse, shift, reverse back
    return board

# Main game loop
board = create_board()
print_board(board)

while True:
    direction = input("Choose a direction (w: up, s: down, a: left, d: right): ").lower()

    if direction == 'w':
        board = shift_board_up(board)
    elif direction == 's':
        board = shift_board_down(board)
    elif direction == 'a':
        board = shift_board_left(board)
    elif direction == 'd':
        board = shift_board_right(board)
    else:
        print("Invalid direction")
        continue

    add_new_tile(board)
    print_board(board)
