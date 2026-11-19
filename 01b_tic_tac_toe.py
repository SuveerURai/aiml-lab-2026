# Question: Write a program to implement a Tic-Tac-Toe game.
"""Two-player Tic-Tac-Toe in the terminal. Enter positions 1 through 9."""

def winner(board):
    lines = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for a,b,c in lines:
        if board[a] and board[a] == board[b] == board[c]:
            return board[a]
    return None

def show(board):
    for row in range(3):
        print(" | ".join(board[row*3:row*3+3]))
        if row < 2: print("---------")

def main():
    board = [str(i) for i in range(1, 10)]
    player = "X"
    moves = 0
    while moves < 9:
        show(board)
        try: pos = int(input(f"{player}, choose a square (1-9): ")) - 1
        except ValueError:
            print("Enter a number from 1 to 9."); continue
        if not 0 <= pos < 9 or board[pos] in ("X", "O"):
            print("That square is unavailable."); continue
        board[pos] = player
        moves += 1
        if winner(board):
            show(board); print(f"{player} wins!"); return
        player = "O" if player == "X" else "X"
    show(board); print("Draw!")

if __name__ == "__main__": main()
