import pygame
import random
import os
from pygame import mixer
from player import Player
from platform import Platform
from enemy import Enemy
from spritesheet import SpriteSheet

# Initialize pygame
mixer.init()
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
pygame.mixer.music.load('assets/music.mp3')
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1, 0.0)
jump_fx = pygame.mixer.Sound('assets/jump.mp3')
jump_fx.set_volume(0.5)
death_fx = pygame.mixer.Sound('assets/death.mp3')
death_fx.set_volume(0.5)

# Game variables
SCROLL_THRESH = 200
GRAVITY = 1
MAX_PLATFORMS = 10
scroll = 0
bg_scroll = 0
game_over = False
score = 0
fade_counter = 0

if os.path.exists('score.txt'):
    with open('score.txt', 'r') as file:
        high_score = int(file.read())
else:
    high_score = 0

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PANEL = (153, 217, 234)

# Define font
font_small = pygame.font.SysFont('Lucida Sans', 20)
font_big = pygame.font.SysFont('Lucida Sans', 24)

# Load images
jumpy_image = pygame.image.load('assets/jump.png').convert_alpha()
bg_image = pygame.image.load('assets/bg.png').convert_alpha()
platform_image = pygame.image.load('assets/wood.png').convert_alpha()
bird_sheet_img = pygame.image.load('assets/bird.png').convert_alpha()
bird_sheet = SpriteSheet(bird_sheet_img)

# Initialize player instance
jumpy = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150, jumpy_image, None, GRAVITY, SCREEN_WIDTH, SCROLL_THRESH, jump_fx)

# Create sprite groups
platform_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()

# Create starting platform
platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, False, platform_image, SCREEN_WIDTH, SCREEN_HEIGHT)
platform_group.add(platform)

# Main game loop
def main():
    global scroll, bg_scroll, game_over, score, fade_counter, high_score

    run = True
    while run:
        clock.tick(FPS)

        if game_over == False:
            scroll = jumpy.move()

            bg_scroll += scroll
            if bg_scroll >= 600:
                bg_scroll = 0

            # ... (rest of your game logic)

            pygame.display.update()

        else:
            if fade_counter < SCREEN_WIDTH:
                # ... (fade-out effect)
                pass
            else:
                # ... (game over screen)
                pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # ... (update high score and exit)
                pass

    pygame.quit()

if __name__ == "__main__":
    main()
