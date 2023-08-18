import pygame

class Player:
    def __init__(self, screen_width, screen_height):
        self.image = pygame.image.load("player_texture.png").convert_alpha()  # Load player texture
        self.image = pygame.transform.scale(self.image, (50, 50))  # Adjust player size
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, 0)
        self.velocity = 0
        self.gravity = 1
        self.is_jumping = False
        self.jump_count = 0
        self.jump_power = -15
        self.camera_y = 0
        self.screen_height = screen_height  # Store screen height

    def jump(self):
        if not self.is_jumping and self.jump_count < 2:
            self.velocity = self.jump_power
            self.is_jumping = True
            self.jump_count += 1

    def update(self, keys, platforms):
        self.velocity += self.gravity
        self.rect.y += self.velocity

        if self.rect.bottom >= self.screen_height:  # Use screen_height here
            self.rect.bottom = self.screen_height
            self.velocity = 0
            self.is_jumping = False
            self.jump_count = 0

        for platform in platforms:
            if self.rect.colliderect(platform.rect) and self.velocity > 0:
                self.rect.bottom = platform.rect.top
                self.velocity = 0
                self.is_jumping = False
                self.jump_count = 0

    def move_camera(self):
        if self.rect.top <= self.camera_y + 200:
            self.camera_y -= 5  # Adjust camera movement speed

    def stop_camera(self):
        if self.rect.top >= self.camera_y + 400:
            self.camera_y += 5  # Adjust camera movement speed
