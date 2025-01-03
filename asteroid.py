from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random
from explosion import Explosion

class Asteroid(CircleShape):
  containers = None
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)


  def draw(self, screen):
      pygame.draw.circle(screen, "white", self.position, self.radius, width=2)
  
  def update(self,dt):
     self.position += (self.velocity*dt)
  
  def split(self):
    # Create explosion effect
    Explosion(self.position.x, self.position.y, self.radius)
    
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
        return
    else:
        angle = random.uniform(20,50)
        A1 = Asteroid(self.position.x,self.position.y,(self.radius - ASTEROID_MIN_RADIUS))
        A2 = Asteroid(self.position.x,self.position.y,(self.radius - ASTEROID_MIN_RADIUS))
        A1.velocity = pygame.math.Vector2.rotate(self.velocity,angle) * 1.2
        A2.velocity = pygame.math.Vector2.rotate(self.velocity,-angle) * 1.2