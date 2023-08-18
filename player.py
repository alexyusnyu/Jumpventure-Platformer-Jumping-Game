import pygame
from main import HEIGHT  # Import HEIGHT from main.py

class Player:
    def __init__(self, screen_width, screen_height):
        self.image = pygame.image.load("player_texture.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 100)
        self.camera_y = 0
        self.velocity = 0
        self.jump_power = -15
        self.gravity = 0.8

    def jump(self):
        if self.rect.bottom == HEIGHT:
            self.velocity = self.jump_power

    def update(self, keys, platforms):
        self.velocity += self.gravity
        self.rect.y += self.velocity

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def move_camera(self):
        self.camera_y = self.rect.y - HEIGHT // 2
