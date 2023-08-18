import pygame
import random

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        super().__init__()
        self.image = pygame.Surface((width, 20))  # Adjust platform size
        self.image.fill((0, 255, 0))  # Adjust platform color
        self.rect = self.image.get_rect(topleft=(x, y))

class PlatformGenerator:
    @staticmethod
    def generate_initial_platforms(screen_width, screen_height, player_y):
        platforms = []
        x = screen_width // 2 - 50  # Center the initial platform
        y = player_y + 150  # Adjust initial platform y position
        width = 100  # Adjust initial platform width
        platforms.append(Platform(x, y, width))
        return platforms

    @staticmethod
    def generate_platform(screen_width, screen_height, camera_height, player_y):
        x = random.randint(0, screen_width - 100)
        y = camera_height + player_y - random.randint(100, 200)  # Adjust platform y position range
        width = random.randint(50, 150)  # Adjust platform width range
        return Platform(x, y, width)
