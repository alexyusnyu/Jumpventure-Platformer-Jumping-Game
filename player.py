import pygame

class Player:
    def __init__(self, screen_width, screen_height):
        self.image = pygame.image.load("player_texture.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.midbottom = (screen_width // 2, screen_height)
        self.camera_y = 0
        self.velocity = pygame.Vector2(0, 0)
        self.gravity = pygame.Vector2(0, 0.5)
        self.jump_power = -15
        self.on_ground = True

    def update(self, keys, platforms):
        self.move(keys)
        self.apply_physics(platforms)

    def move(self, keys):
        self.velocity.x = 0
        if keys[pygame.K_LEFT]:
            self.velocity.x = -5
        if keys[pygame.K_RIGHT]:
            self.velocity.x = 5
        if keys[pygame.K_SPACE] and self.on_ground:
            self.velocity.y = self.jump_power
            self.on_ground = False

    def apply_physics(self, platforms):
        self.velocity += self.gravity
        self.rect.move_ip(self.velocity)
        self.on_ground = False

        for platform in platforms:
            if self.rect.colliderect(platform.rect):
                if self.velocity.y > 0 and self.rect.bottom <= platform.rect.top + 10:
                    self.rect.bottom = platform.rect.top
                    self.velocity.y = 0
                    self.on_ground = True
                elif self.velocity.y < 0 and self.rect.top >= platform.rect.bottom - 10:
                    self.rect.top = platform.rect.bottom
                    self.velocity.y = 0

    def move_camera(self):
        if self.rect.top <= self.camera_y + 200:
            self.camera_y -= 5
