# Simple pygame program

# Import and initialize the pygame library
import pygame
import numpy as np
from colour import Color
from pygame.locals import (
    K_SPACE,
    KEYDOWN,
    QUIT,
)


def color_tuple(color):
    return int(color.rgb[0] * 255), int(color.rgb[1] * 255), int(color.rgb[2] * 255)


pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 900
GAME_WIDTH = 300
GAME_HEIGHT = 300
# initial height of the sandpile
PILE_HEIGHT = 50000

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game_surface = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
screen_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

font = pygame.font.Font('freesansbold.ttf', 15)
text = font.render('Press Space To Start', True, color_tuple(Color('green')), color_tuple(Color('blue')))
textRect = text.get_rect()
textRect.center = (GAME_WIDTH // 2, GAME_HEIGHT // 2)
COLOR = 3000000

sandpile = np.zeros((GAME_WIDTH, GAME_HEIGHT))
sandpile[GAME_WIDTH // 2][GAME_HEIGHT // 2] += 4 * PILE_HEIGHT * COLOR


def pile(field):
    top = COLOR * 4
    if np.max(field) >= top:
        # find the largest piles
        high = field >= top

        # decrease high piles by top
        field[high] -= top
        if sandpile[(299, GAME_WIDTH//2)] > 2:
            return False
        right = (np.where(high)[0] + 1, np.where(high)[1])
        left = (np.where(high)[0] - 1, np.where(high)[1])
        up = (np.where(high)[0], np.where(high)[1] + 1)
        down = (np.where(high)[0], np.where(high)[1] - 1)

        field[right] += top / 4
        field[left] += top / 4
        field[up] += top / 4
        field[down] += top / 4
    return True


clock = pygame.time.Clock()
# Run until the user asks to quit
running = True
started = False
paused = False
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if not started:
                    started = True
                elif started and not paused:
                    paused = True
                elif started and paused:
                    paused = False
    if not started:
        game_surface.fill(color_tuple(Color('white')))
        game_surface.blit(text, textRect)
        pygame.display.update()
    elif started and not paused:
        calls = 0
        if not pile(sandpile):
            paused = True
        # pile_image = [[COLORS[int(i)] for i in row] for row in sandpile]
        pile_image = sandpile
        pygame.surfarray.blit_array(game_surface, pile_image)
        pygame.display.flip()
    elif paused:
        pile_image = sandpile
        pygame.surfarray.blit_array(game_surface, pile_image)

    pygame.transform.scale(game_surface, (SCREEN_WIDTH, SCREEN_HEIGHT), screen_surface)
    screen.blit(screen_surface, (0, 0))

# Done! Time to quit.
pygame.quit()
