#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

class TicTacToe:
    def __init__(self):
        self.board = [' ' for x in range(9)]
        self.player = 'X'
        self.computer = 'O'

    def print_board(self):
        print(self.board[0] + '|' + self.board[1] + '|' + self.board[2])
        print('-+-+-')
        print(self.board[3] + '|' + self.board[4] + '|' + self.board[5])
        print('-+-+-')
        print(self.board[6] + '|' + self.board[7] + '|' + self.board[8])

    def check_win(self):
        # check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] and self.board[i] != ' ':
                return self.board[i]
        # check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] and self.board[i] != ' ':
                return self.board[i]
        # check diagonals
        if self.board[0] == self.board[4] == self.board[8] and self.board[0] != ' ':
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] and self.board[2] != ' ':
            return self.board[2]
        return None

    def check_tie(self):
        for i in range(9):
            if self.board[i] == ' ':
                return False
        return True

    def minimax(self, board, player):
        winner = self.check_win()
        if winner is None:
            if self.check_tie():
                return 0
            scores = []
            moves = []
            for i in range(9):
                if board[i] == ' ':
                    new_board = board.copy()
                    new_board[i] = player
                    if player == self.computer:
                        scores.append(self.minimax(new_board, self.player))
                    else:
                        scores.append(self.minimax(new_board, self.computer))
                    moves.append(i)
            if not scores:
                return 0
            if player == self.computer:
                max_score_index = scores.index(max(scores))
                return moves[max_score_index]
            else:
                min_score_index = scores.index(min(scores))
                return moves[min_score_index]
        else:
            if winner == self.computer:
                return 1
            elif winner == self.player:
                return -1
            else:
                return 0
            
            
    def play(self):
        while True:
            self.print_board()
            print("Your move (0-8):")
            move = int(input())
            if self.board[move] == ' ':
                self.board[move] = self.player
            else:
                print("Invalid move. Try again.")
                continue
            if self.check_win():
                self.print_board()
                if self.check_win() == self.player:
                    print("You win!")
                elif self.check_win() == self.computer:
                    print("You lose.")
                else:
                    print("Tie.")
                break
            elif self.check_tie():
                self.print_board()
                print("Tie.")
                break
            self.board[self.minimax(self.board, self.computer)] = self.computer
            if self.check_win():
                self.print_board()
                if self.check_win() == self.player:
                    print("You win!")
                elif self.check_win() == self.computer:
                    print("You lose.")
                else:
                    print("Tie.")
                break
            elif self.check_tie():
                self.print_board()
                print("Tie.")
                break
                
game = TicTacToe()
game.play()


# In[ ]:




