# game.py

from board import Board
from human import HumanPlayer
from ai import AIPlayer

class Game:

  def __init__(self):
    self.board = Board()
    self.human = HumanPlayer('white') 
    self.ai = AIPlayer('black')

  def play(self):
    current_player = self.human 

    while True:
      start, end = current_player.make_move(self.board)
      self.board.make_move(start, end)

      if self.board.in_checkmate(current_player.color):
        if current_player == self.human:
          print("yeeve lost!")
        else:
          print("yeeve won!")
        break

      if current_player == self.human:
        current_player = self.ai
      else:
        current_player = self.human

game = Game()
game.play()
