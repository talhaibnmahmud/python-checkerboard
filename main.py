"""Main entry point for the application."""
import pygame

from checker import Board
from checker import WIDTH, HEIGHT


FPS = 60
SIZE = (WIDTH, HEIGHT)
WIN: pygame.Surface = pygame.display.set_mode(size=SIZE)  # type: ignore
pygame.display.set_caption("Checkers")


def main():
    """ Main Function"""
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        board.draw(WIN)
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
