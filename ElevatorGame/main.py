#from random
import random
from turtledemo.nim import SCREENWIDTH, SCREENHEIGHT

import pygame
import self
from pygame import mixer, KEYDOWN

#Initialize the game
pygame.init()

#create screen
SCREENWIDTH = 900
SCREENHEIGHT = int(SCREENWIDTH * 0.8)
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))



#Title
pygame.display.set_caption("Elevator game")

#STATE
state = 0

#Text
font = pygame.font.Font('freesansbold.ttf', 32)
fontSmaller = pygame.font.Font('freesansbold.ttf', 24)

#Sounds
clicked_sound = mixer.Sound('mouse-click-sound-233951.mp3')


#Buttons
one_player_game = pygame.Rect((0, 250, SCREENWIDTH, 50))
button1txt = font.render("START GAME" ,True,(0,0,0))

help_button = pygame.Rect((0, 350, SCREENWIDTH, 50))
helptxt = font.render("HOW TO PLAY" ,True,(0,0,0))
helpInfo1 = fontSmaller.render("- instructions",True,(0,0,0))

options = pygame.Rect((0, 450, SCREENWIDTH, 50))
optionstxt = font.render("OPTIONS" ,True,(0,0,0))
optInfo1 = fontSmaller.render("Game options: ",True,(0,0,0))


credits = pygame.Rect((0, 550, SCREENWIDTH, 50))
credtxt = font.render("CREDITS" ,True,(0,0,0))
credInfo1 = fontSmaller.render("Created By: ",True,(0,0,0))
credInfo2 = fontSmaller.render("Artwork By: ",True,(0,0,0))
credInfo3 = fontSmaller.render("Programming By: ",True,(0,0,0))
credInfo4 = fontSmaller.render("Music & Sounds By: ",True,(0,0,0))
credInfo5 = fontSmaller.render("Project Created: ",True,(0,0,0))


back = pygame.Rect((0, SCREENHEIGHT - 100, SCREENWIDTH, 50))
backtxt = font.render("BACK" ,True,(0,0,0))

quit_button = pygame.Rect((SCREENWIDTH - 110, 10, 100, 50))
quittxt = font.render("QUIT" ,True,(0,0,0))

#Player
move_speed = 1.1
playerX = SCREENWIDTH/9
playerY = SCREENHEIGHT - 60
player = pygame.Rect((105, SCREENHEIGHT - 60, 50, 50))
playerImg = pygame.image.load('Images/character.png')
playerImg = pygame.transform.scale(playerImg,(50,50))
playerLocked = False

#lives
#lives = 0


#Enemy?

#enemy = pygame.Rect((400, SCREENHEIGHT - 210, 50, 50))
enemySpeed = 0.5
enemyX = 400
enemyY = SCREENHEIGHT - 210
enemyImg = pygame.image.load('Images/ghost.png')
enemyImg = pygame.transform.scale(enemyImg,(50,50))
enemydir = "left"

#Elevators/stairs/ladders
elevatorImg = pygame.image.load('Images/elevator.webp')
elevatorImg = pygame.transform.scale(elevatorImg,(100,130))
ladderImg = pygame.image.load('Images/ladder.png')
ladderImg = pygame.transform.scale(ladderImg,(100,150))
elevator1X = random.randint(SCREENWIDTH - 595, SCREENWIDTH - 125)
ladder1X = random.randint(SCREENWIDTH - 595, SCREENWIDTH - 125)
elevator1 = pygame.Rect((elevator1X, SCREENHEIGHT - 135, 100, 130))
elevator2= pygame.Rect((elevator1X, SCREENHEIGHT - 285, 100, 130))
floor1wp = pygame.Rect((0, SCREENHEIGHT - 150, SCREENWIDTH, 150))


# Rooms
currentRoom = 1
enemyRoom = 1

                               #### RUNNING CODE STARTS HERE ####

run = True
while run:

    mouse_pos = pygame.mouse.get_pos()

    if state == 0: #main menu
        lives = 3
        currentRoom = 1
        playerX = SCREENWIDTH / 9
        playerY = SCREENHEIGHT - 60
        screen.fill((0, 0, 255))  # screen resets each time
        pygame.draw.rect(screen, (255, 0, 0), one_player_game)
        screen.blit(button1txt, (15, 260))
        #pygame.draw.rect(screen, (0, 255, 255), two_player_game)
        #screen.blit(button2txt, (15, 260))
        pygame.draw.rect(screen, (0, 255, 0), help_button)
        screen.blit(helptxt, (15, 360))
        pygame.draw.rect(screen, (255, 255, 0), options)
        screen.blit(optionstxt, (15, 460))
        pygame.draw.rect(screen, (128, 0, 255), credits)
        screen.blit(credtxt, (15, 560))



        if one_player_game.collidepoint(mouse_pos):
            #one_player_game.Color(100,0,0)
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 1
                p2_is_human = False



        if help_button.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 2

        if options.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 3

        if credits.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 4

    elif state == 1: #The game
        #Load everything
        screen.fill((200, 200, 255))
        pygame.draw.rect(screen, (70, 0, 70), quit_button)
        screen.blit(quittxt, (SCREENWIDTH - 100, 20))
        pygame.draw.line(screen, (0,0,0), (0, SCREENHEIGHT - 150), (SCREENWIDTH, SCREENHEIGHT - 150), 5)
        pygame.draw.line(screen, (0, 0, 0), (0, SCREENHEIGHT - 300), (SCREENWIDTH, SCREENHEIGHT - 300), 5)
        pygame.draw.line(screen, (0, 0, 0), (0, SCREENHEIGHT - 450), (SCREENWIDTH, SCREENHEIGHT - 450), 5)
        pygame.draw.line(screen, (0, 0, 0), (0, SCREENHEIGHT - 600), (SCREENWIDTH, SCREENHEIGHT - 600), 5)

        pygame.draw.rect(screen,(255,150,150),floor1wp)

        #print total lives
        #print(lives)

        #Room 1

        if currentRoom == 1:
            # draw the elevators/stairs
            screen.blit(elevatorImg,(elevator1X, elevator1.y))
            screen.blit(elevatorImg, (elevator1X, elevator2.y))
            if enemyRoom == 1:
                screen.blit(enemyImg, (enemyX, enemyY))
                #pygame.draw.rect(screen, (255, 120, 0), enemy)

        elif currentRoom == 2:
            screen.blit(ladderImg, (ladder1X, SCREENHEIGHT-300))
            screen.blit(ladderImg, (ladder1X, SCREENHEIGHT - 450))
            if enemyRoom == 2:
                screen.blit(enemyImg, (enemyX, enemyY))
                #pygame.draw.rect(screen, (255, 120, 0), enemy)

        # draw the player
        #pygame.draw.rect(screen, (0, 255, 0), player)
        screen.blit(playerImg,(playerX,playerY))

        # Player  Movement
        key = pygame.key.get_pressed()


        if not playerLocked:
            if key[pygame.K_a] | key[pygame.K_LEFT] == True:
                playerX -= 1
            elif key[pygame.K_d] | key[pygame.K_RIGHT] == True:
                playerX += 1
        #elif key[pygame.K_w] | key[pygame.K_UP] == True:
            #player.move_ip(0, -1)
        #elif key[pygame.K_s] | key[pygame.K_DOWN] == True:
            #player.move_ip(0, 1)

        # Enemy movement
        if enemydir == "left":
            enemyX -= enemySpeed
        elif enemydir == "right":
            enemyX += enemySpeed

        if (enemyX > SCREENWIDTH - 60) & (enemyRoom == 1):
            enemyRoom = 2
            enemyX = 10
        elif (enemyX < 10) & (enemyRoom == 1):
            enemyX = 10
            enemydir = "right"
        elif (enemyX > SCREENWIDTH - 60) & (enemyRoom == 2):
            enemyX = SCREENWIDTH - 60
            enemydir = "left"
        elif (enemyX < 10) & (enemyRoom == 2):
            enemyRoom = 1
            enemyX = SCREENWIDTH - 60

        #enemy switching floors
        if ((enemyX > elevator1X + 10) & (enemyX < elevator1X + 60)) & ((enemyY == SCREENHEIGHT - 60) & (currentRoom == 1)):
            #enemySpeed = 0
            enemyY = elevator2.y + 75
           # enemySpeed = 1
        elif ((enemyX > elevator1X + 10) & (enemyX < elevator1X + 60)) & ((enemyY == SCREENHEIGHT - 210) & (currentRoom == 1)):
            #enemySpeed = 0
            enemyY = elevator1.y + 75
            #enemySpeed = 1
        elif ((enemyX> ladder1X + 10) & (enemyX < ladder1X + 60)) & ((enemyY == SCREENHEIGHT - 210) & (currentRoom == 2)):
            enemyY = elevator2.y - 75
            #enemydir = random.Random("left" "right")
        elif ((enemyX > ladder1X + 10) & (enemyX < ladder1X + 60)) & ((enemyY == SCREENHEIGHT - 360) & (currentRoom == 2)):
            enemyY = elevator2.y + 75



        #print(elevator2.x, " ", elevator2.y)
        # traversing floors
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if ((playerX > elevator1X + 10) & (playerX < elevator1X + 60)) & ((playerY == SCREENHEIGHT - 60) & (currentRoom == 1)):
                        playerY = elevator2.y + 75
                    elif ((playerX > elevator1X + 10) & (playerX < elevator1X + 60)) & ((playerY == SCREENHEIGHT - 210) & (currentRoom == 1)):
                        playerY = elevator1.y + 75
                    elif ((playerX > ladder1X + 10) & (playerX < ladder1X + 60)) & ((playerY == SCREENHEIGHT - 210) & (currentRoom == 2)):
                        playerY = elevator2.y - 75
                if event.key == pygame.K_DOWN:
                    if ((playerX > ladder1X + 10) & (playerX < ladder1X + 60)) & ((playerY == SCREENHEIGHT - 360) & (currentRoom == 2)):
                        playerY = elevator2.y + 75
                if event.key == pygame.K_SPACE:
                    print(playerY, " ", ladder1X, " ", playerX)



        #if (key[pygame.K_w] | key[pygame.K_UP] == True) & (playerX >= elevator2.x ):
            #playerY = elevator1.y + 75
            #playerLocked





        # Move between rooms
        if (playerX > SCREENWIDTH - 60) & (currentRoom == 1):
            playerX = 10
            currentRoom = 2
        elif (playerX < 10) & (currentRoom == 2):
            playerX = SCREENWIDTH - 60
            currentRoom = 1
        elif (playerX < 10) & (currentRoom == 1):
            playerX = 10
        elif (playerX > SCREENWIDTH - 60) & (currentRoom == 2):
            playerX = SCREENWIDTH - 60


        #Collision detection
        if ((playerX == enemyX) & (playerY == enemyY)) & (currentRoom == enemyRoom):
            lives -= 1
            print(lives)
        if lives == 0:
            state = 0




        #Return to menu if quit button is pressed
        if quit_button.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 0

    elif state == 2: #how to play
        screen.fill((70, 150, 0))
        pygame.draw.rect(screen, (255, 255, 255), back)
        screen.blit(backtxt, (15, SCREENHEIGHT - 95))
        screen.blit(helpInfo1, (15, 100))

        if back.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 0

    elif state == 3: #options
        screen.fill((70, 70, 70))
        pygame.draw.rect(screen, (255, 255, 255), back)
        screen.blit(backtxt, (15, SCREENHEIGHT - 95))
        screen.blit(optInfo1, (15, 100))


        if back.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 0

    elif state == 4: #credits
        screen.fill((150, 70, 0))
        pygame.draw.rect(screen, (255, 255, 255), back)
        screen.blit(backtxt, (15, SCREENHEIGHT - 95))
        screen.blit(credInfo1, (15, 100))

        if back.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                clicked_sound.play()
                state = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()
