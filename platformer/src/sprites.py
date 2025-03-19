import pygame
from platformer.src.settings import *
from platformer.src.asset_manager import asset_manager

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Create a temporary rectangle for the player
        self.image = pygame.Surface((30, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Movement variables
        self.velocity_x = 0
        self.velocity_y = 0
        self.on_ground = False
        
        # Score
        self.score = 0
    
    def update(self, platforms):
        # Horizontal movement
        self.rect.x += self.velocity_x
        
        # Check platform collisions - horizontal
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_x > 0:  # Moving right
                    self.rect.right = platform.rect.left
                elif self.velocity_x < 0:  # Moving left
                    self.rect.left = platform.rect.right
        
        # Vertical movement
        self.velocity_y += GRAVITY
        self.rect.y += self.velocity_y
        
        # Check platform collisions - vertical
        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity_y > 0:  # Moving down
                    self.rect.bottom = platform.rect.top
                    self.on_ground = True
                    self.velocity_y = 0
                elif self.velocity_y < 0:  # Moving up
                    self.rect.top = platform.rect.bottom
                    self.velocity_y = 0
    
    def jump(self):
        if self.on_ground:
            self.velocity_y = PLAYER_JUMP_POWER
    
    def move_left(self):
        self.velocity_x = -PLAYER_SPEED
    
    def move_right(self):
        self.velocity_x = PLAYER_SPEED
    
    def stop(self):
        self.velocity_x = 0

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        # Create a temporary yellow circle for the coin
        self.image = pygame.Surface((20, 20), pygame.SRCALPHA)
        pygame.draw.circle(self.image, YELLOW, (10, 10), 10)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # Animation variables
        self.animation_frame = 0
        self.animation_speed = 0.2
        
    def update(self):
        # Simple animation - make the coin bob up and down
        self.animation_frame += self.animation_speed
        offset = int(abs(pygame.math.sin(self.animation_frame) * 5))
        self.rect.y += offset
        
        # Reset the position after moving to avoid drifting
        self.rect.y = self.rect.y - offset