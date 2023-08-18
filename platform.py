import pygame
import random


class Platform:
    def __init__(self, x, y, is_moving=False):
        self.rect = pygame.Rect(x, y, 100, 10)  # Adjust size as needed
        self.is_moving = is_moving
        self.direction = 1  # 1 for right, -1 for left
        self.speed = 2  # Adjust platform movement speed

    @staticmethod
    def generate_platforms(screen_width, screen_height, camera_height, player_y):
        platforms = []
        platform_y = screen_height - 10  # Adjust initial platform position
        is_moving = False
        while platform_y > camera_height:
            x = random.randint(0, screen_width - 100)  # Adjust width of the platform
            platforms.append(Platform(x, platform_y, is_moving))
            platform_y -= random.randint(70, 120)  # Adjust gap between platforms
            is_moving = not is_moving  # Toggle moving state

        # Generate additional platforms as camera moves higher
        while platform_y > player_y - 300:  # Adjust the threshold for generating additional platforms
            x = random.randint(0, screen_width - 100)
            platforms.append(Platform(x, platform_y, is_moving))
            platform_y -= random.randint(70, 120)
            is_moving = not is_moving

        return platforms
