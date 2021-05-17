import sys
import pygame
import CharacterClass
import threading
import timer

pygame.init()

size = width, height = 1000, 600

speed = [2, 2]
black = 0, 0, 0

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

screen = pygame.display.set_mode(size)

ballX = 250.0
ballY = 250.0



dogo = CharacterClass.playerOBJ('Doge', "dogo.png")
bitCoin = CharacterClass.playerOBJ('Bitcoin', "bitcoin.png")


ballRect = dogo.Rect
ball2Rect = bitCoin.Rect
ball2Rect.x = 50
ball2Rect.y = 50

font = pygame.font.Font('freesansbold.ttf', 32)



#set player as Tagged
dogo.Tagged = True

timer.timecounter(60)

text = font.render('Dogo is It', True, green, blue)
timeText = font.render('Time left | ' + str(timer.T), True, green, blue)

# create a rectangular object for the
# text surface object
textRect = text.get_rect()

textRect.center = (500, 50)

timeRect = timeText.get_rect()
timeRect.center = (500, 100)


while 1:


    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    key_input = pygame.key.get_pressed()
    
    # Keyboard controlls for "dogo"
    dogo.control(pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT, key_input)
     
    # Keyboard controlls for "Bitcoin"
    bitCoin.control(pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d, key_input)
    
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


    if ballRect.x >= ball2Rect.x and ballRect.x <= ball2Rect.x + 50 and ballRect.x + 50 >= ball2Rect.x and ballRect.x + 50 >= ball2Rect.x + 50 and ballRect.y >= ball2Rect.y and ballRect.y <= ball2Rect.y + 50 and ballRect.y + 50 >= ball2Rect.y and ballRect.y + 50 >= ball2Rect.y + 50:
        
        if dogo.paused == False and bitCoin.paused == False: 
            
            bitCoin.tagged()  
    
            dogo.tagged()
              
               


        
      
        if bitCoin.Tagged:

            text = font.render('Coin is It', True, green, blue)


        if dogo.Tagged:

            text = font.render('dogo is It', True, green, blue)

    
    timeText = font.render('Time left | ' + str(timer.T), True, green, blue)

    if(timer.T == 0):

        if bitCoin.Tagged:

            text = font.render('Dogo Wins!', True, green, blue)


        if dogo.Tagged:

            text = font.render('Coin Wins!', True, green, blue)

    screen.fill(black)
    screen.blit(text, textRect)
    screen.blit(timeText, timeRect)
    screen.blit(dogo.Player, ballRect)
    
    screen.blit(bitCoin.Player, ball2Rect)
    pygame.display.update()