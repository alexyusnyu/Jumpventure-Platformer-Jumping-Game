import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 60))  # Adjust player size
        self.image.fill((0, 0, 255))  # Adjust player color
        self.rect = self.image.get_rect(center=(x, y))
        self.pos = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(0, 0)
        self.gravity = 0.8
        self.jump_power = -15
        self.on_ground = False

    def update(self, keys, platforms):
        self.velocity.y += self.gravity
        self.pos += self.velocity

        self.rect.midbottom = self.pos

        self.on_ground = False
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.velocity.y >= 0:
                self.on_ground = True
                self.pos.y = platform.rect.top + 1
                self.velocity.y = 0

        if self.on_ground:
            if keys[pygame.K_SPACE]:
                self.velocity.y = self.jump_power

    def draw(self, screen):
        screen.blit(self.image, self.rect)
