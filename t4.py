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
rect = hero.get_rect(topleft=(110, 210))
print(rect.top)

sc.fill(WHITE)

pygame.display.update()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rect.move_ip(400, 150)
                sc.blit(hero, rect)
                print(event)


    pygame.display.update()


    clock.tick(FPS)