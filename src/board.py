PIECE = {'Pawn': 1, 'Knight': 2, 'Bishop': 3, 'Rook': 4, 'Queen': 5, 'King': 6}
COLORS = {'White': 1, 'Black': 2}
PAWN = [(1,0), (2,0), (1,1), (1,-1)]
KNIGHT = [(1,2), (2,1), (2,-1), (1,-2), (-1,-2)]
BISHOP = [(1,1), (1,-1), (-1,1), (-1,-1)]
ROOK = [(1,0), (0,1), (-1,0), (0,-1)]
QUEEN = [(1,0), (2,0), (1,1), (1,-1), (0,1), (0,-1), (-1,0), (-1,1), (-1,-1)]
KING = [(1,0), (2,0), (1,1), (1,-1), (0,1)]

class Piece:
   def __init__(self):
      self.has_moved = False

def is_on_board(x, y):
    return 0 <= x < 8 and 0 <= y < 8

def is_empty(self, x, y):
    return self.board[x][y] == None

def is_enemy(self, x, y, color):
    piece = self.board[x][y]
    return piece is not None and piece.color != color

def generate_pawn_moves(self, start_pos):
    moves = []
    x, y = start_pos
    if not self.pieces[start_pos].has_moved:
        moves.append((x, y + 2))
    if is_on_board(x, y + 1) and is_empty(x, y + 1):
        moves.append((x, y + 1))

def generate_knight_moves(self, start_pos):
  moves = []
  for d in KNIGHT:
    x, y = start_pos[0] + d[0], start_pos[1] + d[1]
    if is_on_board(x, y) and is_empty(x, y):
      moves.append((x, y))

  return moves

def generate_legal_moves(self, start_pos):

  piece = self.pieces[start_pos]

  if piece.type == PAWN:
    return generate_pawn_moves(start_pos)
  elif piece.type == KNIGHT:
    return generate_knight_moves(start_pos)
    
def is_on_board(x, y):

def is_empty(self, x, y):

def is_enemy(self, x, y, color):