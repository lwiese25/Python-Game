"""
Authors: Luke Wiese & Brendan Lavarra
Date: 11/17/2022

Description: This is a game made in pygame by Luke Wiese. This 
is a racing game controlled by arrow keys. Every car you dodge gets +1 added to your overall score.
The goal of the game is to achieve the highest score you can by surviving the longest you can.
Hitting the cars ends the game.

Code of honesty: I have neither given nor received unauthorized aid in completing this assignment.
"""
# Distance Formula: https://www.w3schools.com/python/ref_math_dist.asp 
# Importing pygame
import pygame as pg 
from time import sleep
from random import randint
import math as m
#Initializing Pygame
pg.init()
# Setting screen height and width as constants
HEIGHT = 550
WIDTH= 800
# Displaying the screen
screen = pg.display.set_mode((WIDTH,HEIGHT))
pg.mixer.init()
pg.display.set_caption("Hazerdous Highway")
# Setting font for menu text
intro_font = pg.font.Font(None, 50)
title_font = pg.font.Font(None, 80)
instruction_font = pg.font.Font(None, 45)
def play(x,y):

    # Displaying all of the images, sounds, and text on the menu screen
    menu_background  = pg.image.load("Hazerdous Highway/asphaltBG.jpg")
    menu_background= pg.transform.scale(menu_background,(WIDTH, HEIGHT))
    playtext = intro_font.render("PLAY",True,(46,173,17))
    title_text = title_font.render("Hazerdous Highway",True,(252, 186, 3))
    instruction_text1 = instruction_font.render("Use the arrow keys to move!", True,(212, 22, 8))
    instriction_text2 = instruction_font.render("Avoid the cars!", True, (250,127,5))
    screen.blit(menu_background,(0,0))
    screen.blit (playtext,(x,y))
    screen.blit(title_text,(125, 50))
    screen.blit(instruction_text1,(190, 300))
    screen.blit(instriction_text2,(280, 355))

# Setting up the main function
def main():
    running = True
    pg.mixer.music.load("Hazerdous Highway/menu_music.mp3")
    pg.mixer.music.play()
    while running :
        # Setting up where play button is
        screen.fill((0,0,0))
        play(350,410)
        # Getting mouse position in order to click the play button
        x,y = pg.mouse.get_pos()
        # When mouse hovers over rect, rect is highlighted
        play_button = pg.Rect(300,WIDTH//2,180,50)
        pg.draw.rect(screen, (255,255,255), play_button,5)
        if play_button.collidepoint(x,y): 
            pg.draw.rect(screen, (46,173,17), play_button,5)
            if click:
                countdown()
        click = False
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            pg.display.update()

# Countdown before the game starts
def countdown():
    # Number font
    countdown_font = pg.font.Font(None, 90)
    # Loading background in
    countdownBackground = pg.image.load("Hazerdous Highway/gameplay_bg.png")
    countdownBackground = pg.transform.scale(countdownBackground,(WIDTH, HEIGHT))
    three = countdown_font.render("3",True, (212, 22, 8))
    two = countdown_font.render("2",True, (250,127,5))
    one = countdown_font.render("1",True, (11, 143, 4))
    go = countdown_font.render("GO!",True, (255,255,255))
    # Playing countdown music
    pg.mixer.music.load("Hazerdous Highway/Countdown.mp3")
    pg.mixer.music.play()
    screen.blit(countdownBackground, (0,0))
    pg.display.update()

# Dislplaying 3
    screen.blit(three,(350,250))
    pg.display.update()
    # Sleep is called to stop the program for 1.1 seconds in between numbers
    sleep(1.1)
# Blank bg in between numbers
    screen.blit(countdownBackground, (0,0))
    pg.display.update()
# Displaying 2
    screen.blit(two,(350,250))
    pg.display.update()
    sleep(1.1)
# Blank bg in between numbers
    screen.blit(countdownBackground, (0,0))
    pg.display.update()

# Displaying 1
    screen.blit(one,(350,250))
    pg.display.update()
    sleep(1.1)
    screen.blit(countdownBackground, (0,0))
    pg.display.update()

# Displaying "GO!"
    screen.blit(go,(300,250))
    pg.display.update()
    sleep(1)
    gameplay() #calling gameplay so game starts after countdown
    pg.display.update()

# Setting uo gameplay function
def gameplay():
    # Loading in the music for the gameplay
    pg.mixer.music.load("Hazerdous Highway/racing_music.mp3")
    pg.mixer.music.play()
    
    # Car crash sound when crash happens
    crash_sound = pg.mixer.Sound("Hazerdous Highway/carcrash.mp3")
    # Initializing score
    score_value = 0
    score_font= pg.font.Font(None,50)
    # Showing score
    def show_score(x,y):
        score = score_font.render("SCORE: "+ str(score_value), True, (0,255,0))
        screen.blit(score, (x,y))
    # Setting up game over function
    def gameover():
        # Gameover music is loaded in
        pg.mixer.music.load("Hazerdous Highway/gameover_audio.mp3")
        pg.mixer.music.play()
        # Setting up game over page background
        gameover  = pg.image.load("Hazerdous Highway/asphaltBG.jpg")
        gameover = pg.transform.scale(gameover,(WIDTH, HEIGHT))
        running = True
        while running:
            # Blitting the text and background to the gameover screen
            screen.blit(gameover,(0,0))
            gameover = pg.transform.scale(gameover,(WIDTH, HEIGHT))
            gameover_font = pg.font.Font(None, 100)
            gameover_text = gameover_font.render("Game Over",True,(255,0,0))
            playagain_font = pg.font.Font(None, 50)
            playagain_text = playagain_font.render("Press ""Space"" to Play Again", True, (252,186,3))
            author_font = pg.font.Font(None, 35)
            author_text = author_font.render("By: Luke Wiese and Brendan Lavarra", True, (0,93,252))

            screen.blit(gameover_text,(200, 200))
            screen.blit(playagain_text, (180, 400))
            screen.blit(author_text, (0, HEIGHT-35))
            sleep(0.25)
            show_score(400,550)
            sleep(0.25)

            pg.display.update()
            # Event handling
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                    pg.quit()
                # Setting up a spacebar option to play again
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        countdown()
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
    # Making the image fit the screen
    bg = pg.image.load("Hazerdous Highway/gameplay_bg.png")
    bg = pg.transform.scale(bg, (WIDTH,HEIGHT))
    # Setting up the car positions during gameover
    player_car = pg.image.load("Hazerdous Highway/player_car.png")
    player_carX = 350
    player_carY = 495
    player_carx_change = 0
    player_carY_change = 0
    # Where to send each car during start of gameplay
    car1 = pg.image.load("Hazerdous Highway/car1.png")
    # Randominzing where the cars spawn in from during each pass through
    car1X = randint(125,325)
    car1Y = HEIGHT
    # Randomizing the speed at which the cars go for each pass through
    car1Yspeed = randint(4,7)
    car2 = pg.image.load("Hazerdous Highway/car2.png")
    car2X = randint(125,325)
    car2Y = HEIGHT
    car2Yspeed = randint(4,7)

    car3 = pg.image.load("Hazerdous Highway/car3.png")
    car3X = randint(125,325)
    car3Y = HEIGHT
    car3Yspeed = randint(4,7)
    # Quitting event
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                pg.quit()
            # Movement of the player_car (Up, Down, Left, Right) when key is pressed down
            if event.type == pg.KEYDOWN: 
                if event.key == pg.K_UP:
                    player_carY_change -= 5
                if event.key == pg.K_DOWN:
                    player_carY_change += 5
                if event.key == pg.K_LEFT:
                    player_carx_change -= 5
                if event.key == pg.K_RIGHT:
                    player_carx_change += 5
            # When key is lifted up car stops moving
            if event.type == pg.KEYUP: 
                if event.key == pg.K_RIGHT:
                    player_carx_change = 0
                if event.key == pg.K_LEFT:
                    player_carx_change = 0
                if event.key == pg.K_UP:
                    player_carY_change = 0
                if event.key == pg.K_DOWN:
                    player_carY_change = 0            

        # Setting the play area for the player_car
        if player_carX < 130:
            player_carX = 130
        if player_carX > 395:
            player_carX = 395
        
        if player_carY < 0:
            player_carY = 0
        if player_carY > 495:
            player_carY = 495


        # Displaying the background image between car movements to update the background above previous car blits
        screen.blit(bg,(0,0))

        # Displaying the player_car
        screen.blit(player_car,(player_carX,player_carY))

        # Displaying the other cars on the gameplay screen
        screen.blit(car1,(car1X,car1Y))
        screen.blit(car2,(car2X,car2Y))
        screen.blit(car3,(car3X,car3Y))
        show_score(520,260)

        player_carX += player_carx_change
        player_carY += player_carY_change

        car1Y += car1Yspeed
        car2Y += car2Yspeed
        car3Y += car3Yspeed
        # Moving the cars back to the top of the screen after they have gone past the screen boundary
        if car1Y > HEIGHT:
            car1Y = -80
            car1X = randint(130,370)
            car1Yspeed = randint(4,7)
            score_value += 1
        if car2Y > HEIGHT:
            car2Y = -80
            car2X = randint(130,370)
            car2Yspeed = randint(4,7)
            score_value += 1
        if car3Y > HEIGHT:
            car3Y = -80
            car3X = randint(130,370)
            car3Yspeed = randint(4,7)
            score_value += 1

        # Setting up crash function
        def crash(car1X,car1Y,player_carX,player_carY):
            # If the distance between the player car and the other cars is < 45 (half the length the car and about the width of the car)
            # each car is approximatley 90 pixels long and 45 wide meaning we need to create a 45x45 box to detect collision
            # Using the distance formula d = \sqrt{(x_2 - x_1)^2 + (y_2-y_1)^2} we can check if the cars have collided within the 45x45 box
            distance = m.sqrt(m.pow(car1X-player_carX,2) + m.pow(car1Y - player_carY,2)) 
            if distance < 45: 
                return True
            else:
                return False
        def crash(car2X,car2Y,player_carX,player_carY):
            distance = m.sqrt(m.pow(car2X-player_carX,2) + m.pow(car2Y - player_carY,2))
            if distance < 45:
                return True
            else:
                return False
        def crash(car3X,car3Y,player_carX,player_carY):
            distance = m.sqrt(m.pow(car3X-player_carX,2) + m.pow(car3Y - player_carY,2))

            if distance < 45:
                return True
            else:
                return False
        crash_car1 = crash(car1X,car1Y,player_carX,player_carY) 
        crash_car2 = crash(car2X,car2Y,player_carX,player_carY) 
        crash_car3 = crash(car3X,car3Y,player_carX,player_carY) 
        # If crash happens all cars come to a halt and the gameover function is called
        if crash_car1:
    
            car1Yspeed = 0
            car1Y = 0
            player_carx_change = 0
            player_carY_change = 0
            pg.mixer.music.stop()
            crash_sound.play()
            sleep(0.5)
            gameover()
        if crash_car2:
            car2Yspeed = 0
            car2Y = 0
            player_carx_change = 0
            player_carY_change = 0
            pg.mixer.music.stop()
            crash_sound.play()
            sleep(0.5)
            gameover()

        if crash_car3:
            car3Yspeed = 0
            car3Y = 0
            player_carx_change = 0
            player_carY_change = 0
            pg.mixer.music.stop()
            crash_sound.play()

            sleep(0.5)
            gameover()

        pg.display.update()
main()
