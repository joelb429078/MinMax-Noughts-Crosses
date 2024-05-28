#MinMax
import numpy as np
import math

class Board:
    def __init__(self):
        self.boardsize = 3
        self.gameboard = np.array([['1', '2', '3'], #numpy board for all positions
                                   ['4', '5', '6'],
                                   ['7', '8', '9']])
                    
    def display(self): #creating the CLI board 
        columns = "   |   |   "
        centerlines = "-----------"
        for i in range(self.boardsize):
            print(columns)
            print(f" {self.gameboard[i][0]} | {self.gameboard[i][1]} | {self.gameboard[i][2]} ")
            print(columns)
            if i < self.boardsize - 1:
                print(centerlines)

class TicTacToe:
    def __init__(self):
        self.currentplayer = "Human" #can either be human or computer
        self.board = Board()
        self.over = False

    def switchplayer(self):
        if self.currentplayer == "Computer": 
            self.currentplayer = "Human"
        else:
            self.currentplayer = "Computer"

    def game(self):
        while not self.over:
            self.board.display()
            if self.currentplayer == "Human":
                move = int(input(f"{self.currentplayer}, enter your move (1-9): "))
            else:
                print("Computer Player making a move...")
                move = self.get_computer_move()
                print(f"Computer chooses move {move + 1}")
            if self.make_move(move + 1):
                if self.checkgameisOver():
                    self.board.display()
                    print(f"The {self.currentplayer} player wins!")
                    self.over = True
                elif self.draw():
                    self.board.display()
                    print("It's a draw!")
                    self.over = True
                else:
                    self.switchplayer()
            else:
                print("Invalid move. Try again.")

    def make_move(self, index):
        row = (index - 1) // 3 
        col = (index - 1) % 3 
        if self.board.gameboard[row][col] in ['X', 'O']:
            return False 
        self.board.gameboard[row][col] = 'X' if self.currentplayer == "Human" else 'O'
        return True

    def checkgameisOver(self):
        #checking the rows and columns
        for i in range(3):
            if all(self.board.gameboard[i, j] == self.board.gameboard[i, 0] for j in range(3)):
                return True
            if all(self.board.gameboard[j, i] == self.board.gameboard[0, i] for j in range(3)):
                return True

        #checking the diagonals
        if self.board.gameboard[0, 0] == self.board.gameboard[1, 1] == self.board.gameboard[2, 2]:
            return True
        if self.board.gameboard[0, 2] == self.board.gameboard[1, 1] == self.board.gameboard[2, 0]:
            return True

        return False

    def draw(self):
        return all(self.board.gameboard[row][col] in ['X', 'O'] for row in range(3) for col in range(3))


    #Computer MinMax - updated now to have alpha beta pruning
    def get_computer_move(self):
        best_score = -math.inf
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board.gameboard[i][j] not in ['X', 'O']:
                    self.board.gameboard[i][j] = 'O' #making a move for that non-empty space
                    score = self.minimax(0, False, -math.inf, math.inf)
                    self.board.gameboard[i][j] = str(i * 3 + j + 1) #Undoing the move to do next move
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        return best_move[0] * 3 + best_move[1]

    def minimax(self, depth, isMaximising, alpha, beta): 
        if self.checkgameisOver():
            return 1 if not isMaximising else -1
        if self.draw():
            return 0

        if isMaximising: #maximising 
            best_score = -math.inf #worst cas scenario value
            for i in range(3):
                for j in range(3):
                    if self.board.gameboard[i][j] not in ['X', 'O']:
                        self.board.gameboard[i][j] = 'O'
                        score = self.minimax(depth + 1, False, alpha, beta)
                        self.board.gameboard[i][j] = str(i * 3 + j + 1)
                        best_score = max(score, best_score)
                        alpha = max(alpha, best_score)
                        if beta <= alpha:
                            break
            return best_score
        else: #minimising 
            best_score = math.inf
            for i in range(3):
                for j in range(3):
                    if self.board.gameboard[i][j] not in ['X', 'O']:
                        self.board.gameboard[i][j] = 'X'
                        score = self.minimax(depth + 1, True, alpha, beta)
                        self.board.gameboard[i][j] = str(i * 3 + j + 1)
                        best_score = min(score, best_score)
                        beta = min(beta, best_score)
                        if beta <= alpha:
                            break
            return best_score

if __name__ == "__main__":
    game = TicTacToe()
    game.game()
