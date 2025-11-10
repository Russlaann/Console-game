import pygame

pygame.init()

W = 600
H = 400

sc = pygame.display.set_mode((W, H))
pygame.display.set_caption("Класс Rect")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

FPS = 60  # число кадров в секунду
clock = pygame.time.Clock()

hero = pygame.Surface((40, 50))
hero.fill(BLUE)
rect = hero.get_rect(centerx = W//2, centery = H//2)
print(rect)
print(rect.bottom)
print(rect.top)
print(rect.right)

sc.fill(WHITE)
sc.blit(hero, rect)
pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    clock.tick(FPS)