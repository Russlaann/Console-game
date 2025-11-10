import pygame

pygame.init()

w, h = 1, 1
high = width = 100

sc = pygame.display.set_mode((1100, 900))
pygame.display.set_caption("Шрифты")

clock = pygame.time.Clock()
FPS = 520

WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (239, 228, 0)
BLUE = (0,0,150)
GREEN = (0, 255, 0)


while True:
    sc.fill(BLUE)
    pygame.draw.circle(sc, YELLOW, (w, h), 20)
    if h < 1100:
        w += 1
        h += 1
    if h >= 1100:
        w += 1
        h -= 1

    pygame.display.update()
    clock.tick(FPS)