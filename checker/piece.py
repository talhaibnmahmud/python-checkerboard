import pygame

from .constants import CROWN, SQUARE_SIZE, ColorType


class Piece:
    def __init__(self, color: ColorType, row: int, col: int):
        self.color = color
        self.row = row
        self.col = col
        self.king = False

        self.x: int = 0
        self.y: int = 0
        self.calculate_positions()

    def __str__(self) -> str:
        return str(self.color) + " " + str(self.row) + " " + str(self.col) + " " + str(self.king)

    def __repr__(self) -> str:
        return str(self.color) + " " + str(self.row) + " " + str(self.col) + " " + str(self.king)

    def get_color(self) -> ColorType:
        return self.color

    def get_row(self) -> int:
        return self.row

    def get_col(self) -> int:
        return self.col

    def get_king(self):
        return self.king

    # def set_king(self, king) -> None:
    #     self.king = king

    def make_king(self):
        self.king = True

    def set_row(self, row: int) -> None:
        self.row = row

    def set_col(self, col: int) -> None:
        self.col = col

    def set_color(self, color: ColorType) -> None:
        self.color = color

    def calculate_positions(self):
        self.x = self.col * SQUARE_SIZE + (SQUARE_SIZE // 2)
        self.y = self.row * SQUARE_SIZE + (SQUARE_SIZE // 2)

    def move(self, row: int, col: int):
        self.row = row
        self.col = col
        self.calculate_positions()

    def draw(self, win: pygame.Surface):
        pygame.draw.circle(win, self.color, (self.x, self.y), 20)

        if self.king:
            win.blit(
                CROWN,
                (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2)
            )
