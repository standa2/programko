import pygame
from settings import *
from utility import get_image


class Monster(pygame.sprite.Sprite):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.monstersheet = pygame.image.load(
            "assets/monster/monster_spritesheet.png").convert_alpha()
        self.image = get_image(self.monstersheet, 0, 0, 15, 16, 3)
        self.index = 0
        self.rect = self.image.get_rect(topleft=(position))
        self.direction = "Left"

    def animation(self):
        frame_count = 2
        self.index += 0.05

        if self.index >= frame_count:
            self.index = 0
        self.image = get_image(self.monstersheet, int(self.index), 4, 16, 16,
                               5)

    def update(self):
        self.animation()
        if self.rect.x <= 0:
            self.direction = "Right"
        elif self.rect.x >= screen_width - 50:
            self.direction = "Left"

        if self.direction == "Left":
            self.rect.x -= 10
        elif self.direction == "Right":
            self.rect.x += 10

    def draw(self, screen):
        screen.blit(self.image, self.rect)
