import pygame
import os

# Try to initialize pygame mixer for sound loading
try:
    pygame.mixer.init()
    SOUND_ENABLED = True
except pygame.error:
    print("Warning: Sound system not available")
    SOUND_ENABLED = False

class AssetManager:
    def __init__(self):
        # Dictionaries to store loaded assets
        self.images = {}
        self.sounds = {}
        
        # Default assets for fallback
        self._create_default_assets()
    
    def _create_default_assets(self):
        """Create default assets to use as fallbacks"""
        # Create a default surface for missing images
        default_surface = pygame.Surface((32, 32))
        default_surface.fill((255, 0, 255))  # Fill with magenta for visibility
        pygame.draw.rect(default_surface, (0, 0, 0), default_surface.get_rect(), 1)
        self.default_image = default_surface
        
    def load_image(self, path):
        """Load an image and cache it"""
        try:
            # Check if image is already loaded
            if path in self.images:
                return self.images[path]
            
            # Ensure the path exists
            if not os.path.exists(path):
                print(f"Warning: Image not found at {path}")
                return self.default_image
            
            # Load and convert the image
            image = pygame.image.load(path).convert_alpha()
            self.images[path] = image
            return image
            
        except Exception as e:
            print(f"Error loading image {path}: {str(e)}")
            return self.default_image
    
    def load_sound(self, path):
        """Load a sound and cache it"""
        if not SOUND_ENABLED:
            return None
            
        try:
            # Check if sound is already loaded
            if path in self.sounds:
                return self.sounds[path]
            
            # Ensure the path exists
            if not os.path.exists(path):
                print(f"Warning: Sound not found at {path}")
                return None
            
            # Load the sound
            sound = pygame.mixer.Sound(path)
            self.sounds[path] = sound
            return sound
            
        except Exception as e:
            print(f"Error loading sound {path}: {str(e)}")
            return None
    
    def get_image(self, path):
        """Get a loaded image or load it if not cached"""
        return self.load_image(path)
    
    def get_sound(self, path):
        """Get a loaded sound or load it if not cached"""
        return self.load_sound(path)

# Create a global instance of the asset manager
asset_manager = AssetManager()