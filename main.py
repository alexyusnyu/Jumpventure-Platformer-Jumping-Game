import pygame
import random
import os
from pygame import mixer
from spritesheet import SpriteSheet
from enemy import Opponent

mixer.init()
pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('AdventureTime')

clock = pygame.time.Clock()
FPS = 60

pygame.mixer.music.load('assets/theme.mp3')
pygame.mixer.music.set_volume(0.6)
pygame.mixer.music.play(-1, 0.0)
jump_sound = pygame.mixer.Sound('assets/jump.mp3')
jump_sound.set_volume(0.5)
collision_sound = pygame.mixer.Sound('assets/collision.mp3')
collision_sound.set_volume(0.5)

SCROLL_THRESHOLD = 200
GRAVITY = 1
MAX_PLATFORMS = 10
scroll = 0
bg_scroll = 0
game_over = False
score = 0
fade_counter = 0

if os.path.exists('top_score.txt'):
    with open('top_score.txt', 'r') as file:
        highest_score = int(file.read())
else:
    highest_score = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PANEL_COLOR = (153, 217, 234)

font_small = pygame.font.SysFont('Arial', 20)
font_big = pygame.font.SysFont('Arial', 24)

player_image = pygame.image.load('assets/player.png').convert_alpha()
background_image = pygame.image.load('assets/background.png').convert_alpha()
platform_image = pygame.image.load('assets/platform.png').convert_alpha()
opponent_sheet_image = pygame.image.load('assets/opponent_sheet.png').convert_alpha()
opponent_sheet = SpriteSheet(opponent_sheet_image)

# Function for displaying text on the screen
def draw_text(text, font, text_color, x, y):
    text_image = font.render(text, True, text_color)
    screen.blit(text_image, (x, y))

# Function for drawing the information panel
def draw_panel():
    pygame.draw.rect(screen, BLACK, (0, 0, SCREEN_WIDTH, 30))
    pygame.draw.line(screen, WHITE, (0, 30), (SCREEN_WIDTH, 30), 2)
    draw_text('SCORE: ' + str(score), font_small, WHITE, 0, 0)

# Function for drawing the background
def draw_background(bg_scroll):
    screen.blit(background_image, (0, 0 + bg_scroll))
    screen.blit(background_image, (0, -600 + bg_scroll))

class Protagonist():
    def __init__(self, x, y):
        self.image = pygame.transform.scale(player_image, (45, 45))
        self.width = 25
        self.height = 40
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = (x, y)
        self.vel_y = 0
        self.flip_horizontal = False

    def move(self):
        scroll = 0
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx = -10
            self.flip_horizontal = True
        if key[pygame.K_RIGHT]:
            dx = 10
            self.flip_horizontal = False

        self.vel_y += GRAVITY
        dy += self.vel_y

        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > SCREEN_WIDTH:
            dx = SCREEN_WIDTH - self.rect.right

        for platform in platform_group:
            if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                if self.rect.bottom < platform.rect.centery:
                    if self.vel_y > 0:
                        self.rect.bottom = platform.rect.top
                        dy = 0
                        self.vel_y = -20
                        jump_sound.play()

        if self.rect.top <= SCROLL_THRESHOLD:
            if self.vel_y < 0:
                scroll = -dy

        self.rect.x += dx
        self.rect.y += dy + scroll

        return scroll

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip_horizontal, False), (self.rect.x - 12, self.rect.y - 5))

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, moving):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(platform_image, (width, 10))
        self.moving = moving
        self.move_counter = random.randint(0, 50)
        self.direction = random.choice([-1, 1])
        self.speed = random.randint(1, 2)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self, scroll):
        if self.moving == True:
            self.move_counter += 1
            self.rect.x += self.direction * self.speed

        if self.move_counter >= 100 or self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.direction *= -1
            self.move_counter = 0

        self.rect.y += scroll

        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

jumper = Protagonist(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)

platform_group = pygame.sprite.Group()
opponent_group = pygame.sprite.Group()

platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, False)
platform_group.add(platform)

run = True
while run:
    clock.tick(FPS)

    if not game_over:
        scroll = jumper.move()

        bg_scroll += scroll
        if bg_scroll >= 600:
            bg_scroll = 0
        draw_background(bg_scroll)

        if len(platform_group) < MAX_PLATFORMS:
            p_width = random.randint(40, 60)
            p_x = random.randint(0, SCREEN_WIDTH - p_width)
            p_y = platform.rect.y - random.randint(80, 120)
            p_type = random.randint(1, 2)
            if p_type == 1 and score > 500:
                p_moving = True
            else:
                p_moving = False
            platform = Platform(p_x, p_y, p_width, p_moving)
            platform_group.add(platform)

        platform_group.update(scroll)

        if len(opponent_group) == 0 and score > 1500:
            opponent = Opponent(SCREEN_WIDTH, 100, opponent_sheet, 1.5)
            opponent_group.add(opponent)

        opponent_group.update(scroll, SCREEN_WIDTH)

        if scroll > 0:
            score += scroll

        pygame.draw.line(screen, WHITE, (0, score - highest_score + SCROLL_THRESHOLD), (SCREEN_WIDTH, score - highest_score + SCROLL_THRESHOLD), 3)
        draw_text('HIGHEST SCORE', font_small, WHITE, SCREEN_WIDTH - 130, score - highest_score + SCROLL_THRESHOLD)

        platform_group.draw(screen)
        opponent_group.draw(screen)
        jumper.draw()

        draw_panel()

        if jumper.rect.top > SCREEN_HEIGHT:
            game_over = True
            collision_sound.play()

        if pygame.sprite.spritecollide(jumper, opponent_group, False):
            if pygame.sprite.spritecollide(jumper, opponent_group, False, pygame.sprite.collide_mask):
                game_over = True
                collision_sound.play()
    else:
        if fade_counter < SCREEN_WIDTH:
            fade_counter += 5
            for y in range(0, 6, 2):
                pygame.draw.rect(screen, BLACK, (0, y * 100, fade_counter, 100))
                pygame.draw.rect(screen, BLACK, (SCREEN_WIDTH - fade_counter, (y + 1) * 100, SCREEN_WIDTH, 100))
        else:
            draw_text('GAME OVER!', font_big, WHITE, 130, 200)
            draw_text('SCORE: ' + str(score), font_big, WHITE, 130, 250)
            draw_text('PRESS SPACE TO RESTART', font_big, WHITE, 40, 300)
            if score > highest_score:
                highest_score = score
                with open('top_score.txt', 'w') as file:
                    file.write(str(highest_score))
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE]:
                game_over = False
                score = 0
                scroll = 0
                fade_counter = 0
                jumper.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150)
                opponent_group.empty()
                platform_group.empty()
                platform = Platform(SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 50, 100, False)
                platform_group.add(platform)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            if score > highest_score:
                highest_score = score
                with open('top_score.txt', 'w') as file:
                    file.write(str(highest_score))
            run = False

    pygame.display.update()

pygame.quit()
