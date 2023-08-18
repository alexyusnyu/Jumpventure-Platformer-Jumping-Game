# main.py

import pygame
import os
from player import Player
from platform import Platform
from enemy import Enemy
from spritesheet import SpriteSheet

# Initialize pygame
pygame.init()

# Game window dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Jumpy')

# Set frame rate
clock = pygame.time.Clock()
FPS = 60

# Load music and sounds
mixer.init()
pygame.mixer.music.load('assets/music.mp3')
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1, 0.0)
jump_fx = pygame.mixer.Sound('assets/jump.mp3')
jump_fx.set_volume(0.5)
death_fx = pygame.mixer.Sound('assets/death.mp3')
death_fx.set_volume(0.5)

# ... (rest of the code, including variables, fonts, images)

def main():
    # ... (create player instance, sprite groups, and starting platform)

    # Main game loop
    run = True
    while run:
        clock.tick(FPS)

        # ... (game loop code)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Update high score
                if score > high_score:
                    high_score = score
                    with open('score.txt', 'w') as file:
                        file.write(str(high_score))
                run = False

        # Update display window
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
