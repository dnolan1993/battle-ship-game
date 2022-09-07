from random import randint

def print_board(board, opponent=False):
    """
    For a given board print it to the terminal
    """
    if opponent:
        print("---------Opponents Board----------")
    else:
        print("-----------Your Board-------------")
    print("    A   B   C   D   E   F   G   H")
    print("----------------------------------")

    row_number = 1
    for row in board:
        col_str = f"{row_number} |"
        for col in row:
            if opponent and col == "#":
                val = " "
            else:
                val = col
            col_str += f" {val} |"
        print(col_str)
        row_number += 1


def create_ships(board, ships):
    """
    For a given board place the number of ships required
    """
    for i in ships:
        valid_placement = False
        while not valid_placement:
            row, col = get_empty_coordinate(board)
            coordinates = generate_ship_coordinates(i, row, col)
            if check_valid_placement(board, coordinates):
                valid_placement = True

        board = place_ship_on_board(board, coordinates)
    return board