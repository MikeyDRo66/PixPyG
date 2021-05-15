import sys
import pygame

pygame.init()

size = width, height = 500, 500
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ballX = 250
ballY = 250
ball = pygame.image.load("square.PNG")

ballRect = ball.get_rect()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_UP]:
        ballRect.y -= 1 
    if key_input[pygame.K_DOWN]:
        ballRect.y += 1 
    if key_input[pygame.K_LEFT]:
        ballRect.x -= 1 
    if key_input[pygame.K_RIGHT]:
        ballRect.x += 1 

    screen.fill(black)
    screen.blit(ball, ballRect)
    pygame.display.update()