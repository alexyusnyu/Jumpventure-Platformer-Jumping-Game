import pygame
import random

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width):
        super().__init__()

        self.width = width

        # Load platform texture
        self.texture = pygame.image.load("textures/platform_texture.png").convert_alpha()
        self.texture = pygame.transform.scale(self.texture, (self.width, 20))

        self.image = self.texture
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    @staticmethod
    def generate_initial_platforms(screen_width, screen_height, camera_height, player_y):
        platforms = pygame.sprite.Group()

        num_platforms = 4
        distance = 150

        for _ in range(num_platforms):
            x = random.randint(0, screen_width - 100)
            y = player_y + distance
            width = random.randint(50, 150)
            platform = Platform(x, y, width)
            platforms.add(platform)
            distance += 150

        return platforms

    def update(self):
        pass
