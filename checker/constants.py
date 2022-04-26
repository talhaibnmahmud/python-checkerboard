import pygame


_RgbaOutput = tuple[int, int, int, int]
ColorType = pygame.Color \
    | int \
    | str \
    | tuple[int, int, int] \
    | list[int] \
    | _RgbaOutput

Coordinate = tuple[int, int]

WIDTH, HEIGHT = 720, 720
ROW, COL = 8, 8
SQUARE_SIZE = WIDTH // ROW

RED = pygame.Color(255, 0, 0)
BLUE = pygame.Color(0, 0, 255)
GREEN = pygame.Color(0, 255, 0)
YELLOW = pygame.Color(255, 255, 0)
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

CROWN = pygame.transform.scale(
    pygame.image.load('assets/crown.png'), (SQUARE_SIZE // 3, SQUARE_SIZE // 3)
)
