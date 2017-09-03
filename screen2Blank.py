import os
import pygame
import time

def blank(screenNumber):
    if screenNumber == 1:
        dimensions = "-1920,0"
    elif screenNumber == 2:
        dimensions = "0,0"
    elif screenNumber == 3:
        dimensions = "1920,0"
    else:
        dimensions = "0,0"
    os.environ['SDL_VIDEO_WINDOW_POS'] = dimensions
    pygame.init()
    screen = pygame.display.set_mode((1920,1200))
    minutes = 3
    print ("screen" + str(screenNumber))
    for minute in range(minutes):
        time.sleep(2)