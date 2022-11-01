# Create Pygame ins
import pygame
import sys
import os
from pygame.locals import *

pygame.init()
# Make game full screen
pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Duck In Space")
pygame.display.update()

font_normal = pygame.font.Font(
    os.path.join(
        "assets",
        "fonts",
        "ethnocentric.ttf"),
    20)
font_italic = pygame.font.Font(
    os.path.join(
        "assets",
        "fonts",
        "ethnocentric_it.ttf"),
    20)


def main():
    # Keep the game open until the user closes it
    while True:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # Draw the text
        pygame.display.get_surface().blit(font_normal.render(
            "Hello World", True, (255, 255, 255)), (100, 100))
        pygame.display.get_surface().blit(font_italic.render(
            "Hello World", True, (255, 255, 255)), (100, 200))

        # Make Quit button
        pygame.draw.rect(pygame.display.get_surface(),
                         (255, 0, 0), (0, 0, 100, 50))
        pygame.display.get_surface().blit(
            font_normal.render(
                "Quit", True, (255, 255, 255)), (0, 0))
        if (pygame.mouse.get_pressed()[0]):
            if (pygame.mouse.get_pos()[0] <
                    100 and pygame.mouse.get_pos()[1] < 50):
                pygame.quit()
                sys.exit()

        pygame.display.update()


if __name__ == "__main__":
    main()
