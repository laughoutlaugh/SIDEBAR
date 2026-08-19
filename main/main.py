import pygame

WIDTH = 480
HEIGHT = 320

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("SIDEBAR")

clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((20, 20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()