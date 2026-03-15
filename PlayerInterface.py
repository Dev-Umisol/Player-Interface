from abc import ABC, abstractmethod
import random

class Player(ABC):
    """ Abstract base class representing.  player that moves on a 2D grid """
    
    def __init__(self):
        self.moves = [] # available moves, defined by concrete classes
        self.position = (0, 0) # Starting position
        self.path = [self.position] # History of all positions visited
    
    def make_move(self):
        """ Pick a random move, update position, and record it in the path """
        random_moves = random.choice(self.moves)
        
        self.position = (random_moves[0] + self.position[0], random_moves[1] + self.position[1])
        self.path.append(self.position)
        
        return self.position
    
    @abstractmethod
    def level_up(self):
        """ Expand available moves when the player levels up """
        pass

class Pawn(Player):
    """ A basic player that moves one unit in the four cardinal directions """
    
    def __init__(self):
        super().__init__()
        self.moves = [(1, 0), (-1, 0), (0, -1), (0, 1)] # <-- right, left, down, up

    def level_up(self):
        """ Adds diagonal moves when the pawn levels up """
        self.moves += [(1,1), (-1,1), (-1, -1), (1, -1)]