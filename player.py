import pygame

class Player:
    def __init__(self):
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)  # Player position will be set later

    def update(self, keys, platforms):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

    def apply_gravity(self):
        self.rect.y += self.velocity_y

    def jump(self):
        # Implement jump logic here
        pass
