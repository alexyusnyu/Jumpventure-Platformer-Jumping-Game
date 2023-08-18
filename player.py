import pygame

class Player:
    def __init__(self, screen_width, screen_height):
        self.image = pygame.Surface((30, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, 0)

        self.velocity_y = 0
        self.camera_y = 0
        self.screen_width = screen_width
        self.screen_height = screen_height

        self.is_jumping = False
        self.jump_power = -12

    def update(self, keys, platforms):
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
            self.rect.x = max(self.rect.x, 0)  # Prevent from going off the left edge
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
            self.rect.x = min(self.rect.x, self.screen_width - self.rect.width)  # Prevent from going off the right edge

        if keys[pygame.K_SPACE] and not self.is_jumping:
            self.velocity_y = self.jump_power
            self.is_jumping = True

        self.velocity_y += 0.5
        self.rect.y += self.velocity_y

        # Update camera position
        self.camera_y = max(self.rect.y - self.screen_height // 2, 0)

        self.check_collision(platforms)

    def check_collision(self, platforms):
        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.velocity_y > 0 and self.rect.centery < platform.rect.top:
                self.rect.bottom = platform.rect.top
                self.velocity_y = 0
                self.is_jumping = False

        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
            self.velocity_y = 0
            self.is_jumping = False
