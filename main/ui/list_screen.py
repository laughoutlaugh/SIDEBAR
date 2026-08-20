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
        self.list_x = 40
        self.list_y = 65
        self.list_width = 400

        self.item_height = 40
        self.item_spacing = 8

        self.visible_items = 5

    def draw(self):
        surface = self.screen.surface

        # Background
        surface.fill((20, 20, 20))

        # Title
        title = self.title_font.render(
            self.title,
            True,
            (255, 255, 255)
        )

        title_rect = title.get_rect(
            center=(240,30)
        )

        surface.blit(title, title_rect)

        # Draw visible items
        for i in range(self.visible_items):
            item_index = self.scroll_offset + i

            if item_index >= len(self.items):
                break

            item = self.items[item_index]

            x = self.list_x
            y = self.list_y + i * (
                self.item_height + self.item_spacing
            )

            # Highlight selected item
            if item_index == self.selected:
                background = (70, 70, 70)
            else:
                background = (35, 35, 35)

            pygame.draw.rect(
                surface,
                background,
                (
                    x,
                    y,
                    self.list_width,
                    self.item_height
                )
            )

            # Item text
            text = self.font.render(
                item,
                True,
                (255, 255, 255)
            )

            text_rect = text.get_rect(
                midleft=(x + 15, y + self.item_height // 2)
            )

            surface.blit(text, text_rect)

    def move_up(self):
        if self.selected > 0:
            self.selected -= 1

            # Scroll up if necessary
            if self.selected < self.scroll_offset:
                self.scroll_offset = self.selected

    def move_down(self):
        if self.selected < len(self.items) - 1:
            self.selected += 1

            # Scroll down if necessary
            if self.selected >= (
                self.scroll_offset + self.visible_items
            ):
                self.scroll_offset = (
                    self.selected - self.visible_items + 1
                )

    def select(self):
        return self.items[self.selected]