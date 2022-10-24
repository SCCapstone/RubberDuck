# Create Pygame ins
import pygame 

pygame.init()
pygame.display.set_mode((800, 600))
pygame.display.set_caption("Duck In Space")
pygame.display.update()

# keep open till user closes
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()