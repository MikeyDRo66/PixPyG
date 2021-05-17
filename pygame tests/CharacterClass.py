import sys
import pygame
import threading


class playerOBJ:

    

    def __init__(self, playerName, playerIMG):
        
        #player attributes
        self.Name = playerName
        self.IMG = playerIMG
        self.HitBox = (50, 50)
        self.Tagged = False
        self.Player = pygame.image.load(self.IMG)
        self.Player =  pygame.transform.scale(self.Player, self.HitBox)
        self.Rect = self.Player.get_rect()
        self.paused = False
        

    def unPause(self):
        self.paused = False
        
        
        
    def tagged(self):
        

                if self.Tagged == True:
                    self.Tagged = False
                   
                else:
                    self.paused = True
                    self.Tagged = True
                    timer = threading.Timer(2.0, self.unPause, args=None, kwargs=None)
                    timer.start()
                
        # player frozen here for 2 seconds

            # make player blink during the frozen period

                # Ring around player who is it
    
    def control(self, Up, Down, Left, Right, keyInput):
        if self.paused == False:
            if keyInput[Up]:
                self.Rect.y -= 1
            if keyInput[Down]:
                self.Rect.y += 1
            if keyInput[Left]:
                self.Rect.x -= 1 
            if keyInput[Right]:
                self.Rect.x += 1