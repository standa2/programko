import pygame
from settings import *
from utility import get_image


class Player(pygame.sprite.Sprite):

    def __init__(self, position, sprite_groups):
        super().__init__()

        self.position = position
        self.spritesheet = pygame.image.load(
            "assets/player/man_brownhair_run.png").convert_alpha()
        self.image = get_image(self.spritesheet, 0, 0, 15, 16, 3)
        self.index = 0
        self.rect = self.image.get_rect(topleft=(self.position))
        self.score = 0
        self.health = 100
        self.mortal = False
        self.mad = False
        self.starved = False
        self.elapsed_time = 0
        self.starve_time = 0
        self.speed = 15
        self.height = 16
        self.hunger = 100
        self.monster = 100

        for key, group in sprite_groups.items():
            setattr(self, key, group)

    def update(self):
        dx = 0
        dy = 0

        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            dx -= self.speed
            self.animation(2)
        elif key[pygame.K_RIGHT]:
            dx += self.speed
            self.animation(3)
        elif key[pygame.K_UP]:
            dy -= self.speed
            self.animation(1)
        elif key[pygame.K_DOWN]:
            dy += self.speed
            self.animation(0)

        self.rect.x += dx
        self.rect.y += dy

        for desk in pygame.sprite.spritecollide(self, self.desk_group, False):
            if dx > 0:
                self.rect.right = desk.rect.left
            if dx < 0:
                self.rect.left = desk.rect.right
            if dy > 0:
                self.rect.bottom = desk.rect.top
            if dy < 0:
                self.rect.top = desk.rect.bottom

        if self.rect.x < 0:
            self.rect.x = screen_width
        elif self.rect.x > screen_width:
            self.rect.x = 1

        if self.rect.y < 0:
            self.rect.y = screen_height
        elif self.rect.y > screen_height:
            self.rect.y = 1

        if self.elapsed_time > 3000:
            self.mortal = False
            self.mad = False
            self.speed = 15
            self.spritesheet = pygame.image.load(
                "assets/player/man_brownhair_run.png").convert_alpha()
            self.height = 16

        if self.starve_time > 1000:
            self.hunger -= 5
            self.starve_time = 0
        if self.hunger <= 25:
            self.speed = 5
        if self.hunger <= 50:
            self.speed = 8
        if self.hunger <= 75:
            self.speed = 10
        if self.hunger <= 0:
            self.starved = True

        if pygame.sprite.spritecollide(self, self.monsters_group, False):
            if not self.mortal:
                self.health -= 20
                self.mortal = True
                self.elapsed_time = 0
                self.speed = 4
                self.spritesheet = pygame.image.load(
                    "assets/player/man_brownhair_cry.png").convert_alpha()
            if self.mad == True:
                self.monster -= 25
                self.mad = False

            if self.monster == 50:
                pygame.sprite.spritecollide(self, self.monsters_group, True)
            if self.monster == 0:
                pygame.sprite.spritecollide(self, self.monsters_group, True)

        if pygame.sprite.spritecollide(self, self.coin_group, True):
            self.score += 5.3

        if pygame.sprite.spritecollide(self, self.boost_group, True):
            self.mortal = True
            self.mad = True
            self.elapsed_time = 0
            self.speed = 4
            self.height = 28
            self.spritesheet = pygame.image.load(
                "assets/player/man_brownhair_mad.png").convert_alpha()
            self.hunger = 100

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def animation(self, direction):
        frame_count = 4

        self.index += 0.1
        if self.index > frame_count:
            self.index = 0
        self.image = get_image(self.spritesheet, int(self.index), direction,
                               15, self.height, 3)
