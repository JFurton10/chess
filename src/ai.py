import random

def make_move(self, board):
    moves = []

    for piece in board.pieces_for_color(self.color):
        moves.extend(board.generate_legal_moves(piece.pos))

    start, end = random.choice(moves)

    return start, end
