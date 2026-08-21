import pygame
from pygame.sprite import collide_rect_ratio

from ui.screen import Screen
from ui.main_menu import MainMenu
from ui.list_screen import ListScreen


def main():
    pygame.init()
    screen = Screen()
    main_menu = MainMenu(screen)

    songs = [
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

    albums = [
        "Album One",
        "Album Two",
        "Album Three",
        "Album Four",
        "Album Five",
        "Album Six",
        "Album Seven",
    ]

    artists = [
        "Artist One",
        "Artist Two",
        "Artist Three",
        "Artist Four",
        "Artist Five",
        "Artist Six",
        "Artist Seven",
        "Artist Eight",
    ]

    song_list = ListScreen(screen, "Songs", songs)
    album_list = ListScreen(screen, "Albums", albums)
    artist_list = ListScreen(screen, "Artists", artists)

    current_screen = "main_menu"
    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                # --------------------------
                # MAIN MENU
                # --------------------------

                if current_screen == "main_menu":

                    if event.key == pygame.K_UP:
                        main_menu.move_up()

                    elif event.key == pygame.K_DOWN:
                        main_menu.move_down()

                    elif event.key == pygame.K_RIGHT:
                        selected = main_menu.select()

                        if selected == "Songs":
                            current_screen = "songs"
                        elif selected == "Albums":
                            current_screen = "albums"
                        elif selected == "Artists":
                            current_screen = "artists"
                        elif selected == "Settings":
                            print("Settings not implemented yet </3")

                # --------------------------
                # SONG LIST
                # --------------------------

                elif current_screen == "songs":

                    if event.key == pygame.K_UP:
                        song_list.move_up()
                    elif event.key == pygame.K_DOWN:
                        song_list.move_down()
                    elif event.key == pygame.K_RIGHT:
                        selected = song_list.select()
                        print("Selected song:", selected)

                # --------------------------
                # ALBUM LIST
                # --------------------------

                elif current_screen == "albums":

                    if event.key == pygame.K_UP:
                        album_list.move_up()
                    elif event.key == pygame.K_DOWN:
                        album_list.move_down()
                    elif event.key == pygame.K_RIGHT:
                        selected = album_list.select()
                        print("Selected album:", selected)

                # --------------------------
                # ARTIST LIST
                # --------------------------

                elif current_screen == "artists":

                    if event.key == pygame.K_UP:
                        artist_list.move_up()
                    elif event.key == pygame.K_DOWN:
                        artist_list.move_down()
                    elif event.key == pygame.K_RIGHT:
                        selected = artist_list.select()
                        print("Selected artist:", selected)

                # --------------------------
                # BACK
                # --------------------------

                if event.key == pygame.K_LEFT:
                    current_screen = "main_menu"

        # --------------------------
        # DRAW CURRENT SCREEN
        # --------------------------

        if current_screen == "main_menu":
            main_menu.draw()

        elif current_screen == "songs":
            song_list.draw()

        elif current_screen == "albums":
            album_list.draw()

        elif current_screen == "artists":
            artist_list.draw()

        pygame.display.flip()
        screen.clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()