import pygame
import random

class Cloud:
    def __init__(self, x, y, cloud_texture):
        self.rect = pygame.Rect(x, y, 100, 60)  # Adjust size as needed
        self.cloud_texture = cloud_texture

    @staticmethod
    def generate_clouds(screen_width, screen_height, cloud_texture):
        clouds = []
        cloud_y = screen_height - 50  # Adjust initial cloud position
        while cloud_y > 0:
            x = random.randint(0, screen_width - 100)  # Adjust width of the cloud
            clouds.append(Cloud(x, cloud_y, cloud_texture))
            cloud_y -= random.randint(100, 150)  # Adjust gap between clouds
        return clouds
