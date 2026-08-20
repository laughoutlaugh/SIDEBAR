import pygame


class MainMenu:
    def __init__(self, screen):
        self.screen = screen

        self.options = [
            "Songs",
            "Albums",
            "Artists",
            "Settings"
        ]

        self.selected = 0

        self.font = pygame.font.Font(None, 23)

    def draw(self):
        surface = self.screen.surface

        # Background
        surface.fill((20, 20, 20))

        # Menu Options
        start_y = 50
        box_width = 300
        box_height = 45
        spacing = 10

        for i, option in enumerate(self.options):

            x = (480 - box_width) // 2
            y = start_y + i * (box_height + spacing)

            # Selected Option
            if i == self.selected:
                background = (70, 70, 70)
            else:
                background = (35, 35, 35)

            pygame.draw.rect(
                surface,
                background,
                (x, y ,box_width, box_height)
            )

            # Text
            text = self.font.render(
                option,
                True,
                (255, 255, 255)
            )

            text_rect = text.get_rect(
                center=(240, y + box_height // 2)
            )

            surface.blit(text, text_rect)

    def move_up(self):
        self.selected -= 1

        if self.selected < 0:
            self.selected = len(self.options) - 1

    def move_down(self):
        self.selected += 1

        if self.selected >= len(self.options):
            self.selected = 0

    def select(self):
        return self.options[self.selected]