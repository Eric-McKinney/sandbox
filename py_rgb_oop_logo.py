import pygame
import rgb_oop
from time import sleep

WIDTH, HEIGHT = 512, 512
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Logo rgb")
WHITE = (255, 255, 255)


def draw_logo(color):
    WIN.fill(WHITE)

    # Cringe part of bottom snake that needs to be below top snake
    pygame.draw.rect(WIN, color, rect=(326, 194, 66, 66))
    pygame.draw.circle(WIN, WHITE, center=(322, 189), radius=71)

    # Top snake
    pygame.draw.ellipse(WIN, color, rect=(135, 2, 242, 112))
    pygame.draw.rect(WIN, color, rect=(135, 63, 242, 52))
    pygame.draw.rect(WIN, color, rect=(256, 115, 121, 76))
    pygame.draw.circle(WIN, color, center=(323, 192), radius=54)
    pygame.draw.rect(WIN, color, rect=(86, 131, 237, 115))
    pygame.draw.ellipse(WIN, color, rect=(6, 131, 139, 245))
    pygame.draw.rect(WIN, color, rect=(82, 131, 38, 245))
    pygame.draw.rect(WIN, color, rect=(121, 246, 63, 64))
    pygame.draw.circle(WIN, WHITE, center=(184, 311), radius=64)
    pygame.draw.rect(WIN, WHITE, rect=(120, 314, 10, 40))

    # Bottom snake
    pygame.draw.rect(WIN, color, rect=(392, 131, 52, 245))
    pygame.draw.ellipse(WIN, color, rect=(392, 131, 115, 245))
    pygame.draw.rect(WIN, color, rect=(190, 259, 255, 117))
    pygame.draw.circle(WIN, color, center=(189, 315), radius=56)
    pygame.draw.rect(WIN, color, rect=(133, 317, 123, 126))
    pygame.draw.rect(WIN, color, rect=(256, 393, 121, 50))
    pygame.draw.ellipse(WIN, color, rect=(133, 376, 244, 132))
    pygame.draw.rect(WIN, WHITE, rect=(257, 376, 80, 17))

    # "Eyes" of the two snakes
    pygame.draw.circle(WIN, WHITE, center=(188, 61), radius=22.5)
    pygame.draw.circle(WIN, WHITE, center=(324, 445), radius=22.5)

    pygame.display.update()


def main():
    rgb = rgb_oop.RGB()
    cycle = 0
    draw_logo(rgb.get_rgb())
    run = True

    while run:
        rgb.increment_rgb()
        rgb.update_cycle()
        draw_logo(rgb.get_rgb())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        sleep(rgb.DELAY)

    pygame.quit()


if __name__ == "__main__":
    main()
