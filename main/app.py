import pygame

from ui.screen import Screen
from ui.main_menu import MainMenu
from ui.list_screen import ListScreen
from ui.now_playing import NowPlaying


class App:

    def __init__(self):
        pygame.init()

        self.screen = Screen()

        # -------------------------
        # Test music data
        # -------------------------

        self.songs = [
            "Song One",
            "Song Two",
            "Song Three",
            "Song Four",
            "Song Five",
            "Song Six",
            "Song Seven",
            "Song Eight",
            "Song Nine",
            "Song Ten",
            "Song Eleven",
            "Song Twelve",
        ]

        self.albums = [
            "Album One",
            "Album Two",
            "Album Three",
            "Album Four",
            "Album Five",
            "Album Six",
            "Album Seven",
        ]

        self.artists = [
            "Artist One",
            "Artist Two",
            "Artist Three",
            "Artist Four",
            "Artist Five",
            "Artist Six",
            "Artist Seven",
            "Artist Eight",
        ]

        # -------------------------
        # Screens
        # -------------------------

        self.main_menu = MainMenu(self.screen)

        self.song_list = ListScreen(
            self.screen,
            "Songs",
            self.songs
        )

        self.album_list = ListScreen(
            self.screen,
            "Albums",
            self.albums
        )

        self.artist_list = ListScreen(
            self.screen,
            "Artists",
            self.artists
        )

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

                selected = self.song_list.select()

                self.now_playing.set_song(
                    selected,
                    "Test Artist",
                    "Test Album"
                )

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

            if event.key == pygame.K_2:
                self.now_playing.toggle_play()

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
            self.now_playing.draw()