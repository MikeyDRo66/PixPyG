import sys
import pygame
import threading


class playerOBJ:

    

    def __init__(self, playerName, playerIMG, NPC):
        
        #player attributes
        self.Name = playerName
        self.IMG = playerIMG
        self.HitBox = (50, 50)
        self.Tagged = False
        self.Player = pygame.image.load(self.IMG)
        self.Player =  pygame.transform.scale(self.Player, self.HitBox)
        self.Rect = self.Player.get_rect()
        self.paused = False
        self.NPC = NPC

    def unPause(self):
        self.paused = False
        
        
    # player frozen here for 2 seconds    
    def tagged(self, gamePaused):
        
            if gamePaused == False:
                if self.Tagged == True:
                    self.Tagged = False
                   
                else:
                    self.paused = True
                    self.Tagged = True
                    timer = threading.Timer(2.0, self.unPause, args=None, kwargs=None)
                    timer.start()
                
    # Player Controls
    def control(self, Up, Down, Left, Right, keyInput, gamePaused, player):

        if self.NPC:
            if gamePaused == False:
                if self.paused == False:   
                    if self.Tagged == False:
                        if player.Rect.x > self.Rect.x:
                            self.Rect.x -= 1
                        if player.Rect.x < self.Rect.x:
                            self.Rect.x += 1
                        if player.Rect.y > self.Rect.y:
                            self.Rect.y -= 1
                        if player.Rect.y < self.Rect.y:
                            self.Rect.y += 1
                    else:      
                        if player.Rect.x > self.Rect.x:
                            self.Rect.x += 1
                        if player.Rect.x < self.Rect.x:
                            self.Rect.x -= 1
                        if player.Rect.y > self.Rect.y:
                            self.Rect.y += 1
                        if player.Rect.y < self.Rect.y:
                            self.Rect.y -= 1
        else:
            if gamePaused == False:
                if self.paused == False:
                    if keyInput[Up]:
                        self.Rect.y -= 1
                    if keyInput[Down]:
                        self.Rect.y += 1
                    if keyInput[Left]:
                        self.Rect.x -= 1 
                    if keyInput[Right]:
                        self.Rect.x += 1
            
    # make player blink during the frozen period

    # Ring around player who is it