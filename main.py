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
pygame.display.set_caption("Platform Climber")

cloud_texture = pygame.image.load("cloud_texture.png").convert_alpha()

player = Player(WIDTH, HEIGHT, spawn_y=HEIGHT - 100)  # Pass HEIGHT value to Player constructor
platforms = Platform.generate_initial_platforms(WIDTH, HEIGHT, CAMERA_HEIGHT, player.rect.y)
clouds = Cloud.generate_clouds(WIDTH, HEIGHT, cloud_texture, player.camera_y)

clock = pygame.time.Clock()
running = True

generate_new_platform = True  # Flag to control platform generation

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    player.update(keys, platforms)
    player.move_camera()

    if generate_new_platform and player.camera_y <= 0:
        new_platform = Platform.generate_platform(WIDTH, HEIGHT, CAMERA_HEIGHT, player.rect.y, platforms[-1].rect.y)
        platforms.append(new_platform)
        generate_new_platform = False

    screen.fill(WHITE)

    for cloud in clouds:
        screen.blit(cloud.cloud_texture, (cloud.rect.x, cloud.rect.y - player.camera_y))
        if cloud.is_moving:
            cloud.rect.x += cloud.speed * cloud.direction
            if cloud.rect.left <= 0 or cloud.rect.right >= WIDTH:
                cloud.direction *= -1

    for platform in platforms:
        screen.blit(platform.texture, (platform.rect.x, platform.rect.y - player.camera_y))
        if platform.is_moving:
            platform.rect.x += platform.speed * platform.direction
            if platform.rect.left <= 0 or platform.rect.right >= WIDTH:
                platform.direction *= -1

    screen.blit(player.image, (player.rect.x, player.rect.y - player.camera_y))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
