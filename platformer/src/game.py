import pygame
from platformer.src.settings import *
from platformer.src.sprites import Player, Platform, Coin
from platformer.src.menu import MainMenu, PauseMenu
from platformer.src.asset_manager import asset_manager

class Game:
    def __init__(self):
        # Initialize display
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()
        
        # Game state
        self.state = MENU
        self.running = True
        
        # Create sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        
        # Create menus
        self.main_menu = MainMenu(self.screen)
        self.pause_menu = PauseMenu(self.screen)
        
        # Game surface for pause overlay
        self.game_surface = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        
        # Initialize game
        self.setup_game()
    
    def setup_game(self):
        """Initialize game objects"""
        # Clear sprite groups
        self.all_sprites.empty()
        self.platforms.empty()
        self.coins.empty()
        
        # Create platforms from settings
        for plat in PLATFORM_LIST:
            platform = Platform(*plat)
            self.all_sprites.add(platform)
            self.platforms.add(platform)
        
        # Create player
        self.player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
        self.all_sprites.add(self.player)
        
        # Create coins
        for coin_pos in COIN_POSITIONS:
            coin = Coin(*coin_pos)
            self.all_sprites.add(coin)
            self.coins.add(coin)
    
    def handle_events(self):
        """Handle game events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state == PLAYING:
                        self.state = "PAUSED"
                    elif self.state == "PAUSED":
                        self.state = PLAYING
                        
                if self.state == PLAYING:
                    if event.key == pygame.K_SPACE:
                        self.player.jump()
            
            # Handle menu events
            if self.state == MENU:
                action = self.main_menu.handle_event(event)
                if action == 'start':
                    self.state = PLAYING
                elif action == 'quit':
                    self.running = False
                    
            elif self.state == "PAUSED":
                action = self.pause_menu.handle_event(event)
                if action == 'resume':
                    self.state = PLAYING
                elif action == 'menu':
                    self.state = MENU
    
    def update(self):
        """Update game state"""
        if self.state == PLAYING:
            # Get keyboard state
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player.move_left()
            elif keys[pygame.K_RIGHT]:
                self.player.move_right()
            else:
                self.player.stop()
            
            # Update all sprites
            self.all_sprites.update()
            self.player.update(self.platforms)
            
            # Check coin collisions
            coin_hits = pygame.sprite.spritecollide(self.player, self.coins, True)
            for coin in coin_hits:
                self.player.score += COIN_VALUE
                
        elif self.state == MENU:
            self.main_menu.update()
            
        elif self.state == "PAUSED":
            self.pause_menu.update()
    
    def draw(self):
        """Draw the game state"""
        if self.state == PLAYING:
            # Draw game
            self.game_surface.fill((100, 100, 255))  # Sky blue background
            self.all_sprites.draw(self.game_surface)
            
            # Draw score
            font = pygame.font.Font(None, 36)
            score_text = font.render(f'Score: {self.player.score}', True, WHITE)
            self.game_surface.blit(score_text, (10, 10))
            
            # Update screen
            self.screen.blit(self.game_surface, (0, 0))
            pygame.display.flip()
            
        elif self.state == MENU:
            self.main_menu.draw()
            
        elif self.state == "PAUSED":
            self.pause_menu.draw(self.game_surface)
    
    def run(self):
        """Main game loop"""
        try:
            while self.running:
                self.handle_events()
                self.update()
                self.draw()
                self.clock.tick(FPS)
                
        except Exception as e:
            print(f"Game crashed: {str(e)}")
            
        finally:
            pygame.quit()