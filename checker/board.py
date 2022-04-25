import pygame

from .constants import COL, ROW, SQUARE_SIZE, ColorType
from .piece import Piece


class Board:
    def __init__(self):
        self.selected_piece = None
        self.black_left = self.white_left = 12
        self.black_kings = self.white_kings = 0
        self.valid_moves: list[tuple[int, int]] = []

        self.create_board()

    def set_valid_moves(self, valid_moves: list[tuple[int, int]]):
        self.valid_moves = valid_moves

    def draw_squares(self, win: pygame.Surface):
        win.fill('#808000')
        for row in range(ROW):
            for col in range(row % 2, COL, 2):
                pygame.draw.rect(
                    win,
                    (218, 160, 109),
                    (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                )

    def _draw_circle_alpha(self, win: pygame.Surface, center: tuple[int, int], radius: int, color: tuple[int, int, int, int]):
        target_rect = pygame.Rect(center, (0, 0)).inflate(
            radius * 2, radius * 2)
        shape_surface = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.circle(shape_surface, color, (radius, radius), radius)
        win.blit(shape_surface, target_rect)

    def draw_valid_moves(self, win: pygame.Surface, valid_moves: list[tuple[int, int]]):
        for row, col in valid_moves:
            x = col * SQUARE_SIZE + (SQUARE_SIZE // 2)
            y = row * SQUARE_SIZE + (SQUARE_SIZE // 2)
            pygame.draw.circle(win, (0, 200, 0), (x, y), 15)

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

    def get_valid_moves(self, piece: Piece):
        valid_moves: list[tuple[int, int]] = []

        if piece.get_color() == "white":
            direction = 1
            moves = self.adjacent_move(piece, direction)
            valid_moves.extend(moves)
        else:
            direction = -1
            moves = self.adjacent_move(piece, direction)
            valid_moves.extend(moves)

        if piece.get_king() and piece.get_color() == "white":
            top = self.adjacent_move(piece, direction=-1)

            valid_moves.extend(top)
        if piece.get_king() and piece.get_color() == "black":
            bottom = self.adjacent_move(piece, direction=1)
            valid_moves.extend(bottom)

        return valid_moves

    def adjacent_move(self, piece: Piece, direction: int):
        valid: list[tuple[int, int]] = []
        row, col = piece.get_row(), piece.get_col()

        if (direction == 1 and row == 7) or (direction == -1 and row == 0):
            return valid

        if col == 0:
            if self._check_adjacent(row + direction, col + 1) is not None:
                valid.append((row + direction, col + 1))
        elif col == 7:
            if self._check_adjacent(row + direction, col - 1) is not None:
                valid.append((row + direction, col - 1))
        else:
            if self._check_adjacent(row + direction, col + 1) is not None:
                valid.append((row + direction, col + 1))
            if self._check_adjacent(row + direction, col - 1) is not None:
                valid.append((row + direction, col - 1))

        return valid

    def _check_adjacent(self, row: int, col: int):
        if self.board[row][col] is None:
            return row, col
        return None

    def _traverse_left(self, row: int, col: int, color: ColorType):
        valid: list[tuple[int, int]] = []
        x, y = col, row

        x_direction = 1
        y_direction = 1 if color == "white" else -1

        while -1 < x < 8 and -1 < y < 8:
            cell = self.board[y][x]

            if cell is not None and cell.color == color:
                break
            if cell is not None and cell.color != color:
                x -= x_direction
                y += y_direction
                continue

            if cell is None:
                valid.append((y, x))

            x -= x_direction
            y += y_direction

        return valid

    def _traverse_right(self, row: int, col: int, color: ColorType):
        valid: list[tuple[int, int]] = []
        x, y = col, row

        x_direction = 1
        y_direction = 1 if color == "white" else -1

        while -1 < x < 8 and -1 < y < 8:
            cell = self.board[y][x]

            if cell is not None and cell.color == color:
                break
            if cell is not None and cell.color != color:
                x += x_direction
                y += y_direction
                continue

            if cell is None:
                valid.append((y, x))

            x += x_direction
            y += y_direction

        return valid

    def move_piece(self, piece: Piece, row: int, col: int):
        self.board[piece.get_row()][piece.get_col()] = self.board[row][col]
        piece.set_row(row)
        piece.set_col(col)
        self.board[row][col] = piece

        piece.move(row, col)

        if (row == 0 or row == ROW - 1) and not piece.get_king():
            piece.make_king()

            if piece.get_color() == "white":
                self.white_kings += 1 if piece.get_king() else 0
            else:
                self.black_kings += 1 if piece.get_king() else 0

    def check_winner(self):
        if self.black_left == 0:
            return "white"
        elif self.white_left == 0:
            return "black"
        else:
            return None

    def draw(self, win: pygame.Surface):
        self.draw_squares(win)
        self.draw_valid_moves(win, self.valid_moves)

        for row in range(ROW):
            for col in range(COL):
                piece = self.board[row][col]
                if piece is not None:
                    piece.draw(win)
