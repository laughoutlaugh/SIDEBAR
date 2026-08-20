'''
import pygame

from ui.screen import Screen
from ui.main_menu import MainMenu


def main():
    pygame.init()

    screen = Screen()
    menu = MainMenu(screen)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN: # On buttonpress
                if event.key == pygame.K_UP: # Up arrow
                    menu.move_up()
                elif event.key == pygame.K_DOWN: # Down arrow
                    menu.move_down()
                elif event.key == pygame.K_RIGHT: # Right arrow
                    selected = menu.select()
                    print("Selected:", selected)

        menu.draw()
        pygame.display.flip()
        screen.clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()

'''

# Testing list_screen class

import pygame

from ui.screen import Screen
from ui.list_screen import ListScreen


def main():
    pygame.init()

    screen = Screen()

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

    list_screen = ListScreen(
        screen,
        "Songs",
        songs
    )

    running = True

    while running:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_UP:
                    list_screen.move_up()

                elif event.key == pygame.K_DOWN:
                    list_screen.move_down()

                elif event.key == pygame.K_RIGHT:
                    selected = list_screen.select()
                    print("Selected:", selected)

        list_screen.draw()

        pygame.display.flip()

        screen.clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()