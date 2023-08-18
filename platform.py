import pygame
import random

class Platform:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 100, 10)  # Adjust size as needed

    @staticmethod
    def generate_platforms(screen_height, camera_height):
        platforms = []
        platform_y = screen_height - 10  # Adjust initial platform position
        while platform_y > camera_height:
            x = random.randint(0, WIDTH - 100)  # Adjust width of the platform
            platforms.append(Platform(x, platform_y))
            platform_y -= random.randint(50, 100)  # Adjust gap between platforms
        return platforms
