#CSE 210 Week 2 Tic-Tac-Toe
#Author: Kelsey Scott

def main():
    board = start_game()
    player = next_turn("X")

    while not (win(board) or tie(board)):
        display_board(board)
        move(board,player)
        player = next_turn(player)
    display_board(board)

    if win(board):
      display_winner(player)
    else:
      print("Tie Game.")
    print("Good game. Thanks for playing!")


def next_turn(player):
    if  player == "X":
        return "O"
    elif player == "O":
        return "X"

def start_game():
    board = []
    for block in range(9):
        board.append(block + 1)
    return board

def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

def move(board, player):
    block = int(input(f"Player {player}, please select a square between 1-9: "))
    board[block - 1] = player

def win(board):
    return (board[0] == board[1] == board[2] or
            board[0] == board[4] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[2] == board[4] == board[6] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8]
            )

def display_winner(player):
    if  player == "X":
        print(f"Congrats Play O, you win!")
    elif player == "O":
        print(f"Congrats Play X, you win!")


def tie(board):
    if not win(board) and (
      board[0] != 1 and
      board[1] != 2 and
      board[2] != 3 and
      board[3] != 4 and
      board[4] != 5 and
      board[5] != 6 and
      board[6] != 7 and
      board[7] != 8 and
      board[8] != 9):
      return True
    else:
      return False

if __name__ == "__main__":
    main()



