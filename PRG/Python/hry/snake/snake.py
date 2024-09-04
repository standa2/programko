#importy
from sys import exit
import pygame
import random

pygame.init()

clock = pygame.time.Clock()

#okno
screen_height = 600
screen_width = 800
screen = pygame.display.set_mode((screen_width, screen_height))

#snake
snake_x = 100
snake_y = 200
snake_surf = pygame.image.load("C:\\Users\\jakub\\OneDrive\\Plocha\\prg\\snake\\pixelsnake.png").convert_alpha()
snake_rect = snake_surf.get_rect(midbottom=(snake_x, snake_y))

#jablko
apple_x = random.randrange(10, 550)
apple_y = random.randrange(10, 750)
apple_surf = pygame.image.load("C:\\Users\\jakub\\OneDrive\\Plocha\\prg\\snake\\apple.png").convert_alpha()
apple_rect = apple_surf.get_rect(midbottom=(apple_x, apple_y))


points = 0

font = pygame.font.Font(None, 25)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    key = pygame.key.get_pressed()

#pohyb
    if key[pygame.K_LEFT]:
        snake_rect.left -= 10
    elif key[pygame.K_RIGHT]:
        snake_rect.right += 10
    elif key[pygame.K_UP]:
        snake_rect.top -= 10
    elif key[pygame.K_DOWN]:
        snake_rect.bottom += 10

    screen.fill((255, 255, 255))
    text = font.render(f"POINTS: {points}", False, "#000000")
    screen.blit(text, (700, 10))

#jablko vs snake
    if snake_rect.colliderect(apple_rect):
      points += 1
      apple_x = random.randrange(10, 550)
      apple_y = random.randrange(10, 750)
      apple_rect.topleft = (apple_x, apple_y)

  
      
    screen.blit(snake_surf, snake_rect)
    screen.blit(apple_surf, apple_rect)


    pygame.display.update()

    clock.tick(60)