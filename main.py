import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_LIVES
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from explosion import Explosion
import sys

def main():
    # Either uncomment this:
    pygame.init()
    
    # OR add this after the print statements:
    # pygame.font.init()
    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    explosions = pygame.sprite.Group()
    
    
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    Explosion.containers = (explosions, updatable, drawable)
    
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()
   
    score = 0
    font = pygame.font.Font(None, 36)
    
    lives = PLAYER_LIVES
    
    while True:
        dt = clock.tick(60) / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
                
        for sprite in updatable:
            sprite.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player) and player.invulnerable <= 0:
                lives -= 1
                if lives <= 0:
                    print("Game Over!")
                    sys.exit(0)
                else:
                    player.respawn()
            for shot in shots:
                if asteroid.collision(shot):
                    score += 100
                    asteroid.split()
                    shot.kill()
        screen.fill("black")
        for sprite in drawable:  # Each sprite is a Player instance
            sprite.draw(screen)  # Call the draw method on the sprite
        
        score_text = font.render(f"Score: {score}", True, "white")
        screen.blit(score_text, (10, 10))
        
        lives_text = font.render(f"Lives: {lives}", True, "white")
        screen.blit(lives_text, (10, 50))
        
        pygame.display.flip()


if __name__ == "__main__":
    main()
