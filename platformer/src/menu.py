import pygame
import random
from platformer.src.settings import *
from platformer.src.asset_manager import asset_manager

class Button:
    def __init__(self, x, y, width, height, text, font_size=32):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font_size = font_size
        self.font = pygame.font.Font(None, font_size)
        
        # Colors
        self.normal_color = (70, 70, 70)
        self.hover_color = (100, 100, 100)
        self.text_color = WHITE
        
        # Button states
        self.is_hovered = False
        
        # Animation
        self.scale = 1.0
        self.target_scale = 1.0
        
    def update(self, mouse_pos):
        # Check if mouse is hovering over button
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        
        # Update scale for hover animation
        if self.is_hovered:
            self.target_scale = 1.1
        else:
            self.target_scale = 1.0
            
        # Smooth scale animation
        self.scale += (self.target_scale - self.scale) * 0.2
        
    def draw(self, screen):
        # Calculate scaled dimensions
        scaled_rect = pygame.Rect(
            self.rect.x - (self.rect.width * (self.scale - 1)) / 2,
            self.rect.y - (self.rect.height * (self.scale - 1)) / 2,
            self.rect.width * self.scale,
            self.rect.height * self.scale
        )
        
        # Draw button background
        color = self.hover_color if self.is_hovered else self.normal_color
        pygame.draw.rect(screen, color, scaled_rect, border_radius=12)
        
        # Draw button text
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=scaled_rect.center)
        screen.blit(text_surface, text_rect)

class MainMenu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        
        # Create buttons
        button_width = 200
        button_height = 50
        start_x = SCREEN_WIDTH // 2 - button_width // 2
        
        self.buttons = {
            'start': Button(start_x, 250, button_width, button_height, "Start Game"),
            'options': Button(start_x, 320, button_width, button_height, "Options"),
            'quit': Button(start_x, 390, button_width, button_height, "Quit")
        }
        
        # Title text
        self.title_font = pygame.font.Font(None, 74)
        self.title_text = "Platformer Adventure"
        self.title_color = WHITE
        
        # Background effect variables
        self.particles = [(pygame.math.Vector2(random.randint(0, SCREEN_WIDTH),
                                             random.randint(0, SCREEN_HEIGHT)),
                          pygame.math.Vector2(1, 1))
                         for _ in range(50)]
        
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                for button_name, button in self.buttons.items():
                    if button.is_hovered:
                        return button_name
        return None
    
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        
        # Update buttons
        for button in self.buttons.values():
            button.update(mouse_pos)
            
        # Update particles
        for particle, velocity in self.particles:
            particle.x = (particle.x + velocity.x) % SCREEN_WIDTH
            particle.y = (particle.y + velocity.y) % SCREEN_HEIGHT
    
    def draw(self):
        # Fill background
        self.screen.fill((40, 40, 40))
        
        # Draw particles
        for particle, _ in self.particles:
            pygame.draw.circle(self.screen, (100, 100, 100), particle, 2)
        
        # Draw title with shadow
        title_surface = self.title_font.render(self.title_text, True, self.title_color)
        title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, 150))
        
        # Draw shadow
        shadow_surface = self.title_font.render(self.title_text, True, (30, 30, 30))
        shadow_rect = shadow_surface.get_rect(center=(SCREEN_WIDTH // 2 + 4, 154))
        self.screen.blit(shadow_surface, shadow_rect)
        
        # Draw main title
        self.screen.blit(title_surface, title_rect)
        
        # Draw buttons
        for button in self.buttons.values():
            button.draw(self.screen)
        
        pygame.display.flip()
        self.clock.tick(FPS)

class PauseMenu:
    def __init__(self, screen):
        self.screen = screen
        self.surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        self.surface.fill((0, 0, 0, 128))  # Semi-transparent black
        
        # Create buttons
        button_width = 200
        button_height = 50
        start_x = SCREEN_WIDTH // 2 - button_width // 2
        
        self.buttons = {
            'resume': Button(start_x, 250, button_width, button_height, "Resume"),
            'menu': Button(start_x, 320, button_width, button_height, "Main Menu")
        }
        
        self.title_font = pygame.font.Font(None, 74)
        self.title_text = "Paused"
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left click
                for button_name, button in self.buttons.items():
                    if button.is_hovered:
                        return button_name
        return None
    
    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        for button in self.buttons.values():
            button.update(mouse_pos)
    
    def draw(self, game_surface):
        # Draw the game screen first
        self.screen.blit(game_surface, (0, 0))
        
        # Draw semi-transparent overlay
        self.screen.blit(self.surface, (0, 0))
        
        # Draw title
        title_surface = self.title_font.render(self.title_text, True, WHITE)
        title_rect = title_surface.get_rect(center=(SCREEN_WIDTH // 2, 150))
        self.screen.blit(title_surface, title_rect)
        
        # Draw buttons
        for button in self.buttons.values():
            button.draw(self.screen)
        
        pygame.display.flip()