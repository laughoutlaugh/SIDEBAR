import pygame

from ui.screen import Screen
from ui.main_menu import MainMenu
from ui.list_screen import ListScreen
from ui.now_playing import NowPlaying
from player.mock_player import MockPlayer


class App:

    def __init__(self):
        pygame.init()

        self.screen = Screen()

        # -------------------------
        # Test music data
        # -------------------------

        self.songs = [
            {
                "title": "Song One",
                "artist": "Artist One",
                "album": "Album One",
            },
            {
                "title": "Song Two",
                "artist": "Artist One",
                "album": "Album One",
            },
            {
                "title": "Song Three",
                "artist": "Artist Two",
                "album": "Album Two",
            },
            {
                "title": "Song Four",
                "artist": "Artist Two",
                "album": "Album Two",
            },
            {
                "title": "Song Five",
                "artist": "Artist Three",
                "album": "Album Three",
            },
            {
                "title": "Song Six",
                "artist": "Artist Three",
                "album": "Album Three",
            },
        ]

        # -------------------------
        # Screens
        # -------------------------

        self.main_menu = MainMenu(self.screen)

        self.song_list = ListScreen(
            self.screen,
            "Songs",
            self.songs,
            "song"
        )

        self.album_list = ListScreen(
            self.screen,
            "Albums",
            self.songs,
            "album"
        )

        self.artist_list = ListScreen(
            self.screen,
            "Artists",
            self.songs,
            "artist"
        )

        self.player = MockPlayer(self.songs)

        self.now_playing = NowPlaying(self.screen)

        # Current screen
        self.current_screen = "main_menu"

    def run(self):

        running = True

        while running:

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False

                else:
                    self.handle_input(event)

            self.update()
            self.draw()
            pygame.display.flip()
            self.screen.clock.tick(60)

        pygame.quit()

    def handle_input(self, event):

        if event.type != pygame.KEYDOWN:
            return

        # -------------------------
        # MAIN MENU
        # -------------------------

        if self.current_screen == "main_menu":

            if event.key == pygame.K_UP:
                self.main_menu.move_up()

            elif event.key == pygame.K_DOWN:
                self.main_menu.move_down()

            elif event.key == pygame.K_RIGHT:

                selected = self.main_menu.select()

                if selected == "Songs":
                    self.current_screen = "songs"

                elif selected == "Albums":
                    self.current_screen = "albums"

                elif selected == "Artists":
                    self.current_screen = "artists"

                elif selected == "Settings":
                    print("Settings not implemented yet")

        # -------------------------
        # SONGS
        # -------------------------

        elif self.current_screen == "songs":

            if event.key == pygame.K_UP:
                self.song_list.move_up()

            elif event.key == pygame.K_DOWN:
                self.song_list.move_down()

            elif event.key == pygame.K_RIGHT:

                selected_index = self.song_list.selected

                self.player.current_index = selected_index
                self.player.position = 0

                song = self.player.current_song

                self.now_playing.set_song(
                    song["title"],
                    song["artist"],
                    song["album"]
                )

                self.player.play()

                self.current_screen = "now_playing"

            elif event.key == pygame.K_LEFT:
                self.current_screen = "main_menu"

        # -------------------------
        # ALBUMS
        # -------------------------

        elif self.current_screen == "albums":

            if event.key == pygame.K_UP:
                self.album_list.move_up()

            elif event.key == pygame.K_DOWN:
                self.album_list.move_down()

            elif event.key == pygame.K_RIGHT:
                print(
                    "Selected album:",
                    self.album_list.select()
                )

            elif event.key == pygame.K_LEFT:
                self.current_screen = "main_menu"

        # -------------------------
        # ARTISTS
        # -------------------------

        elif self.current_screen == "artists":

            if event.key == pygame.K_UP:
                self.artist_list.move_up()

            elif event.key == pygame.K_DOWN:
                self.artist_list.move_down()

            elif event.key == pygame.K_RIGHT:
                print(
                    "Selected artist:",
                    self.artist_list.select()
                )

            elif event.key == pygame.K_LEFT:
                self.current_screen = "main_menu"

        # -------------------------
        # NOW PLAYING
        # -------------------------

        elif self.current_screen == "now_playing":

            if event.key == pygame.K_1:
                self.player.previous()

            if event.key == pygame.K_2:
                self.player.toggle_play()

            if event.key == pygame.K_3:
                self.player.next()

            elif event.key == pygame.K_LEFT:
                self.current_screen = "songs"

    def draw(self):

        if self.current_screen == "main_menu":
            self.main_menu.draw()

        elif self.current_screen == "songs":
            self.song_list.draw()

        elif self.current_screen == "albums":
            self.album_list.draw()

        elif self.current_screen == "artists":
            self.artist_list.draw()

        elif self.current_screen == "now_playing":
            self.now_playing.draw(self.player)

    def update(self):
        self.player.update()

        if self.current_screen == "now_playing":
            self.now_playing.update_song(self.player)