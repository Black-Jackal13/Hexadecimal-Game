import time

import pygame
import pygame_gui

from Game.counter import Counter
from Game.display.binary import Binary
from Game.display.hexadecimal import Hexadecimal
from Game.tools import binary_to_hexadecimal, hexadecimal_to_binary

# Initialize Pygame
pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

# Create Window
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hexadecimal Game")
background = pygame.Surface((WIDTH, HEIGHT))
background.fill(pygame.Color('#000000'))

# Initialize Pygame GUI
manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# Create Counter
counter = Counter()

# Colours
RED = pygame.Color('red')
GRAY = pygame.Color(211, 211, 211)
TEXT_COLOUR = pygame.Color('white')

# Create Objects
binary_obj = Binary(WIDTH, HEIGHT, RED, GRAY)
text_obj = Hexadecimal(WIDTH, HEIGHT, TEXT_COLOUR)


def counting():
    """
    Executes a counting sequene in both Binary and the respective Hexadecimal value.

    :raises pygame.error: Raised in case of any issues caused by Pygame -
        such as improper initialisation or issues during screen update.

    :return: None
    """
    counter.reset()
    text_obj.letters = "00"
    running = True

    while running:
        time_delta = clock.tick(60) / 1000.0
        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # Escape Key
                if event.key == pygame.K_ESCAPE:
                    running = False

            manager.process_events(event)

        manager.update(time_delta)

        screen.blit(background, (0, 0))

        # Get and Increment Binary Counter
        binary = counter.get_binary()
        counter.increment()

        # Drawe Letters
        text_obj.letters = binary_to_hexadecimal(binary)
        text_obj.draw_hexadecimal(screen)

        # Draw Binary
        binary_obj.sequence = binary
        binary_obj.draw_binary(screen, 500)

        # Update Display
        manager.draw_ui(screen)
        pygame.display.update()
        pygame.time.delay(250)

    pygame.quit()


def translate_binary_to_hexadecimal():
    goal = counter.random()
    binary_obj.sequence = goal

    guess = ""

    valid_keys = [
        pygame.K_0,
        pygame.K_1,
        pygame.K_2,
        pygame.K_3,
        pygame.K_4,
        pygame.K_5,
        pygame.K_6,
        pygame.K_7,
        pygame.K_8,
        pygame.K_9,
        pygame.K_a,
        pygame.K_b,
        pygame.K_c,
        pygame.K_d,
        pygame.K_e,
        pygame.K_f,
    ]

    running = True

    while running:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                running = False

            # Key POresss
            if event.type == pygame.KEYDOWN:

                # Escape Key (Quit)
                if event.key == pygame.K_ESCAPE:
                    running = False

                # Enter Key (Submit if valid guess)
                if event.key == pygame.K_RETURN and len(guess) == 2:
                    if hexadecimal_to_binary(guess) == goal:
                        correct = pygame.font.Font(None, 160).render("Correct", False, pygame.Color('green'))
                        screen.blit(correct, (10, 10))

                        # Update Display
                        manager.draw_ui(screen)
                        pygame.display.update()

                        time.sleep(3)
                        return

                    else:
                        incorrect = pygame.font.Font(None, 160).render("Sorry, Nope", False, pygame.Color('red'))
                        screen.blit(incorrect, (10, 10))

                        # Update Display
                        manager.draw_ui(screen)
                        pygame.display.update()

                        time.sleep(3)

                # Backspace Key (Remove Last Character if character available)
                elif event.key == pygame.K_BACKSPACE and len(guess) > 0:
                    guess = guess[:-1]

                # Hexadecimal Key (Append Guess if character available)
                elif event.key in valid_keys and len(guess) < 2:
                    if event.key == pygame.K_0:
                        guess += "0"
                    elif event.key == pygame.K_1:
                        guess += "1"
                    elif event.key == pygame.K_2:
                        guess += "2"
                    elif event.key == pygame.K_3:
                        guess += "3"
                    elif event.key == pygame.K_4:
                        guess += "4"
                    elif event.key == pygame.K_5:
                        guess += "5"
                    elif event.key == pygame.K_6:
                        guess += "6"
                    elif event.key == pygame.K_7:
                        guess += "7"
                    elif event.key == pygame.K_8:
                        guess += "8"
                    elif event.key == pygame.K_9:
                        guess += "9"
                    elif event.key == pygame.K_a:
                        guess += "A"
                    elif event.key == pygame.K_b:
                        guess += "B"
                    elif event.key == pygame.K_c:
                        guess += "C"
                    elif event.key == pygame.K_d:
                        guess += "D"
                    elif event.key == pygame.K_e:
                        guess += "E"
                    elif event.key == pygame.K_f:
                        guess += "F"

            manager.process_events(event)

        manager.update(time_delta)

        screen.blit(background, (0, 0))

        # Draw Letters
        text_obj.letters = guess
        text_obj.draw_hexadecimal(screen)

        # Draw Binary
        binary_obj.sequence = goal
        binary_obj.draw_binary(screen, 500)

        # Update Display
        manager.draw_ui(screen)
        pygame.display.update()

    pygame.quit()


def translate_hexadecimal_to_binary():
    values = "00000000"
    goal = counter.random()
    text_obj.letters = binary_to_hexadecimal(goal)

    valid_keys = [
        pygame.K_0,
        pygame.K_1,
        pygame.K_2,
        pygame.K_3,
        pygame.K_4,
        pygame.K_5,
        pygame.K_6,
        pygame.K_7,
        pygame.K_8,
    ]

    running = True

    while running:
        time_delta = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            # Quit Game
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                # Escape Key (Quit)
                if event.key == pygame.K_ESCAPE:
                    running = False

                # Enter Key (Submit)
                if event.key == pygame.K_RETURN:
                    # TODO: Submission Logic
                    print(values)
                    if values == goal:
                        correct = pygame.font.Font(None, 160).render("Correct", False, pygame.Color('green'))
                        screen.blit(correct, (10, 10))

                        # Update Display
                        manager.draw_ui(screen)
                        pygame.display.update()

                        time.sleep(3)
                        return

                    else:
                        incorrect = pygame.font.Font(None, 160).render("Sorry, Nope", False, pygame.Color('red'))
                        screen.blit(incorrect, (10, 10))

                        # Update Display
                        manager.draw_ui(screen)
                        pygame.display.update()

                        time.sleep(3)

                # Binary Unit (Toggle Values)
                elif event.key in valid_keys:
                    if event.key == pygame.K_1:
                        values = ("1" if values[0] == "0" else "0") + values[1:]
                    elif event.key == pygame.K_2:
                        values = values[:1] + ("1" if values[1] == "0" else "0") + values[2:]
                    elif event.key == pygame.K_3:
                        values = values[:2] + ("1" if values[2] == "0" else "0") + values[3:]
                    elif event.key == pygame.K_4:
                        values = values[:3] + ("1" if values[3] == "0" else "0") + values[4:]
                    elif event.key == pygame.K_5:
                        values = values[:4] + ("1" if values[4] == "0" else "0") + values[5:]
                    elif event.key == pygame.K_6:
                        values = values[:5] + ("1" if values[5] == "0" else "0") + values[6:]
                    elif event.key == pygame.K_7:
                        values = values[:6] + ("1" if values[6] == "0" else "0") + values[7:]
                    elif event.key == pygame.K_8:
                        values = values[:7] + ("1" if values[7] == "0" else "0")

                manager.process_events(event)

            manager.update(time_delta)

            screen.blit(background, (0, 0))

        # Show Goal
        text_obj.draw_hexadecimal(screen)

        # Show Binary
        binary_obj.sequence = values
        binary_obj.draw_binary(screen, 500)

        manager.draw_ui(screen)

        pygame.display.update()

    pygame.quit()
