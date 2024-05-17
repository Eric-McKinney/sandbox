import pygame
from time import sleep

WIDTH, HEIGHT = 1300, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("rgb")
DELAY = 0.0035


def change_color(color):
    WIN.fill(color)
    pygame.display.update()


def change_rgb(color, increase):
    if increase and color < 255:
        color += 1
    elif not increase and color > 0:
        color -= 1

    return color


def update_cycle(rgb, cycle):
    if rgb == (255, 0, 0):
        cycle = 1
    elif rgb == (255, 255, 0):
        cycle = 2
    elif rgb == (0, 255, 0):
        cycle = 3
    elif rgb == (0, 255, 255):
        cycle = 4
    elif rgb == (0, 0, 255):
        cycle = 5
    elif rgb == (255, 0, 255):
        cycle = 6

    return cycle


def cycle_rgb(r, g, b, cycle):
    order = [
        # color, increase?
        (r, True),
        (g, True),
        (r, False),
        (b, True),
        (g, False),
        (r, True),
        (b, False)
    ]

    current_cycle = order[cycle]
    color = current_cycle[0]
    increase = current_cycle[1]

    color = change_rgb(color, increase)

    if cycle in [0, 2, 5]:
        r = color
    elif cycle in [1, 4]:
        g = color
    elif cycle in [3, 6]:
        b = color

    cycle = update_cycle((r, g, b), cycle)

    return r, g, b, cycle


def main():
    r, g, b = 0, 0, 0
    change_color((r, g, b))
    run = True
    cycle = 0

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        r, g, b, cycle = cycle_rgb(r, g, b, cycle)
        change_color((r, g, b))
        sleep(DELAY)

    pygame.quit()


if __name__ == "__main__":
    main()
