# Initalizations
import pygame
import os
from pygame import *
import random
import math

pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# backgrounds
hs_bg = pygame.image.load('barr.png')
game_bg = pygame.image.load('barr.png')
be_bg = pygame.image.load('barr.png')
mid = pygame.image.load('vdart_all.png')

# music
hit_sound = mixer.Sound('tuck_sound.wav')
hit_sound.play()
mixer.music.load('daybreak.mp3')
mixer.music.play(-1)

# title and icon
pygame.display.set_caption("V-Dart")
icon = pygame.image.load("dd.png")
pygame.display.set_icon(icon)

# player bow
playerimg = pygame.image.load("sid.a.png")
playerx = 20
playery = 250
playerx_change = 0
playery_change = 0

# target
dbimg = pygame.image.load("Dboard.png")
dbx = 577
dby = random.randint(69, 420)
dbx_change = 0
dby_change = 12
# db_w = dbimg.get_width
# db_h = dbimg.get_height
# hitbox_db = (50, 50, 50, 50)
# x, y = 0, 0
# pygame.draw.rect(screen, (255, 0, 0), hitbox_db, 2)

# bullet img
fireimg = pygame.image.load('vdart_logo.png')
firex = 150
firey = 150
firex_change = 75
firey_change = 0
fire_state = "ready"
# hitbox_fire = (320, 240, 50, 50)
# x, y = 0, 0
# pygame.draw.rect(screen, (255, 0, 0), hitbox_fire, 2)

# home screen
#hs_bg = screen.fill((225, 225, 225))
hs_font = pygame.font.SysFont('comicsansms.ttf', 64)

# score
score_value = 0
score_font = pygame.font.Font('freesansbold.ttf', 32)

# game over
go_font = pygame.font.Font('freesansbold.ttf', 69)

# replay
r_font = pygame.font.Font('freesansbold.ttf', 22)


def player(x, y):
    screen.blit(playerimg, (x, y))


def midpoint(x, y):
    return midpoint((x + y) / 2)


def db(x, y):
    screen.blit(dbimg, (x, y))


def fire_bullet(x, y):
    global fire_state
    fire_state = "fire"
    screen.blit(fireimg, (x + 0, y + 45))


# def iscollision(dbx, dby, firex, firey):
#     distance = math.sqrt((math.pow(firex - dbx, 2)) + (math.pow(firey - dby, 2)))
#     if distance < 25:
#         return True
#     else:
#         return False


# Main While Loop (MWL)
running_game = True
start = True
winning = True
bullseye = False
delay = 0

while running_game:
    # clock.tick(speed)
    # clock.tick(speed)

    # home screen
    if start:
        screen.fill((0, 0, 0))
        screen.blit(hs_bg, (0, 0))
        screen.blit(hs_font.render("VDart Digital Presents: V-Dart Game", True, (0, 0, 225)), (10, 80))
        screen.blit(hs_font.render("Your game will begin shortly", True, (255, 24, 130)), (110, 145))
        screen.blit(r_font.render("Credits to: Tarun, Abiali, Angel, and Zahra", True, (220, 220, 105)), (180, 210))
        screen.blit(mid, (300, 250))
        # screen.blit(hs_font.render("Press Spacebar to Start", True, (255, 24, 130)), (150, 400))
        screen.blit(r_font.render("Objective: Hit the bullseye and prove you are a true VDartian", True, (225, 100, 100)), (66, 480))
        screen.blit(r_font.render("Controls: up arrow to travel up and down arrow to travel down", True, (225, 100, 100)), (60, 520))
        pygame.display.update()
        while delay < 500000:
            delay += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running_game = False
                    pygame.quit()
                    quit()
        start = False
        winning = True

    # checks if the game has be exited
    if winning:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            # exit button check
            if event.type == pygame.QUIT:
                running_game = False
                pygame.quit()
                quit()
        screen.fill((0, 0, 0))
        screen.blit(game_bg, (0, 0))

        # if keystroke is been pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                playery_change = -15
            if event.key == pygame.K_DOWN:
                playery_change = 15
            if event.key == pygame.K_SPACE:
                playery_change = 0
                if fire_state == "ready":
                    firey = playery
                    fire_bullet(firex, firey)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    playery_change = 0
            playery += playery_change

        # boundaries of player bow
        if playery <= 10:
            playery = 10
        elif playery >= 390:
            playery = 390

        # boundaries of db
        if dby <= -5:
            dby_change = 12
        elif dby >= 350:
            dby_change = -12
        dby += dby_change
        player(playerx, playery)
        db(dbx, dby)

        if firex >= 800:
            firex = 150
            firey = 150
            fire_state = "ready"

        if fire_state == "fire":
        # fire_bullet(firex, firey)
        # firex -= firex_change
        # collision = iscollision(dbx, dby, firex, firey)
            #print(dbx, firey)
            # print(firex, dby)
            # print((firex + firey) / 2)
            # print((dbx + dby) / 2)
            # x, y = event.pos
            # firex.cen = event.pos
            # collid_img = firex.collidrect(hitbox_db)
            if (firey >= dby) and (firey <= dby + 80) and (firex >= dbx + 63): # need to fix this condition to hit only bullseye/ create hitbox for center of vdart logo
                hit_sound = mixer.Sound('tuck_sound.wav')
                hit_sound.play()
                bullseye = True
                # if ((firey >= dby) and (firey <= dby + 50)) and ((firex >= dbx) and (firex < dbx+100)):
                # if midpoint(firex, firey) >= midpoint(dbx, dby):
                # if ((firex+firey)/2 + 100 >= (dbx+dby)/2) and ((firex+firey)/2 + 100 <= (dbx+dby)/2)
                # elif ((firey >= dby and (firey) <= (dby + 200)) and (firex >= dbx + 40)): # This condition only if arrow hits outer ring of bullseye
                #     out_ring = True
            # elif (firex > dbx) and (firey > dby): # This condition true if arrow misses the board completely
            #     game_over = True
                for i in range(1):
                    firex = 800
                    firey = 600
            fire_bullet(firex, firey)
            firex += firex_change
        pygame.display.update()

    # exit button check
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_game = False
            pygame.quit()
            quit()

    # game over page
    while bullseye:
        screen.fill((192, 192, 192))
        screen.blit(be_bg, (1, 0))
        screen.blit(go_font.render("BULLSEYE!", True, (255, 0, 0)), (205, 200))
        # print_score = score_font.render("Score: " + str(score * 10), True, (255, 100, 100))
        # screen.blit(print_score, (325, 275))
        Next = pygame.key.get_pressed()
        print_next = r_font.render("PRESS R TO RETRY", True, (255, 255, 255))
        screen.blit(print_next, (290, 300))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_game = False
                pygame.quit()
                quit()

    # while game_over:
    #     screen.fill((192, 192, 192))
    #     # screen.blit(go_bg, (0, 0))
    #     screen.blit(go_font.render("GAME OVER!", True, (255, 0, 0)), (205, 200))
    #     # print_score = score_font.render("Score: " + str(score * 10), True, (255, 100, 100))
    #     # screen.blit(print_score, (325, 275))
    #     Next = pygame.key.get_pressed()
    #     print_next = r_font.render("PRESS R TO RETRY", True, (255, 255, 255))
    #     screen.blit(print_next, (290, 300))
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running_game = False
    #             pygame.quit()
    #             quit

        # Restarting V-Dodge
        if Next[pygame.K_r]:
            winning = True
            score = 0
            playerX = 80
            playerY = 300
            num_asteroid = 3
            game_over = False
            bullseye = False

        pygame.display.update()
