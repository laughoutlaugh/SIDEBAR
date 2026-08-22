import pygame

class NowPlaying:
    def __init__(self, screen):
        self.screen = screen

        self.title_font = pygame.font.Font(None, 32)
        self.artist_font = pygame.font.Font(None, 26)
        self.small_font = pygame.font.Font(None, 22)

        self.song = None
        self.artist = None
        self.album = None

        self.playing = False

    def set_song(self, song, artist="Unknown Artist", album="Unknown Album"):
        self.song = song
        self.artist = artist
        self.album = album
        self.playing = True

    def draw(self):
        surface = self.screen.surface
        surface.fill((20, 20, 20))

        # Header
        header = self.title_font.render(
            "Now Playing",
            True,
            (255, 255, 255)
        )

        header_rect = header.get_rect(
            center=(240, 25)
        )

        surface.blit(header, header_rect)

        # Album art placeholder
        album_art = pygame.Rect(
            140,
            50,
            200,
            150
        )

        pygame.draw.rect(
            surface,
            (50, 50, 50),
            album_art
        )

        # Album art text
        art_text = self.title_font.render(
            "ALBUM ART",
            True,
            (150, 150, 150)
        )

        art_rect = art_text.get_rect(
            center=album_art.center
        )

        surface.blit(art_text, art_rect)

        # Song information
        if self.song:

            song_text = self.title_font.render(
                self.song,
                True,
                (255, 255, 255)
            )

            song_rect = song_text.get_rect(
                center=(240, 220)
            )

            surface.blit(song_text, song_rect)

            artist_text = self.artist_font.render(
                self.artist,
                True,
                (180, 180, 180)
            )

            artist_rect = artist_text.get_rect(
                center=(240, 245)
            )

            surface.blit(artist_text, artist_rect)

        # Progress bar
        bar_x = 40
        bar_y = 270
        bar_width = 400
        bar_height = 5

        pygame.draw.rect(
            surface,
            (70, 70, 70),
            (bar_x, bar_y, bar_width, bar_height)
        )

        # Playback controls
        if self.playing:
            control_text = "◀     II     ▶"
        else:
            control_text = "◀     ▶     ▶"

        controls = self.title_font.render(
            control_text,
            True,
            (255, 255, 255)
        )

        controls_rect = controls.get_rect(
            center=(240, 300)
        )

        surface.blit(controls, controls_rect)

    def toggle_play(self):
        self.playing = not self.playing

    def update_song(self, player):
        song = player.current_song

        self.song = song["title"]
        self.artist = song["artist"]
        self.album = song["album"]
        self.playing = player.playing