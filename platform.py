import pygame
import random

class Platform:
    def __init__(self, x, y, width):
        self.rect = pygame.Rect(x, y, width, 20)  # Adjust platform height
        self.texture = pygame.image.load("platform_texture.png").convert_alpha()
        self.texture = pygame.transform.scale(self.texture, (width, 20))  # Adjust platform size
        self.is_moving = False
        self.speed = 2
        self.direction = 1

    @staticmethod
    def generate_initial_platforms(screen_width, screen_height, camera_height, player_y):
        platforms = []
        width = random.randint(150, 300)  # Adjust platform width range
        x = (screen_width - width) // 2  # Place platform in the center
        platforms.append(Platform(x, player_y, width))
        return platforms

    @staticmethod
    def generate_platform(screen_width, screen_height, camera_height, player_y, last_platform_y, move=False):
        x = random.randint(0, screen_width - 150)  # Fix platform width
        width = random.randint(150, 300)  # Adjust platform width range
        y = last_platform_y - random.randint(250, 400)  # Adjust vertical distance
        platform = Platform(x, y, width)
        platform.is_moving = move
        return platform

    @staticmethod
    def generate_more_realistic_platforms(screen_width, screen_height, camera_height, player_y):
        platforms = []
        last_platform_y = player_y
        while last_platform_y > player_y - screen_height:
            platform = Platform.generate_platform(screen_width, screen_height, camera_height, player_y, last_platform_y)
            platforms.append(platform)
            last_platform_y = platform.rect.y
        return platforms
