import pygame
import random

class Cloud:
    def __init__(self, x, y, cloud_texture):
        self.rect = pygame.Rect(x, y, 80, 50)  # Adjust size as needed
        self.cloud_texture = cloud_texture

    @staticmethod
    def generate_clouds(screen_height, camera_height):
        clouds = []
        cloud_y = screen_height - 50  # Adjust initial cloud position
        while cloud_y > camera_height:
            x = random.randint(0, WIDTH - 80)  # Adjust width of the cloud
            clouds.append(Cloud(x, cloud_y, cloud_texture))
            cloud_y -= random.randint(100, 150)  # Adjust gap between clouds
        return clouds
