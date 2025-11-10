import pygame

pygame.init()

W = 900
H = 600

pygame.display.set_caption("События от клавиатуры")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

FPS = 120  # число кадров в секунду
clock = pygame.time.Clock()


sc = pygame.display.set_mode((W, H))
sc.fill(BLACK)
pygame.display.update()
x=y=100
pygame.mouse.set_visible(False)
while 1:

    surf = pygame.Surface((200, 200))
    surf.fill(RED)
    pygame.draw.circle(surf, GREEN, (100, 100), 80)

    surf_alpha = pygame.Surface((W, 200))
    pygame.draw.rect(surf_alpha, BLUE, (0, 0, W, 100))
    surf_alpha.set_alpha(128)

    surf_beta = pygame.Surface((20, 20))
    surf_beta.fill(BLUE)

    surf.blit(surf_alpha, (0, 50))
    sc.blit(surf, (50, 50))
    sc.blit(surf_beta, (x, y))
    pygame.display.update()

    clock.tick(FPS)