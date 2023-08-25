import pygame
import random

class Opponent(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, y, custom_sheet, scale):
        pygame.sprite.Sprite.__init__(self)

        self.animation_frames = []
        self.current_frame = 0
        self.update_timer = pygame.time.get_ticks()
        self.direction = random.choice([-1, 1])
        if self.direction == 1:
            self.flip_horizontal = True
        else:
            self.flip_horizontal = False

        animation_steps = 8
        for animation in range(animation_steps):
            frame = custom_sheet.extract_image(animation, 32, 32, scale, (0, 0, 0))
            frame = pygame.transform.flip(frame, self.flip_horizontal, False)
            frame.set_colorkey((0, 0, 0))
            self.animation_frames.append(frame)

        self.image = self.animation_frames[self.current_frame]
        self.rect = self.image.get_rect()

        if self.direction == 1:
            self.rect.x = 0
        else:
            self.rect.x = SCREEN_WIDTH
        self.rect.y = y

    def update(self, scroll, SCREEN_WIDTH):
        ANIMATION_COOLDOWN = 50

        self.image = self.animation_frames[self.current_frame]

        if pygame.time.get_ticks() - self.update_timer > ANIMATION_COOLDOWN:
            self.update_timer = pygame.time.get_ticks()
            self.current_frame += 1
        if self.current_frame >= len(self.animation_frames):
            self.current_frame = 0

        self.rect.x += self.direction * 2
        self.rect.y += scroll

        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()
