"""Main entry point for the application."""
import pygame

from checker import Game
from checker.constants import Coordinate, Dimensions


FPS = 60
SIZE = (Dimensions.WIDTH, Dimensions.HEIGHT)
WIN: pygame.Surface = pygame.display.set_mode(size=SIZE)  # type: ignore
pygame.display.set_caption("Checkers")


def get_row_col_from_mouse_pos(mouse_pos: tuple[float, float]) -> Coordinate:
    """ Get the row and column from the mouse position. """

    x, y = mouse_pos
    row = int(y // Dimensions.SQUARE_SIZE)
    col = int(x // Dimensions.SQUARE_SIZE)

    return row, col


def main():
    """ Main Function"""

    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                row, col = get_row_col_from_mouse_pos(event.pos)

                if pygame.mouse.get_pressed()[2]:
                    game.select_piece(row, col)
                if pygame.mouse.get_pressed()[0]:
                    game.move_piece(row, col)

        game.play()

    pygame.quit()


if __name__ == '__main__':
    main()
