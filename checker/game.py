""" Game Class """
import pygame

from .board import Board


class Game:
    """ Game class """

    def __init__(self, window: pygame.Surface):
        """ Initialize the game """

        self.window = window
        self.player1 = "white"
        self.player2 = "black"

        self._reset()

    def play(self):
        """ Play the game """

        self.board.draw(self.window)
        pygame.display.update()

    def switch_player(self):
        """ Switch the current player """

        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def select_piece(self, row: int, col: int):
        """ Select a piece """

        piece = self.board.get_piece(row, col)
        if piece is None:
            return

        if piece.get_color() == self.current_player:
            self.selected_piece = piece
            self.valid_moves = self.board.get_valid_moves(piece)

            self.board.set_valid_moves(self.valid_moves)
            self.refresh()
        else:
            self.selected_piece = None
            self.valid_moves = []
            self.board.set_valid_moves(self.valid_moves)
            self.refresh()

    def move_piece(self, row: int, col: int):
        """ Move a piece """

        if self.selected_piece is None:
            return

        if (row, col) in self.valid_moves:
            self.board.move_piece(self.selected_piece, row, col)
            self.selected_piece = None
            self.valid_moves = []
            self.board.set_valid_moves(self.valid_moves)
            self.switch_player()
            self.winner = self.board.check_winner()

            self.refresh()
        else:
            self.selected_piece = None
            self.valid_moves = []
            self.board.set_valid_moves(self.valid_moves)
            self.refresh()

    def refresh(self):
        """ Refresh the game window """

        self.board.draw(self.window)
        pygame.display.update()

    def reset(self):
        """ Reset the game """

        self._reset()

    def _reset(self):
        self.board = Board()
        self.current_player = "white"
        self.selected_piece = None
        self.valid_moves = []
        self.winner = None
