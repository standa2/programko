from typing import Any
import pygame
import button
from sys import exit
from settings import *
from world import World
from monster import Monster
from player import Player

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

font1 = pygame.font.Font(None, 25)
font2 = pygame.font.Font(None, 100)

player = pygame.sprite.GroupSingle()
monsters = pygame.sprite.Group()

desk_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
boost_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


sprite_groups = {
    "all": all_sprites,
    "player_group": player,
    "monsters_group": monsters,
    "desk_group": desk_group,
    "coin_group": coin_group,
    "boost_group": boost_group,
}
key = pygame.key.get_pressed()
world = World("tiled/ucebna-final.tmx", screen, sprite_groups)

paused_img = pygame.image.load("assets/objects/paused.png")
resume_img = pygame.image.load("assets/objects/resume.png")
quit_img = pygame.image.load("assets/objects/quit.png")

resume_button = button.Button(540, 300, resume_img, 1)
paused_button = button.Button(440, 100, paused_img, 2)
quit_button = button.Button(540, 400, quit_img, 1)


killer = False
game_paused = False
game_over = False
win = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_paused = True
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_paused == True:
        pygame.display.update()
        pygame.draw.rect(screen, "white", (400, 60, 482, 500))

        if resume_button.draw(screen):
            game_paused = False
        if quit_button.draw(screen):
            pygame.quit()
        if paused_button.draw(screen):
                pass

    else:
        if game_over == False:
            screen.fill((255, 255, 255))
            world.draw_background()
            
            text1 = font1.render(f"Health", False, "#000000")
            text2 = font1.render(f"Hunger", False, "#000000")
            text3 = font1.render(f"Monsters HP", False, "#000000")



            pygame.draw.rect(screen, "red", (540, 50, 200, 20))
            pygame.draw.rect(screen, "brown", (540, 50, 2 * player.sprite.hunger, 20))

            pygame.draw.rect(screen, "red", (540, 20, 200, 20))
            pygame.draw.rect(screen, "green", (540, 20, 2 * player.sprite.health, 20))

            pygame.draw.rect(screen, "red", (540, 690, 200, 20))
            pygame.draw.rect(screen, "green", (540, 690, 2 * player.sprite.monster, 20))

            pygame.draw.rect(screen, "black", (1240, 260, 20, 200))
            pygame.draw.rect(screen, "gold", (1240, 260, 20, 2 * player.sprite.score))

            screen.blit(text1, (480, 20))
            screen.blit(text2, (480, 50))
            screen.blit(text3, (590, 690))



            monsters.update()
            player.update()
            all_sprites.draw(screen)

            player.sprite.elapsed_time += clock.get_time()
            player.sprite.starve_time += clock.get_time()


            if player.sprite.health <= 0:
                game_over = True
            
            if player.sprite.score >= 100:
                win = True
                player.sprite.health = 100

            if player.sprite.monster <= 0:
                killer = True
            



        elif game_over == True:
            screen.fill((0, 0, 0))
            title = font2.render(f"GAME OVER", False, "#FFFFFF")
            screen.blit(title, (400 , 310))
            if player.sprite.starve_time > 1000:
                player.sprite.hunger += 5
                player.sprite.starve_time = 0

        if win == True:
            screen.fill((0, 0, 0))
            title = font2.render(f"YOU WIN", False, "#FFFFFF")
            screen.blit(title, (500 , 320))
            if player.sprite.starve_time > 1000:
                player.sprite.hunger += 5
                player.sprite.starve_time = 0

        if player.sprite.starved == True :
            screen.fill((0, 0, 0))
            title = font2.render(f"YOU STARVED", False, "#FFFFFF")
            screen.blit(title, (400 , 320))

        if killer == True:
            screen.fill((0, 0, 0))
            title = font2.render(f"KILLED THEM ALL", False, "#FFFFFF")
            screen.blit(title, (350 , 320))
            if player.sprite.starve_time > 1000:
                player.sprite.hunger += 5
                player.sprite.starve_time = 0

        


        pygame.display.update()

        clock.tick(60)