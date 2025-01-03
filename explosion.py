import pygame
from constants import EXPLOSION_DURATION

class Explosion(pygame.sprite.Sprite):
    containers = None
    
    def __init__(self, x, y, radius):
        super().__init__(self.containers)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.timer = EXPLOSION_DURATION
        
    def update(self, dt):
        self.timer -= dt
        if self.timer <= 0:
            self.kill()
            
    def draw(self, screen):
        # Fade out as timer decreases
        alpha = int((self.timer / EXPLOSION_DURATION) * 255)
        color = (255, 200, 50, alpha)  # Yellow-orange color
        
        # Draw expanding circle
        size = self.radius * (1 + (1 - self.timer / EXPLOSION_DURATION))
        surf = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
        pygame.draw.circle(surf, color, (size, size), size)
        screen.blit(surf, self.position - pygame.Vector2(size, size)) 