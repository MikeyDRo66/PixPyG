import sys
import pygame
import CharacterClass
import threading
import timer
import pyganim
import hudFunctions
import time

# initalize pygame istance
pygame.init()

# local variables
size = width, height = 1000, 600
global GameState 
GameState = "Menu"
speed = [2, 2]
black = 0, 0, 0

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

screen = pygame.display.set_mode(size)

ballX = 250.0
ballY = 250.0

timeStr = '0'

totalTime = 60
timeToEnd = totalTime
timePaused = 0
pausedTimeStart = 0
totalTimePaused = 0

# initalize players
dogo = CharacterClass.playerOBJ('Doge', "dogo.png", False)
bitCoin = CharacterClass.playerOBJ('Bitcoin', "bitcoin.png", False)

# create button

pauseButton = hudFunctions.button('Pause',(900,50),(100,50),'freesansbold.ttf', 32,white,blue,lambda:hudFunctions.pauseGame())

startButton = hudFunctions.button('Game Start',(500,300),(200,70),'freesansbold.ttf', 32,white,black,lambda:ChangeGameState(GameState,))

SinglePlayerButton = hudFunctions.button('Single Player',(700,300),(100,50),'freesansbold.ttf', 32,white,blue,lambda:ChangeGameState(GameState,dogo,bitCoin,'Single Player'))
TwoPlayerButton = hudFunctions.button('Two Player',(300,300),(100,50),'freesansbold.ttf', 32,white,blue,lambda:ChangeGameState(GameState,dogo,bitCoin,'Two Player'))
print(SinglePlayerButton.Coordinates)



#store player rectangles (coordinates) in local variables. temp vars
ballRect = dogo.Rect
ball2Rect = bitCoin.Rect
ball2Rect.x = 50
ball2Rect.y = 50

# initalize font
font = pygame.font.Font('freesansbold.ttf', 32)
Menufont2 = pygame.font.Font('freesansbold.ttf',60)

#set player as Tagged
dogo.Tagged = True



text = font.render('Dogo is It', True, green, blue)
timeText = font.render('Time left | ' + timeStr, True, green, blue)

GameName = Menufont2.render("Tagger", True, white, black)

#create a rectangular object for the
# I text surface object

textRect = text.get_rect()

textRect.center = (500, 50)

timeRect = timeText.get_rect()
timeRect.center = (500, 100)

GameNameRect = GameName.get_rect()
GameNameRect.center = (500,100)

# get start time
startTime = time.perf_counter()

while 1:

    mouse = pygame.mouse.get_pos()

    key_input = pygame.key.get_pressed()
            
    if GameState == "Play":

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            #checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
            
                pauseButton.onClick(mouse)


        
        pauseButton.isOver(mouse)
        # Keyboard controlls for "dogo"
        dogo.control(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, key_input, hudFunctions.PAUSE_FLAG, bitCoin)
        
        # Keyboard controlls for "Bitcoin"
        bitCoin.control(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, key_input, hudFunctions.PAUSE_FLAG, dogo)
        
        # Setting screen boundaries for dogo
        if ballRect.x >= width - 50:
            ballRect.x = width - 50 
        
        if ballRect.x <= 0:
            ballRect.x = 0

        if ballRect.y >= height - 50:
            ballRect.y = height - 50

        if ballRect.y <= 0:
            ballRect.y = 0
        
        ## Setting screen boundaries for bitcoin
        if ball2Rect.x >= width - 50:
            ball2Rect.x = width - 50 
        
        if ball2Rect.x <= 0:
            ball2Rect.x = 0

        if ball2Rect.y >= height - 50:
            ball2Rect.y = height - 50

        if ball2Rect.y <= 0:
            ball2Rect.y = 0

        # Hit boxes for Dogo and Bitcoin
        if ballRect.x >= ball2Rect.x and ballRect.x <= ball2Rect.x + 50 and ballRect.x + 50 >= ball2Rect.x and ballRect.x + 50 >= ball2Rect.x + 50 and ballRect.y >= ball2Rect.y and ballRect.y <= ball2Rect.y + 50 and ballRect.y + 50 >= ball2Rect.y and ballRect.y + 50 >= ball2Rect.y + 50:
            
            if dogo.paused == False and bitCoin.paused == False: 
                
                bitCoin.tagged(hudFunctions.PAUSE_FLAG)  
        
                dogo.tagged(hudFunctions.PAUSE_FLAG)
                
                


            
            # Who is tagged text
            if bitCoin.Tagged:

                text = font.render('Coin is It', True, green, blue)


            if dogo.Tagged:

                text = font.render('dogo is It', True, green, blue)

        
        timeText = font.render('Time left | ' + timeStr, True, green, blue)

        # Who won text
        if(timeToEnd == 0):

            if bitCoin.Tagged:

                text = font.render('Dogo Wins!', True, green, blue)
                


            if dogo.Tagged:

                text = font.render('Coin Wins!', True, green, blue)
            
            hudFunctions.PAUSE_FLAG = True
                

        # increment timer
        currentTime = time.perf_counter()

        

    

        if hudFunctions.PAUSE_FLAG:

            startTime = currentTime
            totalTime = timeToEnd
            pauseButton.Text = "play"

        else:
            pausedTimeStart = 0
            totalTimePaused += timePaused
            timeToEnd = totalTime - timer.countDown(startTime, currentTime) 
            timeStr = str(timeToEnd)
            pauseButton.Text = "pause"

        screen.fill(black)
        screen.blit(pauseButton.buttonText,pauseButton.buttonRect)
        screen.blit(text, textRect)
        screen.blit(timeText, timeRect)
        screen.blit(dogo.Player, ballRect)
        screen.blit(bitCoin.Player, ball2Rect)

    if GameState == "Menu":

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            #checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
            
                startButton.onClick(mouse)
        
        screen.fill(black)
        screen.blit(startButton.buttonText,startButton.buttonRect)
        screen.blit(GameName, GameNameRect)
    
    if GameState == "PlayerSelect":
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

            #checks if a mouse is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
            
                SinglePlayerButton.onClick(mouse)
                TwoPlayerButton.onClick(mouse)

        screen.fill(black)
        screen.blit(SinglePlayerButton.buttonText,SinglePlayerButton.buttonRect)
        screen.blit(TwoPlayerButton.buttonText,TwoPlayerButton.buttonRect)
        screen.blit(GameName, GameNameRect)
        


    pygame.display.update()

    def ChangeGameState(State, player1, player2, buttontext):
        global GameState
        
        if State == 'Menu':
            GameState = 'PlayerSelect'
        elif State == 'PlayerSelect':
            GameState = 'Play'
            if buttontext == 'Single Player':
                player2.NPC = True

        else:
            GameState = 'Menu'
        
        