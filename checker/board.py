import pygame

from .constants import ROW, COL, SQUARE_SIZE
from .piece import Piece


class Board:
    def __init__(self):
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0

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
        self.board: list[list[Piece | int]] = []
        for row in range(ROW):
            self.board.append([])
            for col in range(COL):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece("white", row, col))
                    elif row > 4:
                        self.board[row].append(Piece("black", row, col))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win: pygame.Surface):
        self.draw_squares(win)
        for row in range(ROW):
            for col in range(COL):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)  # type: ignore
