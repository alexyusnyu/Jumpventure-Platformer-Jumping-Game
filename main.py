import pygame
from platform import Platform
from player import Player

# Define screen dimensions
WIDTH = 800
HEIGHT = 600
CAMERA_HEIGHT = 400

# Initialize pygame
pygame.init()

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Game")

# Load textures
platform_texture = pygame.image.load("textures/platform_texture.png").convert_alpha()
cloud_texture = pygame.image.load("textures/cloud_texture.png").convert_alpha()

# Generate initial platforms and clouds
player = Player(WIDTH, HEIGHT)  # Create player
platforms = Platform.generate_initial_platforms(WIDTH, HEIGHT, CAMERA_HEIGHT, player.rect.y)
clouds = []  # Create an empty list for clouds

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Update player and platforms
    player.update(keys, platforms)
    if player.rect.top <= CAMERA_HEIGHT:
        platforms = Platform.generate_platforms(WIDTH, CAMERA_HEIGHT, player.rect.y)

    # Clear the screen
    screen.fill((135, 206, 235))

    # Draw clouds
    for cloud in clouds:
        cloud.update()
        cloud.draw(screen)

    # Draw platforms
    for platform in platforms:
        platform.draw(screen)

    # Draw player
    player.draw(screen)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
