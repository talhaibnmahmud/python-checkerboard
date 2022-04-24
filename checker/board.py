import pygame

from .constants import COL, ROW, SQUARE_SIZE
from .piece import Piece


class Board:
    def __init__(self):
        self.selected_piece = None
        self.black_left = self.white_left = 12
        self.black_kings = self.white_kings = 0

        self.create_board()

    def draw_squares(self, win: pygame.Surface):
        win.fill('#808000')
        for row in range(ROW):
            for col in range(row % 2, COL, 2):
                pygame.draw.rect(
                    win,
                    (218, 160, 109),
                    (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                )

    def create_board(self):
        self.board: list[list[Piece | None]] = []
        for row in range(ROW):
            self.board.append([])
            for col in range(COL):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece("white", row, col))
                    elif row > 4:
                        self.board[row].append(Piece("black", row, col))
                    else:
                        self.board[row].append(None)
                else:
                    self.board[row].append(None)

    def get_piece(self, row: int, col: int) -> Piece | None:
        return self.board[row][col]

    def move_piece(self, piece: Piece, row: int, col: int):
        self.board[piece.get_row()][piece.get_col()] = self.board[row][col]
        piece.set_row(row)
        piece.set_col(col)
        self.board[row][col] = piece

        piece.move(row, col)

        if row == 0 or row == ROW - 1:
            piece.make_king()

        if piece.get_color() == "white":
            self.white_kings += 1 if piece.get_king() else 0
            self.white_left -= 1
        else:
            self.black_kings += 1 if piece.get_king() else 0
            self.black_left -= 1

    def draw(self, win: pygame.Surface):
        self.draw_squares(win)
        for row in range(ROW):
            for col in range(COL):
                piece = self.board[row][col]
                if piece is not None:
                    piece.draw(win)
