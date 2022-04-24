"""Main entry point for the application."""
import pygame

from checker import HEIGHT, WIDTH, SQUARE_SIZE,  Board


FPS = 60
SIZE = (WIDTH, HEIGHT)
WIN: pygame.Surface = pygame.display.set_mode(size=SIZE)  # type: ignore
pygame.display.set_caption("Checkers")


def get_row_col_from_mouse_pos(mouse_pos: tuple[float, float]) -> tuple[int, int]:
    x, y = mouse_pos
    row = int(y // SQUARE_SIZE)
    col = int(x // SQUARE_SIZE)

    return row, col


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
            if event.type == pygame.MOUSEBUTTONDOWN:
                row, col = get_row_col_from_mouse_pos(event.pos)
                piece = board.get_piece(row, col)
                print(piece)

        board.draw(WIN)
        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
