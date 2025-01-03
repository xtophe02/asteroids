from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN, RESPAWN_INVULNERABILITY
import pygame
from shot import Shot


class Player(CircleShape):
    containers = None
  
    
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.spawn_position = pygame.Vector2(x, y)  # Store initial position
        self.invulnerable = 0  # Invulnerability timer
        
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        # Flashing effect when invulnerable
        if self.invulnerable <= 0 or int(self.invulnerable * 10) % 2:
            pygame.draw.polygon(screen, "white", self.triangle(), width=2)
    
    def rotate(self, dt):
        self.rotation +=  (PLAYER_TURN_SPEED * dt)
    
    def update(self, dt):
        if self.invulnerable > 0:
            self.invulnerable -= dt
        keys = pygame.key.get_pressed()
        self.timer -= dt
        if keys[pygame.K_a]:
            self.rotate(dt*-1)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt*-1)
        if keys[pygame.K_SPACE]:
            self.shoot()
        

    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer <= 0:  # Only shoot if cooldown has elapsed
            self.timer = PLAYER_SHOOT_COOLDOWN
            shot = Shot(self.position.x, self.position.y)
            shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED 
     
    def respawn(self):
        self.position = pygame.Vector2(self.spawn_position)
        self.velocity = pygame.Vector2(0, 0)
        self.rotation = 0
        self.invulnerable = RESPAWN_INVULNERABILITY
     