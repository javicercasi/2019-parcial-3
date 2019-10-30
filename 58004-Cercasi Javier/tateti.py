import sys
import math

class TaTeTi():

    def __init__(self,board=None):
        if not board:
            board = [' ' for _ in range(9)]
        self.board= board
        self.board_new=[' ' for _ in range(9)]
        self.board_old=board

    def full (self):
        c=0
        for i in range(9):
            if self.board[i] != ' ':
                c+=1

        if c == 9:
            return True
        else:
            return False

    def win(self):

        if self.board[0]!= ' ' and self.board[0]==self.board[3] and self.board[3]==self.board[6]:
            return True
        if self.board[1]!= ' ' and self.board[1]==self.board[4] and self.board[4]==self.board[7]:
            return True
        if self.board[2]!= ' ' and self.board[2]==self.board[5] and self.board[5]==self.board[8]:
            return True
        if self.board[0]!= ' ' and self.board[0]==self.board[1] and self.board[1]==self.board[2]:
            return True
        if self.board[0] != ' ' and self.board[0]==self.board[4] and self.board[4]==self.board[8]:
            return True
        if self.board[2]!= ' ' and self.board[2]==self.board[4] and self.board[4]==self.board[6]:
            return True
        if self.board[3]!= ' ' and self.board[3]==self.board[4] and self.board[4]==self.board[5]:
            return True
        if self.board[6]!= ' ' and self.board[6]==self.board[7] and self.board[7]==self.board[8]:
            return True
        return False

    def validate (self,posicion):
        return(self.board[posicion-1] == ' ')

    def assign (self,posicion,piece):
        
        if self.validate(posicion) is False:
            raise Exception
        
        if self.validate(posicion):
            self.board[posicion-1]=piece

    def draw_board(self):
        self.display = "\n"
        for valor in range(9):
            if self.board[valor] != ' ':
                self.display += ' ' + self.board[valor] + ' '

            else:
                self.display += ' ' + str(valor+1) + ' '

            if valor == 2 or valor == 5:
                self.display += ("\n---+---+---\n")

            elif valor == 8:
                self.display += ("\n")
            else:

                self.display += ("|")

        return self.display  


        

    def play(self):
        self.full()
        self.draw_board()


if __name__ == "__main__":
    I = TaTeTi()
    I.play()