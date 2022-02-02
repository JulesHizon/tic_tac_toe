import random
import time

class Game():
    
    def __init__(self, opponent='computer'):
        self.board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.opponent = opponent
        self.counter = 0
        self.winner = False
        self.print_board()

    def print_board(self):
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}")
        print('---------')
        print(f"{self.board[3]} | {self.board[4]} | {self.board[5]}")
        print('---------')
        print(f"{self.board[6]} | {self.board[7]} | {self.board[8]}")

    def get_moves(self):
        self.available_moves = [i for i, val in enumerate(self.board) if val == ' ']
        return self.available_moves

    def xmove(self):
        print("X's Turn.")
        move = int(input('Please input a space between 0-8 to make a move.'))
        if move in self.get_moves():
            self.board[move] = 'X'
            self.counter += 1
            self.print_board()
            self.check_for_winner()
        else:
            print('That is not a valid move. Please try again.')
            self.print_board()
            return self.xmove()

    def omove(self):
        print("O's Turn.")

        if self.opponent == 'computer':
            move = random.choice(self.get_moves())
            self.board[move] = 'O'
            self.counter += 1
            self.print_board()
            self.check_for_winner()

        else:
            move = int(input('Please input a space between 0-8 to make a move.'))
            if move in self.get_moves():
                self.board[move] = 'O'
                self.counter += 1
                self.print_board()
                self.check_for_winner()
            else:
                print('That is not a valid move. Please try again.')
                self.print_board()
                return self.omove()

    def check_for_winner(self):
        # x_player win conditions
        if self.board[0] == 'X' and self.board[1] == 'X' and self.board[2] == 'X':
            self.winner = True
            print('X wins!')
            self.print_board()
            
        elif self.board[3] == 'X' and self.board[4] == 'X' and self.board[5] == 'X':
            self.winner = True
            print('X wins!')
            self.print_board()
            
        elif self.board[6] == 'X' and self.board[7] == 'X' and self.board[8] == 'X':
            self.winner = True
            print('X wins!')
            self.print_board()
            
        elif self.board[0] == 'X' and self.board[3] == 'X' and self.board[6] == 'X':
            self.winner = True
            print('X wins!')
            self.print_board()
            
        elif self.board[1] == 'X' and self.board[4] == 'X' and self.board[7] == 'X':
            self.winner = True
            print('X wins!')
            self.print_board()
            
        elif self.board[2] == 'X' and self.board[5] == 'X' and self.board[8] == 'X':
            self.winner = True
            print('X wins!')
            self.print_board()
            
        elif self.board[0] == 'X' and self.board[4] == 'X' and self.board[8] == 'X':
            self.winner = True
            print('X wins!')
            self.print_board()
            
        elif self.board[2] == 'X' and self.board[4] == 'X' and self.board[6] == 'X':
            self.winner = True
            print('X wins!')
            self.print_board()
            

        # o_player win conditions
        elif self.board[0] == 'O' and self.board[1] == 'O' and self.board[2] == 'O':
            self.winner = True
            print('O wins!')
            self.print_board()
            
        elif self.board[3] == 'O' and self.board[4] == 'O' and self.board[5] == 'O':
            self.winner = True
            print('O wins!')
            self.print_board()
            
        elif self.board[6] == 'O' and self.board[7] == 'O' and self.board[8] == 'O':
            self.winner = True
            print('O wins!')
            self.print_board()
            
        elif self.board[0] == 'O' and self.board[3] == 'O' and self.board[6] == 'O':
            self.winner = True
            print('O wins!')
            self.print_board()
            
        elif self.board[1] == 'O' and self.board[4] == 'O' and self.board[7] == 'O':
            self.winner = True
            print('O wins!')
            self.print_board()
            
        elif self.board[2] == 'O' and self.board[5] == 'O' and self.board[8] == 'O':
            self.winner = True
            print('O wins!')
            self.print_board()
            
        elif self.board[0] == 'O' and self.board[4] == 'O' and self.board[8] == 'O':
            self.winner = True
            print('O wins!')
            self.print_board()
            
        elif self.board[2] == 'O' and self.board[4] == 'O' and self.board[6] == 'O':
            self.winner = True
            print('O wins!')
            self.print_board()
            

        elif len(self.get_moves()) == 0:
            self.winner = True
            self.print_board()
            print('Tie! No more moves available.')

if __name__ == '__main__':
    
    game = Game(opponent='computer')

    while not game.winner:
        if game.counter % 2 == 0:
            time.sleep(0.5)
            game.xmove()
        else:
            time.sleep(0.5)
            game.omove()
