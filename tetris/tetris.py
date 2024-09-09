import pygame
import button
from sys import exit
from map import World

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,800))
font = pygame.font.Font(None, 60)

start = World("assets/Start/start.tmx", screen)
game = World("assets/Map/mapa.tmx", screen)
tutorial = World("assets/Tutorial/tutorial.tmx", screen)

start_img = pygame.image.load("assets/Buttons/start.png")
play_img = pygame.image.load("assets/Buttons/play.png")
pause_img = pygame.image.load("assets/Buttons/pause.png")


drop_img = pygame.image.load("assets/Texts/drop.png")
rotate_img = pygame.image.load("assets/Texts/rotate.png")
move_left_img = pygame.image.load("assets/Texts/left.png")
move_right_img = pygame.image.load("assets/Texts/right.png")

up_img = pygame.image.load("assets/Keys/up.png")
down_img = pygame.image.load("assets/Keys/down.png")
left_img = pygame.image.load("assets/Keys/left.png")
right_img = pygame.image.load("assets/Keys/right.png")

L_img = pygame.image.load("assets/Block_images/L.png")
J_img = pygame.image.load("assets/Block_images/J.png")
O_img = pygame.image.load("assets/Block_images/O.png")
Z_img = pygame.image.load("assets/Block_images/Z.png")
S_img = pygame.image.load("assets/Block_images/S.png")
T_img = pygame.image.load("assets/Block_images/T.png")
I_img = pygame.image.load("assets/Block_images/I.png")


start_button = button.Button(470, 625, start_img, 1)
pause_button = button.Button(70, 180, pause_img, 0.9)
play_button = button.Button(870, 650, play_img, 1)

up_button = button.Button(870, 230, up_img, 1)
down_button = button.Button(870, 330, down_img, 1)
left_button = button.Button(870, 430, left_img, 1)
right_button = button.Button(870, 530, right_img, 1)

points = 0
top_points = 0
game_started = True
game_playing = False
game_tutorial = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if game_started == True:
        pygame.display.update()
        start.draw_background()

        if start_button.draw(screen):
            game_started = False
            game_tutorial = True


    if game_tutorial == True:
        pygame.display.update()
        tutorial.draw_background()

        
        screen.blit(drop_img, [270, 330])
        screen.blit(rotate_img, [270, 230])
        screen.blit(move_left_img, [260, 430])
        screen.blit(move_right_img, [265, 530])

        if up_button.draw(screen):
            pass
        if down_button.draw(screen):
            pass
        if left_button.draw(screen):
            pass
        if right_button.draw(screen):
            pass

        if play_button.draw(screen):
            game_tutorial = False
            game_playing = True

    if game_playing == True:
        pygame.display.update()
        game.draw_background()

        score_text = font.render(f"SCORE", False, "#FFFFFF")
        top_score_text = font.render(f"TOP SCORE", False, "#FFFFFF")
        score_points = font.render(f"{points}", False, "#FFFFFF")
        top_score_points = font.render(f"{top_points}", False, "#FFFFFF")

        screen.blit(score_text, (1010 , 330))
        screen.blit(score_points, (1070 , 400))

        screen.blit(top_score_text, (960 , 500))
        screen.blit(top_score_points, (1070 , 570))

        screen.blit(L_img, [80, 340])
        screen.blit(J_img, [80, 380])
        screen.blit(Z_img, [80, 420])
        screen.blit(S_img, [80, 460])
        screen.blit(O_img, [80, 500])
        screen.blit(T_img, [80, 540])
        screen.blit(I_img, [80, 580])

        if pause_button.draw(screen):
            pass

    clock.tick(60)
    