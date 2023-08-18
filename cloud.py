import pygame
import random

class Cloud(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((100, 60))  # Adjust cloud size
        self.image.fill((255, 255, 255))  # Adjust cloud color
        self.rect = self.image.get_rect(topleft=(x, y))

class CloudGenerator:
    @staticmethod
    def generate_cloud(screen_width, screen_height, camera_height, player_y):
        x = random.randint(0, screen_width)
        y = camera_height + player_y - random.randint(100, 400)  # Adjust cloud y position
        return Cloud(x, y)
