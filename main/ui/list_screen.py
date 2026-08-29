import pygame


class ListScreen:
    def __init__(self, screen, title, items, item_type="default"):
        self.screen = screen
        self.title = title
        self.items = items
        self.item_type = item_type

        self.selected = 0
        self.scroll_offset = 0

        self.font = pygame.font.Font(None, 26)
        self.title_font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 20)

        # Layout
        self.list_x = 30
        self.list_y = 60
        self.list_width = 420

        self.item_height = 48
        self.item_spacing = 6

        self.visible_items = 4

    def draw(self):
        surface = self.screen.surface

        surface.fill((20, 20, 20))

        # -------------------------
        # Title
        # -------------------------

        title = self.title_font.render(
            self.title,
            True,
            (255, 255, 255)
        )

        title_rect = title.get_rect(
            center=(240, 25)
        )

        surface.blit(title, title_rect)

        # -------------------------
        # List
        # -------------------------

        for visible_index in range(self.visible_items):

            item_index = self.scroll_offset + visible_index

            if item_index >= len(self.items):
                break

            item = self.items[item_index]

            x = self.list_x
            y = self.list_y + visible_index * (
                self.item_height + self.item_spacing
            )

            # Background
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

            # Selection arrow
            if item_index == self.selected:

                arrow = self.font.render(
                    ">",
                    True,
                    (255, 255, 255)
                )

                surface.blit(
                    arrow,
                    (x + 8, y + 10)
                )

            # Item content
            if self.item_type == "song":
                self.draw_song(surface, item, x, y)

            elif self.item_type == "album":
                self.draw_album(surface, item, x, y)

            elif self.item_type == "artist":
                self.draw_artist(surface, item, x, y)

            else:
                self.draw_default(surface, item, x, y)

        # Scroll bar
        self.draw_scroll_indicator(surface)

    # -------------------------
    # SONG
    # -------------------------

    def draw_song(self, surface, item, x, y):

        title = self.font.render(
            item["title"],
            True,
            (255, 255, 255)
        )

        artist = self.small_font.render(
            item["artist"],
            True,
            (170, 170, 170)
        )

        surface.blit(
            title,
            (x + 35, y + 5)
        )

        surface.blit(
            artist,
            (x + 35, y + 27)
        )

    # -------------------------
    # ALBUM
    # -------------------------

    def draw_album(self, surface, item, x, y):

        album = self.font.render(
            item["album"],
            True,
            (255, 255, 255)
        )

        artist = self.small_font.render(
            item["artist"],
            True,
            (170, 170, 170)
        )

        surface.blit(
            album,
            (x + 35, y + 5)
        )

        surface.blit(
            artist,
            (x + 35, y + 27)
        )

    # -------------------------
    # ARTIST
    # -------------------------

    def draw_artist(self, surface, item, x, y):

        artist = self.font.render(
            item["artist"],
            True,
            (255, 255, 255)
        )

        surface.blit(
            artist,
            (x + 35, y + 14)
        )

    # -------------------------
    # DEFAULT
    # -------------------------

    def draw_default(self, surface, item, x, y):

        text = self.font.render(
            str(item),
            True,
            (255, 255, 255)
        )

        surface.blit(
            text,
            (x + 35, y + 14)
        )

    # -------------------------
    # SCROLL BAR
    # -------------------------

    def draw_scroll_indicator(self, surface):

        if len(self.items) <= self.visible_items:
            return

        track_x = 465
        track_y = self.list_y

        track_height = (
            self.visible_items *
            self.item_height
            +
            (self.visible_items - 1) *
            self.item_spacing
        )

        # Track
        pygame.draw.rect(
            surface,
            (50, 50, 50),
            (
                track_x,
                track_y,
                5,
                track_height
            )
        )

        # Thumb size
        ratio = self.visible_items / len(self.items)

        thumb_height = max(
            15,
            int(track_height * ratio)
        )

        # How far can we scroll?
        max_scroll = max(
            1,
            len(self.items) - self.visible_items
        )

        scroll_ratio = (
            self.scroll_offset / max_scroll
        )

        # Thumb position
        thumb_y = (
            track_y
            +
            int(
                (track_height - thumb_height)
                * scroll_ratio
            )
        )

        pygame.draw.rect(
            surface,
            (150, 150, 150),
            (
                track_x,
                thumb_y,
                5,
                thumb_height
            )
        )

    # -------------------------
    # NAVIGATION
    # -------------------------

    def move_up(self):

        if self.selected > 0:

            self.selected -= 1

            if self.selected < self.scroll_offset:
                self.scroll_offset = self.selected

    def move_down(self):

        if self.selected < len(self.items) - 1:

            self.selected += 1

            if self.selected >= (
                self.scroll_offset +
                self.visible_items
            ):
                self.scroll_offset = (
                    self.selected -
                    self.visible_items +
                    1
                )

    def select(self):

        return self.items[self.selected]

    def reset(self):

        self.selected = 0
        self.scroll_offset = 0