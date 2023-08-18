import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
CAMERA_HEIGHT = HEIGHT // 2
FPS = 60
WHITE = (255, 255, 255)
GRAVITY = 0.5
JUMP_POWER = 10

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumping Platformer")

player_image = pygame.Surface((30, 30))
player_image.fill((255, 0, 0))

cloud_texture = pygame.image.load("cloud_texture.png").convert_alpha()

CLOUD_WIDTH = 80
CLOUD_HEIGHT = 50

PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 10

player_rect = player_image.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT // 2)

platforms = []
clouds = []
platform_y = HEIGHT - PLATFORM_HEIGHT
while platform_y > CAMERA_HEIGHT:
    x = random.randint(0, WIDTH - PLATFORM_WIDTH)
    platform = pygame.Rect(x, platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
    platforms.append(platform)
    platform_y -= JUMP_POWER * 2

cloud_y = HEIGHT - CLOUD_HEIGHT
while cloud_y > CAMERA_HEIGHT:
    x = random.randint(0, WIDTH - CLOUD_WIDTH)
    cloud = pygame.Rect(x, cloud_y, CLOUD_WIDTH, CLOUD_HEIGHT)
    clouds.append(cloud)
    cloud_y -= JUMP_POWER * 3

moving_platforms = []
for _ in range(8):
    x = random.randint(0, WIDTH - cloud_texture.get_width())
    y = random.randint(CAMERA_HEIGHT, HEIGHT - 200)
    platform = pygame.Rect(x, y, CLOUD_WIDTH, CLOUD_HEIGHT)
    speed = random.uniform(0.5, 1.5)
    direction = random.choice([-1, 1])
    moving_platforms.append((platform, speed, direction))

player_velocity_y = 0
camera_y = 0
player_jump_start_y = None
on_ground = False
on_moving_platform = False
current_moving_platform = None

def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and on_ground:
            player_velocity_y = -JUMP_POWER
            on_ground = False
            player_jump_start_y = player_rect.y

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5

    player_velocity_y += GRAVITY
    player_rect.y += player_velocity_y

    if player_rect.top < camera_y:
        camera_y = player_rect.top

    if player_rect.top < CAMERA_HEIGHT:
        new_platform = pygame.Rect(random.randint(0, WIDTH - PLATFORM_WIDTH), camera_y - PLATFORM_HEIGHT, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        platforms.append(new_platform)

        new_cloud = pygame.Rect(random.randint(0, WIDTH - CLOUD_WIDTH), camera_y - CLOUD_HEIGHT, CLOUD_WIDTH, CLOUD_HEIGHT)
        clouds.append(new_cloud)

    for i, (platform, speed, direction) in enumerate(moving_platforms):
        platform.x += speed * direction
        if platform.right > WIDTH or platform.left < 0:
            direction *= -1
        moving_platforms[i] = (platform, speed, direction)

    on_moving_platform = False
    for platform, _, _ in moving_platforms:
        if check_collision(player_rect, platform):
            on_moving_platform = True
            current_moving_platform = platform
            break

    if on_moving_platform:
        player_rect.x += speed * direction
        if player_rect.left < 0:
            player_rect.left = 0
        if player_rect.right > WIDTH:
            player_rect.right = WIDTH

        if player_velocity_y > 0 and player_rect.centery < platform.top:
            player_rect.bottom = platform.top
            player_velocity_y = 0
            on_ground = True

    # Check collision with stationary platforms
    for platform in platforms:
        if check_collision(player_rect, platform) and player_velocity_y > 0 and player_rect.centery < platform.top:
            player_rect.bottom = platform.top
            player_velocity_y = 0
            on_ground = True

    # Prevent walking on top of clouds
    if on_moving_platform and player_rect.bottom <= current_moving_platform.top:
        player_rect.bottom = current_moving_platform.top
        player_velocity_y = 0
        on_ground = True

    # Allow dropping down from clouds
    if on_moving_platform and not check_collision(player_rect, current_moving_platform):
        on_moving_platform = False

    # Adjust camera when player goes up
    if player_jump_start_y is not None and player_rect.y < player_jump_start_y:
        camera_y = max(player_rect.y - CAMERA_HEIGHT, camera_y)

    if player_rect.top < camera_y:
        player_rect.top = camera_y
        player_velocity_y = 0

    if player_rect.bottom > HEIGHT:
        player_rect.bottom = HEIGHT
        player_velocity_y = 0
        on_ground = True

    screen.fill(WHITE)
    for cloud in clouds:
        cloud_texture_resized = pygame.transform.scale(cloud_texture, (CLOUD_WIDTH, CLOUD_HEIGHT))
        screen.blit(cloud_texture_resized, (cloud.x, cloud.y - camera_y))
    for platform in platforms:
        pygame.draw.rect(screen, (0, 0, 255), (platform.x, platform.y - camera_y, PLATFORM_WIDTH, PLATFORM_HEIGHT))
    for platform, _, _ in moving_platforms:
        cloud_texture_resized = pygame.transform.scale(cloud_texture, (CLOUD_WIDTH, CLOUD_HEIGHT))
        screen.blit(cloud_texture_resized, (platform.x, platform.y - camera_y))

    screen.blit(player_image, (player_rect.x, player_rect.y - camera_y))  # Draw the player

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
