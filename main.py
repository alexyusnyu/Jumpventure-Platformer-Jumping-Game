import pygame
import sys
from player import Player
from platform import Platform
from cloud import Cloud

pygame.init()

WIDTH, HEIGHT = 800, 600
CAMERA_HEIGHT = HEIGHT // 2
FPS = 60
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumping Platformer")

# Load cloud texture
cloud_texture = pygame.image.load("cloud_texture.png").convert_alpha()

# Create instances
player = Player(HEIGHT)
platforms = Platform.generate_platforms(WIDTH, HEIGHT, CAMERA_HEIGHT)
clouds = Cloud.generate_clouds(WIDTH, HEIGHT, cloud_texture)  # Pass cloud_texture

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Update player
    player.update(keys, platforms)

    # Clear the screen
    screen.fill(WHITE)

    # Draw clouds
    for cloud in clouds:
        screen.blit(cloud.cloud_texture, (cloud.rect.x, cloud.rect.y - player.camera_y))

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, (0, 0, 255), (platform.rect.x, platform.rect.y - player.camera_y, 100, 10))  # Adjust platform size

    # Draw player
    screen.blit(player.image, (player.rect.x, player.rect.y - player.camera_y))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
