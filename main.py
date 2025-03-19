import os
import sys
import pygame

# Add the current directory to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from platformer.src.game import Game

def main():
    try:
        # Initialize pygame
        pygame.init()
        
        # Try to initialize sound, but continue if it fails
        try:
            pygame.mixer.init()
        except pygame.error:
            print("Warning: Sound system not available - continuing without sound")
        
        # Create and run game
        game = Game()
        game.run()
        
    except Exception as e:
        print(f"Error running game: {str(e)}")
        
    finally:
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    main()