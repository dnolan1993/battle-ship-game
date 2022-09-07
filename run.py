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


def check_for_oob(board, coordinates):
    """
    For a given list of ship coordinates check if any are oob (off of board)
    for the board
    """
    for i in coordinates:
        if i[0] < 0 or i[0] > len(board)-1:  # Board is a list of rows
            return True
        elif i[1] < 0 or i[1] > len(board[0])-1:  # Each row is a list of cols
            return True
    return False


def check_ship_conflict(board, coordinates):
    """
    For a given set of coordinates see if they conflict with other ships
    """
    for coordinate in coordinates:
        row, col = coordinate[0], coordinate[1]
        if get_coordinate_value(board, row, col) == "#":
            return True
    return False


def check_valid_placement(board, coordinates):
    """
    Given a board and set of coordinates
    return if its a valid place to place a ship
    """
    if check_for_oob(board, coordinates):
        return False
    elif check_ship_conflict(board, coordinates):
        return False
    return True


def get_coordinate_value(board, row, col):
    """
    For a given board return the value of a coordinate
    """
    return board[row][col]


def get_empty_coordinate(board):
    """
    For a given board find a random empty coordinate
    """
    empty = False

    while not empty:
        row, col = randint(0, 7), randint(0, 7)
        coordinate_value = get_coordinate_value(board, row, col)
        if coordinate_value == " ":
            empty = True
    return row, col


def get_random_direction():
    """
    Return a random direction
    """
    directions = {0: "up",
                  1: "down",
                  2: "left",
                  3: "right"}
    return directions[randint(0, 3)]


def generate_ship_coordinates(length, row, col):
    """"
    Given a start point generate a set of coordinates for a ship
    """
    direction = get_random_direction()
    coordinates = []

    if direction == "up":
        for i in range(length):
            coordinates.append([row - i, col])

    elif direction == "down":
        for i in range(length):
            coordinates.append([row + i, col])

    elif direction == "left":
        for i in range(length):
            coordinates.append([row, col - i])

    else:  # Right
        for i in range(length):
            coordinates.append([row, col + i])
    return coordinates


def place_ship_on_board(board, ship_coordinates):
    """
    Given a board and a ships coordinates update the board
    with the ship and return the updated board
    """
    for coordinate in ship_coordinates:
        row, col = coordinate[0], coordinate[1]
        board[row][col] = "#"
    return board


def get_ship_row():
    """
    Allow player to input a guess for row value
    """
    try:
        guess_row = int(input("Please guess a row between 1 and 8: "))
        if guess_row <= 8 and guess_row > 0:
            return guess_row - 1
        else:
            print("please enter valid row number")
            guess_row = int(input("Please guess a row between 1 and 8: "))
            return guess_row - 1
    except ValueError:
        print("You must guess a number")
        guess_row = int(input("Please guess a row between 1 and 8: "))
        return guess_row - 1


def get_ship_column():
    """
    Allow player to input a guess for column value
    """
    column_dict = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    guess_column = None
    while guess_column not in column_dict.keys():
        guess_column = input("Please guess a column A-H: ")
    return column_dict[guess_column]


def get_player_coordinate():
    """
    Store the players guess as a list
    """
    player_row_column = [get_ship_row(), get_ship_column()]
    return player_row_column


def get_computer_coordinate(board):
    """
    Generates random coordinates for computer guess
    """
    not_a_miss = False
    while not not_a_miss:
        row, col = randint(0, 7), randint(0, 7)
        if get_coordinate_value(board, row, col) != "*":
            not_a_miss = True
    return [row, col]


def make_a_move(board, coordinate):
    """
    Print guess coordinates to choosen board
    """
    row = coordinate[0]
    col = coordinate[1]
    if get_coordinate_value(board, row, col) == " ":
        board[row][col] = "-"
        print("It's a miss!")
    elif get_coordinate_value(board, row, col) == "#":
        board[row][col] = "X"
        print("It's a hit!")
    elif get_coordinate_value(board, row, col) == "-":
        print("Positioned already guessed!")
        return None
    return board


def hit_ships(board):
    """
    Count the amount of hits on chosen board
    """
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


def check_win(board):
    """
    Check if all ships have been hit
    """
    if hit_ships(board) == 10:
        print(f"Game Over! all ship on have been sunk!")
        return True
    return False


def print_winner(winner, player_board, opponent_board):
    """
    Prints winner when all ships on either board are sunk
    """
    if winner == "Player" or hit_ships(player_board) < hit_ships(opponent_board):
        print("Congratulations! You Win!")
    elif winner == "Opponent" or hit_ships(player_board) > hit_ships(opponent_board):
        print("You Lose!, Better luck next time.")
    else:
        print("It's a Draw, Try again")