import pygame

class ListScreen:
    def __init__(self, screen, title, items):
        self.screen = screen
        self.title = title
        self.items = items

        self.selected = 0
        self.scroll_offset = 0

        self.font = pygame.font.Font(None, 28)
        self.title_font = pygame.font.Font(None, 36)

        # Layout

