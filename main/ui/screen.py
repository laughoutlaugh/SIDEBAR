import pygame

class Screen:
    WIDTH = 480
    HEIGHT = 320

    def __init__(self):
        self.surface = pygame.display.set_mode(
            (self.WIDTH, self.HEIGHT)
        )

        pygame.display.set_caption("SIDEBAR")

        self.clock = pygame.time.Clock()

    def update(self):
        self.surface.fill((20, 20, 20))