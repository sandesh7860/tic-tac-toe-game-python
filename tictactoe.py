import random
import os.path
import json

board_path = "board.json"

def load_board():
    if os.path.isfile(board_path):
        with open(board_path, 'r'):
            return json.load(open(board_path, 'rb'))

random.seed()

def draw_board(board):
    print("+-------+")
    for row in board:
        print("|" + "|".join(row) + "|")
        print("+-------+")

def welcome(board):
    print("Welcome to Tic Tac Toe!\n")
    draw_board(board)

def initialise_board(board):
    for i in range(3):
        for j in range(3):
            board[i][j] = " "
    return board

def get_player_move(board):
    while True:
        try:
            row = int(input("Enter the row number (1-3): "))
            col = int(input("Enter the column number (1-3): "))
            if row < 1 or row > 3 or col < 1 or col > 3:
                raise ValueError
            if board[row-1][col-1] != " ":
                print("That cell is already occupied. Try again.")
                continue
            return row-1, col-1
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

def choose_computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            return row, col

def check_for_win(board, mark):
    # check rows
    for i in range(3):
        if all(board[i][j] == mark for j in range(3)):
            return True
    # check columns
    for j in range(3):
        if all(board[i][j] == mark for i in range(3)):
            return True
    # check diagonals
    if all(board[i][i] == mark for i in range(3)):
        return True
    if all(board[i][2-i] == mark for i in range(3)):
        return True
    return False

def check_for_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def play_game(board):
    initialise_board(board)
    draw_board(board)
    while True:
        # Player's turn
        row, col = get_player_move(board)
        board[row][col] = "X"
        draw_board(board)
        if check_for_win(board, "X"):
            print("You win!")
            return 1
        if check_for_draw(board):
            print("It's a draw!")
            return 0
        # Computer's turn
        row, col = choose_computer_move(board)
        board[row][col] = "O"
        draw_board(board)
        if check_for_win(board, "O"):
            print("Computer wins!")
            return -1
        if check_for_draw(board):
            print("It's a draw!")
            return 0

def menu():
    while True:
        print("Main Menu")
        print("1. Play the game")
        print("2. Save score in file 'scores.txt'")
        print("3. Load and display the scores from the 'scores.txt'")
        print("q. Quit the program")
        choice = input("Enter your choice: ")
        if choice in ["1", "2", "3", "q"]:
            return choice
        else:
            print("Invalid input. Please enter a number between 1 and 3 or 'q' to quit.")

def load_scores():
    try:
        with open("scores.txt") as f:
            return [tuple(line.strip().split()) for line in f]
    except FileNotFoundError:
        return []
    

def save_score(score):
    name = input("Enter your name: ")
    with open('leaderboard.txt', 'a') as f:
        f.write(f"{name}: {score}\n")


def display_leaderboard(leaders):
    print("LEADERBOARD\n")
    for name, score in leaders.items():
        print(f"{name}: {score}")


def main():
    board = [ ['1','2','3'],\
              ['4','5','6'],\
              ['7','8','9']]

    welcome(board)
    total_score = 0
    while True:
        choice = menu()
        if choice == '1':
            score = play_game(board)
            total_score += score
            print('Your current score is:',total_score)
        if choice == '2':
            save_score(total_score)
        if choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good bye')
            return


# Program execution begins here
if __name__ == '__main__':
    main()


