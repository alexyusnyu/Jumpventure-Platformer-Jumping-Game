import pygame

class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def extract_image(self, frame, width, height, scale, color_key):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
        image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        image.set_colorkey(color_key)

        return image
