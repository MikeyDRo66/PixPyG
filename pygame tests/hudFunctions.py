import pygame
import time


global PAUSE_FLAG

PAUSE_FLAG = False

class button():

    def __init__(self, text, coordinates, size, fontname, fontsize, textcolor, backcolor, function):
        self.Text = text
        self.Size = size
        self.FontName = fontname
        self.FontSize = fontsize
        self.Coordinates = coordinates
        self.TextColor = textcolor
        self.BackColor = backcolor
        self.Function = function

        # initalize font
        self.font = pygame.font.Font(self.FontName, self.FontSize)

        # initalize pygame text instance
        self.buttonText = self.font.render(self.Text, True, self.TextColor, self.BackColor)

        self.buttonText = pygame.transform.scale(self.buttonText, self.Size)

        self.buttonRect = self.buttonText.get_rect()

        self.buttonRect.center = self.Coordinates

    #checks if mouse is over button
    def isOver(self, mousePosition):
        if mousePosition[0] >= self.Coordinates[0] - self.Size[0]/2 and mousePosition[0] <= self.Coordinates[0] + self.Size[0]/2 and mousePosition[1] >= self.Coordinates[1] - self.Size[1]/2 and mousePosition[1] <= self.Coordinates[1] + self.Size[1]/2 :
             self.buttonText = self.font.render(self.Text, True, (255,0,0), self.BackColor)
        else:
             self.buttonText = self.font.render(self.Text, True, self.TextColor, self.BackColor)
    #activates buttons functionality
    def onClick(self, mousePosition):

        if mousePosition[0] >= self.Coordinates[0] - self.Size[0]/2 and mousePosition[0] <= self.Coordinates[0] + self.Size[0]/2 and mousePosition[1] >= self.Coordinates[1] - self.Size[1]/2 and mousePosition[1] <= self.Coordinates[1] + self.Size[1]/2 :
            
            self.Function()
        

def pauseGame():
    global PAUSE_FLAG

    if PAUSE_FLAG:
        PAUSE_FLAG = False

    else:
        PAUSE_FLAG = True
