import pygame
import random


class Cloud:
    def __init__(self, x, y, cloud_texture, is_moving=False):
        self.rect = pygame.Rect(x, y, 80, 50)  # Adjust size as needed
        self.cloud_texture = cloud_texture
        self.is_moving = is_moving
        self.direction = 1  # 1 for right, -1 for left
        self.speed = 1  # Adjust cloud movement speed

    @staticmethod
    def generate_clouds(screen_width, screen_height, cloud_texture, camera_height):
        clouds = []
        cloud_y = screen_height - 150  # Adjust initial cloud position
        is_moving = False
        while cloud_y > camera_height:
            x = random.randint(0, screen_width - 80)  # Adjust width of the cloud
            clouds.append(Cloud(x, cloud_y, cloud_texture, is_moving))
            cloud_y -= random.randint(100, 150)  # Adjust gap between clouds
            is_moving = not is_moving  # Toggle moving state

        return clouds
