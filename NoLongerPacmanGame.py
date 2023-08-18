import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
PLATFORM_WIDTH = 100
PLATFORM_HEIGHT = 10
PLATFORM_COLOR = (0, 0, 255)
GRAVITY = 0.5
JUMP_POWER = 10

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Platformer")

# Load images
player_image = pygame.Surface((30, 30))
player_image.fill((255, 0, 0))

# Create player
player_rect = player_image.get_rect()
player_rect.center = (WIDTH // 2, HEIGHT // 2)

# Create platforms
platforms = []
platform_y = HEIGHT - PLATFORM_HEIGHT  # Start from the bottom
while platform_y > 100:
    x = random.randint(0, WIDTH - PLATFORM_WIDTH)
    platform = pygame.Rect(x, platform_y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
    platforms.append(platform)

    platform_y -= random.randint(80, 120)  # Vary platform spacing

# Create moving platforms
moving_platforms = []
for _ in range(3):
    x = random.randint(0, WIDTH - PLATFORM_WIDTH)
    y = random.randint(100, HEIGHT - 200)
    platform = pygame.Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
    speed = random.uniform(1, 3)  # Random speed between 1 and 3
    moving_platforms.append((platform, speed))

# Player's vertical velocity
player_velocity_y = 0
on_ground = False

# Main game loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and on_ground:
            player_velocity_y = -JUMP_POWER
            on_ground = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5

    # Apply gravity
    player_velocity_y += GRAVITY
    player_rect.y += player_velocity_y

    # Check for collisions with platforms
    for platform in platforms:
        if player_rect.colliderect(platform) and player_rect.bottom > platform.top:
            player_rect.bottom = platform.top
            player_velocity_y = 0
            on_ground = True
            break

    # Update moving platforms
    for platform, speed in moving_platforms:
        platform.x += speed
        if platform.right > WIDTH:
            platform.left = 0  # Reset to the left when reaching the screen edge
        pygame.draw.rect(screen, PLATFORM_COLOR, platform)

    # Keep the player within the screen bounds
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > WIDTH:
        player_rect.right = WIDTH
    if player_rect.top < 0:
        player_rect.top = 0
    if player_rect.bottom > HEIGHT:
        player_rect.bottom = HEIGHT
        player_velocity_y = 0
        on_ground = True

    # Clear the screen
    screen.fill(WHITE)

    # Draw player
    screen.blit(player_image, player_rect.topleft)

    # Draw platforms
    for platform in platforms:
        pygame.draw.rect(screen, PLATFORM_COLOR, platform)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Clean up
pygame.quit()
sys.exit()
