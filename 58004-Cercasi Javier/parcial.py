import sys
import math

class Sudoku():

    def __init__(self, tabla, tamano):
        self.tamano = tamano 
        self.is_playing = True
        self.matriz = [ [ 0 for __ in range(self.tamano) ] for _ in range(self.tamano) ]
        self.fijos = [ [ 0 for __ in range(self.tamano) ] for _ in range(self.tamano) ]
        self.string_converter(tabla)
        dsaads