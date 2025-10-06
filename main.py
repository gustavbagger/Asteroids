#before running anything, use this:
# source .venv/bin/activate


import pygame
from constants import *
from player import *

updatable = pygame.sprite.Group()
drawable = pygame.sprite.Group()

def main(): 
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    Player.containers = (updatable, drawable)
    Play = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        updatable.update(dt)
        screen.fill("black")
        for draw_object in drawable:
            draw_object.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
