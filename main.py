import pygame
import sys
from player import Player
from platform import Platform
from cloud import Cloud

pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Platformer Game")

# Colors
WHITE = (255, 255, 255)

# Player
player = Player(WIDTH // 2, HEIGHT // 2)  # Adjust player spawn position

# Platforms
platforms = Platform.generate_initial_platforms(WIDTH, HEIGHT, player.rect.y)

# Clouds
clouds = Cloud.generate_initial_clouds(WIDTH, HEIGHT)

# Game loop
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    player.update(keys, platforms)

    # Update clouds
    for cloud in clouds:
        cloud.update()

    # Update camera position
    if player.rect.top <= HEIGHT // 4:
        player.pos.y += abs(player.velocity.y)
        for platform in platforms:
            platform.rect.y += abs(player.velocity.y)
        for cloud in clouds:
            cloud.rect.y += abs(player.velocity.y)

    # Generate new platforms and clouds as player goes up
    while len(platforms) < 6:  # Adjust the number of platforms to generate
        new_platform = Platform.generate_platform(WIDTH, HEIGHT, player.rect.y)
        platforms.append(new_platform)

    while len(clouds) < 5:  # Adjust the number of clouds to generate
        new_cloud = Cloud.generate_cloud(WIDTH, HEIGHT)
        clouds.append(new_cloud)

    # Draw everything
    screen.fill(WHITE)
    for platform in platforms:
        platform.draw(screen)
    for cloud in clouds:
        cloud.draw(screen)
    player.draw(screen)

    pygame.display.flip()
    clock.tick(60)
