from enum import Enum


class Color(Enum):
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    ORANGE = (255, 165 ,0)
    PURPLE = (128, 0, 128)
    TURQUOISE = (64, 224, 208)
    

class State(Enum): 
    START = Color.ORANGE
    END = Color.PURPLE
    VISITED = Color.TURQUOISE
    UNVISITED = Color.WHITE
    BARRIER = Color.BLACK

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = Color.WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
    
    def get_pos(self): 
        return (self.row, self.col)



