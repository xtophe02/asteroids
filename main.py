import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    # Initialize Pygame
    # pygame.init()
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()  # renamed for clarity
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        dt = clock.tick(60) / 1000  # Calculate dt first, at the start of each frame
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        screen.fill("black")
        player.update(dt)  # Now dt has a meaningful value
        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
