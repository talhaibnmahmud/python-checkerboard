from pygame import color


ColorType = color.Color \
    | int \
    | str \
    | tuple[int, int, int] \
    | list[int] \

Coordinate = tuple[int, int]

WIDTH, HEIGHT = 720, 720
ROW, COL = 8, 8
SQUARE_SIZE = WIDTH // ROW

RED = color.Color(255, 0, 0)
BLUE = color.Color(0, 0, 255)
GREEN = color.Color(0, 255, 0)
YELLOW = color.Color(255, 255, 0)
BLACK = color.Color(0, 0, 0)
WHITE = color.Color(255, 255, 255)
