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
base_font = 'Quintessential-Regular.ttf'
instruction_font = pygame.font.Font(base_font, 40)

newpath = './Your_Photos' 
if os.path.exists(newpath):
    shutil.rmtree(newpath)
os.mkdir(newpath)

while(True):
    timer.tick(framerate)        #Sets the framerate

    keys = pygame.key.get_pressed()
    events = pygame.event.get()

    
    if game_state == 4:
        pass
    
    if game_state == 3:
        pass
    
    if game_state == 2:
        pass
    
    if game_state == 1:
        #Game
        pass
    
    if game_state == 0:
        #Instructions
        screen.fill([30, 20, 0])

        text = instruction_font.render('Once you begin, you will have 5 seconds to take 5 pictures.', True, (255, 255, 245), (30, 20, 0))
        screen.blit(text, ((pygame.Surface.get_width(screen) - pygame.Surface.get_width(text))/2,(pygame.Surface.get_height(screen)/2)-220))

        text = instruction_font.render('Move your mouse around to explore the image and find the best 5 scenes.', True, (255, 255, 245), (30, 20, 0))
        screen.blit(text, ((pygame.Surface.get_width(screen) - pygame.Surface.get_width(text))/2,(pygame.Surface.get_height(screen)/2)-140))

        text = instruction_font.render('Once you\'ve found a good area, click to take a photo of it.', True, (255, 255, 245), (30, 20, 0))
        screen.blit(text, ((pygame.Surface.get_width(screen) - pygame.Surface.get_width(text))/2,(pygame.Surface.get_height(screen)/2)-60))

        text = instruction_font.render('Make sure to take good photos.  You won\'t be able to come back and take more.', True, (255, 255, 245), (30, 20, 0))
        screen.blit(text, ((pygame.Surface.get_width(screen) - pygame.Surface.get_width(text))/2,(pygame.Surface.get_height(screen)/2)+20))

        text = instruction_font.render('Click once to start', True, (255, 255, 245), (30, 20, 0))
        screen.blit(text, ((pygame.Surface.get_width(screen) - pygame.Surface.get_width(text))/2,(pygame.Surface.get_height(screen)/2)+150))

    pygame.display.flip()  #updates the screen

    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #code go here
            pass

        if game_state == 4:
            #4 - Post Lose
            pass

        if game_state == 3:
            #3 - Lose
            pass

        if game_state == 2:
            #2 - Win
            pass

        if game_state == 1:
            #1 - Game
            pass

        if game_state == 0:
            #0 - Instructions
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_state = 1
    
        #X button
        if event.type == pygame.QUIT:
            pygame.display.quit()
            break

    else:
        continue  # Continue if the inner loop wasn't broken.
    break  # Inner loop was broken, break the outer.

if game_state == 0 or game_state == 1 or game_state == 3:
    shutil.rmtree(newpath)

# if game_state == 4 or game_state == 2:
#     subprocess.Popen("python -c \"import os, time; time.sleep(1); os.remove('{}');\"".format(sys.argv[0]))
#     sys.exit(0)