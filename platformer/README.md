# Platformer Adventure

A 2D platformer game built with Python and Pygame.

## Controls

- Left Arrow: Move left
- Right Arrow: Move right
- Space: Jump
- ESC: Pause game

## Features

- Modern main menu with animated buttons
- Collectible coins with score system
- Smooth player movement and physics
- Multiple platforms to explore
- Pause menu system

## Setup

1. Make sure you have Python 3.x installed
2. Install Pygame:
```bash
pip install pygame
```
3. Run the game:
```bash
python main.py
```

## Game Elements

- Player: Blue rectangle that can move and jump
- Platforms: Green rectangles to stand on
- Coins: Yellow circles to collect
- Score: Displayed in the top-left corner

## Development

The game is structured in a modular way:
- `main.py`: Entry point
- `src/game.py`: Main game logic
- `src/sprites.py`: Game objects (Player, Platform, Coin)
- `src/menu.py`: Menu system
- `src/settings.py`: Game constants and configuration
- `src/asset_manager.py`: Resource loading and management