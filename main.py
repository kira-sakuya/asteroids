# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
import player

# Pour avoir accès à pygame lancer dans le terminal "source venv/bin/activate"

def main():
    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    ply = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill('black')
        ply.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        ply.update(dt)

if __name__ == "__main__":
    main()
