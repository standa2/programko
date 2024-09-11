import pygame
import button
from sys import exit
from map import World

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280,800))
font = pygame.font.Font(None, 60)
font2 = pygame.font.Font(None, 40)

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

aply_img = pygame.image.load("assets/Buttons/aply.png")
resume_img = pygame.image.load("assets/Buttons/resume.png")
quit_img = pygame.image.load("assets/Buttons/quit.png")
new_game_img = pygame.image.load("assets/Buttons/new_game.png")


L_img = pygame.image.load("assets/Block_images/L.png")
J_img = pygame.image.load("assets/Block_images/J.png")
O_img = pygame.image.load("assets/Block_images/O.png")
Z_img = pygame.image.load("assets/Block_images/Z.png")
S_img = pygame.image.load("assets/Block_images/S.png")
T_img = pygame.image.load("assets/Block_images/T.png")
I_img = pygame.image.load("assets/Block_images/I.png")

score_img = pygame.image.load("assets/Texts/score.png")
top_score_img = pygame.image.load("assets/Texts/top_score.png")


start_button = button.Button(450, 620, start_img, 10)
aply_button = button.Button(870, 250, aply_img, 8)
pause_button = button.Button(70, 185, pause_img, 6)
play_button = button.Button(870, 650, play_img, 8)

up_button = button.Button(870, 230, up_img, 1)
down_button = button.Button(870, 330, down_img, 1)
left_button = button.Button(870, 430, left_img, 1)
right_button = button.Button(870, 530, right_img, 1)

resume_button = button.Button(450, 450, resume_img, 8)
quit_button = button.Button(450, 650, quit_img, 8)
new_game_button = button.Button(450, 250, new_game_img, 8)

points = 0
top_points = 0

L_points = 0
J_points = 0
S_points = 0
Z_points = 0
O_points = 0
T_points = 0
I_points = 0

game_started = True
game_choose = False
game_pause = False
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
            game_choose = True

    if game_choose == True:
        pygame.display.update()
        tutorial.draw_background()


        if aply_button.draw(screen):
            game_choose = False
            game_tutorial = True

    if game_pause == True:
        pygame.display.update()
        tutorial.draw_background()

        if resume_button.draw(screen):
            game_pause = False
            game_playing = True

        if quit_button.draw(screen):
            pygame.quit()

        if new_game_button.draw(screen):
            game_pause = False
            game_choose = True

    if game_tutorial == True:
        pygame.display.update()
        tutorial.draw_background()

        
        screen.blit(drop_img, [270, 340])
        screen.blit(rotate_img, [270, 240])
        screen.blit(move_left_img, [270, 440])
        screen.blit(move_right_img, [270, 540])

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

        screen.blit(score_img, [1015, 320])
        screen.blit(top_score_img, [980, 500])

        score = font.render(f"{points : 04d}", False, "#FFFFFF")
        top_score = font.render(f"{top_points : 04d}", False, "#FFFFFF")

        screen.blit(score, (1035 , 400))
        screen.blit(top_score, (1035 , 570))

        screen.blit(L_img, [80, 340])
        screen.blit(J_img, [80, 380])
        screen.blit(Z_img, [80, 420])
        screen.blit(S_img, [80, 460])
        screen.blit(O_img, [80, 500])
        screen.blit(T_img, [80, 540])
        screen.blit(I_img, [80, 580])

        L_score = font2.render(f"{L_points : 04d}", False, "#FFFFFF")
        J_score = font2.render(f"{J_points : 04d}", False, "#FFFFFF")
        Z_score = font2.render(f"{Z_points : 04d}", False, "#FFFFFF")
        S_score = font2.render(f"{S_points : 04d}", False, "#FFFFFF")
        O_score = font2.render(f"{O_points : 04d}", False, "#FFFFFF")
        T_score = font2.render(f"{T_points : 04d}", False, "#FFFFFF")
        I_score = font2.render(f"{I_points : 04d}", False, "#FFFFFF")

        screen.blit(L_score, (200 , 335))
        screen.blit(J_score, (200 , 375))
        screen.blit(Z_score, (200 , 415))
        screen.blit(S_score, (200 , 455))
        screen.blit(O_score, (200 , 495))
        screen.blit(T_score, (200 , 535))
        screen.blit(I_score, (200 , 575))


        if pause_button.draw(screen):
            game_pause = True
            game_playing = False

    clock.tick(60)
    