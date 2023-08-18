import pygame
from main import HEIGHT  # Import HEIGHT from main.py

class Player(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()

        self.image = pygame.image.load("textures/player_texture.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.centerx = screen_width // 2
        self.rect.bottom = screen_height - 100
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
            self.velocity = 0

        self.check_collision(platforms)

    def check_collision(self, platforms):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.rect.bottom = hits[0].rect.top
            self.velocity = 0
