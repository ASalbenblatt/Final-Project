from math import *

import pygame

import random as rnd
import numpy as np

import sys, subprocess, os, shutil

game_state = 0 
#0 - Instructions
#1 - Game
#2 - Win
#3 - Lose
#4 - Post Lose

#Creates the window
pygame.display.init()
screen_size = pygame.display.get_desktop_sizes()[0]
screen_size = (screen_size[0], screen_size[1] - 60)
flags = pygame.RESIZABLE
screen = pygame.display.set_mode(screen_size, flags)

timer = pygame.time.Clock()
framerate = 60
countdown = 100

pygame.font.init()
# base_font = 'Minecraftia-Regular.ttf'
# UI_font = pygame.font.Font(base_font, 20)

newpath = './Your_Photos' 
os.mkdir(newpath)

while(True):
    timer.tick(framerate)        #Sets the framerate

    keys = pygame.key.get_pressed()
    events = pygame.event.get()

    screen.fill([0, 0, 5])

    #code here
    
    pygame.display.flip()  #updates the screen

    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #code go here
            pass
    
        #X button
        if event.type == pygame.QUIT:
            pygame.display.quit()
            break

    else:
        continue  # Continue if the inner loop wasn't broken.
    break  # Inner loop was broken, break the outer.

if game_state == 0 or game_state == 1 or game_state == 3:
    shutil.rmtree(newpath)

if game_state == 4 or game_state == 2:
    subprocess.Popen("python -c \"import os, time; time.sleep(1); os.remove('{}');\"".format(sys.argv[0]))
    sys.exit(0)