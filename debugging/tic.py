#!/usr/bin/python3

def print_board(board):
    """
    Print the current state of the Tic-Tac-Toe board with exact formatting.

    Parameters:
    board (list of list of str): The 3x3 board to be printed.
    """
    # Define the number of columns and the width of each cell
    num_cols = len(board[0])
    cell_width = 5  # Adjust width of each cell to match the desired output

    # Create the horizontal separator line
    separator = "-" * (num_cols * cell_width + (num_cols + 1))

    # Print the board with vertical and horizontal separators
    print(separator)  # Print the top border
    for row in board:
        print("|", " | ".join(f"{cell:^{cell_width}}" for cell in row), "|")  # Format each cell
        print(separator)  # Print the horizontal separator

def check_winner(board):
    """
    Check if there is a winner on the Tic-Tac-Toe board.

    Parameters:
    board (list of list of str): The 3x3 board to check for a winner.

    Returns:
    bool: True if there is a winner, False otherwise.
    """
    # Check rows for a win
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a win
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """
    Run a game of Tic-Tac-Toe where two players alternate turns.
    """
    board = [[" "]*3 for _ in range(3)]  # Initialize a 3x3 board
    player = "X"  # Player "X" starts the game

    while not check_winner(board):
        print_board(board)  # Display the board
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if 0 <= row < 3 and 0 <= col < 3:  # Ensure the input is within bounds
                if board[row][col] == " ":
                    board[row][col] = player  # Place the player's mark
                    player = "O" if player == "X" else "X"  # Switch players
                else:
                    print("That spot is already taken! Try again.")
            else:
                print("Invalid row or column. Please enter values between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 2.")

    print_board(board)  # Display the final board
    print("Player " + player + " wins!")  # Announce the winner

# Run the Tic-Tac-Toe game
tic_tac_toe()
