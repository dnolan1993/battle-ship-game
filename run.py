from random import randint

opponent_ship_row = []
opponent_ship_column = []


class board():
    def __init__(self, grid_size):
        self.grid = [[" "] * grid_size for x in range(grid_size)]

    def print_board(self, opponent=False):
        """
        For a given grid print it to the terminal
        """
        if opponent:
            print("---------Opponents Board----------")
        else:
            print("-----------Your Board-------------")
        print("    A   B   C   D   E   F   G   H")
        print("----------------------------------")

        row_number = 1
        for row in self.grid:
            col_str = f"{row_number} |"
            for col in row:
                if opponent and col == "#":
                    val = " "
                else:
                    val = col
                col_str += f" {val} |"
            print(col_str)
            row_number += 1

    def check_for_oob(self, coordinates):
        """
        For a given list of ship coordinates check if any are oob for the grid
        """
        for i in coordinates:
            if i[0] < 0 or i[0] > len(self.grid)-1:  # Grid is a list of rows
                return True
            elif i[1] < 0 or i[1] > len(self.grid[0])-1:  # Each row is a list of cols
                return True
        return False

    def check_ship_conflict(self, coordinates):
        """
        For a given set of coordinates see if they conflict with other ships
        """
        for coordinate in coordinates:
            row, col = coordinate[0], coordinate[1]
            if self.get_coordinate_value(row, col) == "#":
                return True
        return False

    def check_valid_placement(self, coordinates):
        """
        Given a board and set of coordinates
        return if its a valid place to place a ship
        """
        if self.check_for_oob(coordinates):
            return False
        elif self.check_ship_conflict(coordinates):
            return False
        return True

    def get_coordinate_value(self, row, col):
        """
        For a given coordinate return its value
        """
        return self.grid[row][col]

    def update_coordinate_value(self, row, col, value):
        """
        For a given coordinate update its value
        """
        self.grid[row][col] = value

    def get_empty_coordinate(self):
        """
        For a given grid find a random empty coordinate
        """
        empty = False

        while not empty:
            row, col = randint(0, 7), randint(0, 7)
            coordinate_value = self.get_coordinate_value(row, col)
            if coordinate_value == " ":
                empty = True
        return row, col

    def place_ship_on_board(self, ship_coordinates):
        """
        Given a grid and a ships coordinates update the grid
        with the ship
        """
        for coordinate in ship_coordinates:
            row, col = coordinate[0], coordinate[1]
            self.grid[row][col] = "#"

    def get_random_direction(self):
        """
        Return a random direction
        """
        directions = {0: "up",
                      1: "down",
                      2: "left",
                      3: "right"}
        return directions[randint(0, 3)]

    def create_ships(self, ships):
        """
        For a given board place the number of ships required
        """
        for i in ships:
            row, col = self.get_empty_coordinate()
            valid_placement = False
            while not valid_placement:
                row, col = self.get_empty_coordinate()
                coordinates = self.generate_ship_coordinates(i, row, col)
                if self.check_valid_placement(coordinates):
                    self.place_ship_on_board(coordinates)
                    valid_placement = True

    def generate_ship_coordinates(self, length, row, col):
        """"
        Given a start point generate a set of coordinates for a ship
        """
        coordinates = []
        direction = self.get_random_direction()

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

    def hit_ships(self):
        """
        Count the amount of hits on chosen grid
        """
        count = 0
        for row in self.grid:
            for column in row:
                if column == "X":
                    count += 1
        return count

    def check_win(self):
        """
        Check if all ships have been hit
        """
        if self.hit_ships() == 10:
            print(f"Game Over! all ship on have been sunk!")


# End of Board Class


def get_ship_row():
    """
    Allow player to input a guess for row value
    """
    guess_row = 0
    while guess_row < 1 or guess_row > 8:
        try:
            guess_row = int(input("Please guess a row between 1 and 8:\n"))
            if guess_row <= 8 and guess_row > 0:
                return guess_row - 1
            else:
                print("please enter valid row number")
                guess_row = int(input("Please guess a row between 1 and 8:\n"))
                return guess_row - 1
        except ValueError:
            print("You must guess a number")
            guess_row = int(input("Please guess a row between 1 and 8:\n"))
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
        if board.get_coordinate_value(row, col) != "*":
            not_a_miss = True
    return [row, col]


def make_a_move(board, coordinate):
    """
    Print guess coordinates to choosen board
    """
    row = coordinate[0]
    col = coordinate[1]
    if board.get_coordinate_value(row, col) == " ":
        board.update_coordinate_value(row, col, "-")
        print("It's a miss!")
    elif board.get_coordinate_value(row, col) == "#":
        board.update_coordinate_value(row, col, "X")
        print("It's a hit!")
    elif board.get_coordinate_value(row, col) == "-" or board.get_coordinate_value(row, col) == "X":
        print("Positioned already guessed! Annnd you've wasted a turn!")
        return None
    return board


def print_winner(winner, player_board, opponent_board):
    """
    Prints winner when all ships on either board are sunk
    """
    if winner == "Player" or player_board.hit_ships() < opponent_board.hit_ships():
        print("Congratulations! You Win!")
    elif winner == "Opponent" or player_board.hit_ships(player_board) > opponent_board.hit_ships():
        print("You Lose!, Better luck next time.")
    else:
        print("It's a Draw, Try again")


def run_game(turns, player_board, opponent_board):
    """Runs the main game loop"""

    while turns > 0:
        # Players turn
        coordinate = get_player_coordinate()
        make_a_move(opponent_board, coordinate)
        if opponent_board.check_win():
            return "Player"
        # Computers turn
        coordinate = get_computer_coordinate(player_board)
        make_a_move(player_board, coordinate)
        if player_board.check_win():
            return "Opponent"

        opponent_board.print_board(opponent=True)
        player_board.print_board()
        print(f"Opponents hits: {player_board.hit_ships()}")
        print(f"Player hits: {opponent_board.hit_ships()}")
        turns -= 1
        print(f"Turns remaining: {turns}")
    return "Draw"


def main():
    """
    Calls all functions needed to run game
    """
    opponent_board = board(8)
    player_board = board(8)
    ships = [2, 4, 4]
    print("  = empty place")
    print("- = a missed shot")
    print("* = a hit shot")
    print("# = location of your ship")
    opponent_board.create_ships(ships)
    player_board.create_ships(ships)

    opponent_board.print_board(opponent=True)
    player_board.print_board()

    winner = run_game(20, player_board, opponent_board)
    print_winner(winner, player_board, opponent_board)


main()
