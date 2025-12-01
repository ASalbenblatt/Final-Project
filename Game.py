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
countdown = framerate * 5
photos_taken = 0
screen_fraction = 0.2
flash = 0

pygame.font.init()
base_font = 'Quintessential-Regular.ttf'
instruction_font = pygame.font.Font(base_font, 40)

newpath = './Your_Photos' 
if os.path.exists(newpath):
    shutil.rmtree(newpath)
os.mkdir(newpath)

os.rename('./Save-Mem/Save-Data.txt', './Save-Mem/Save-Data.png')
image = pygame.image.load('./Save-Mem/Save-Data.png')
os.rename('./Save-Mem/Save-Data.png', './Save-Mem/Save-Data.txt')

while(True):
    timer.tick(framerate)        #Sets the framerate

    keys = pygame.key.get_pressed()
    events = pygame.event.get()

    
    W_H_ratio_img = pygame.Surface.get_width(image) / pygame.Surface.get_height(image)
    W_H_ratio_screen = pygame.Surface.get_width(screen) / pygame.Surface.get_height(screen)
    if W_H_ratio_img > W_H_ratio_screen:
        scale_factor = pygame.Surface.get_height(screen) / pygame.Surface.get_height(image)
        img_scaled = pygame.transform.scale_by(image, scale_factor)
    else:
        scale_factor = pygame.Surface.get_width(screen) / pygame.Surface.get_width(image)
        img_scaled = pygame.transform.scale_by(image, scale_factor)

    if game_state == 4:
        screen.blit(img_scaled, (0,0))

        text = instruction_font.render('Click anywhere to quit.', True, (255, 255, 245), (30, 20, 0))
        pygame.draw.rect(screen, (30, 20, 0), pygame.Rect(0, 0, 400, 70), border_bottom_right_radius=10)
        screen.blit(text, (15, 5))
    
    if game_state == 3:
        #lose
        screen.fill([30, 20, 0])

        text = instruction_font.render('You know what, it\'s ok you didn\'t take enough photos.', True, (235, 235, 255), (30, 20, 0))
        screen.blit(text, ((pygame.Surface.get_width(screen) - pygame.Surface.get_width(text))/2,(pygame.Surface.get_height(screen)/2)-170))

        text = instruction_font.render('It\'s probably better to just sit back and enjoy the view.', True, (235, 235, 255), (30, 20, 0))
        screen.blit(text, ((pygame.Surface.get_width(screen) - pygame.Surface.get_width(text))/2,(pygame.Surface.get_height(screen)/2)-90))

        text = instruction_font.render('No, no, no, just quick click anywhere and try again!', True, (255, 235, 235), (30, 20, 0))
        screen.blit(text, ((pygame.Surface.get_width(screen) - pygame.Surface.get_width(text))/2,(pygame.Surface.get_height(screen)/2)+50))

        text = instruction_font.render('You\'ll get 5 perfect photos this time.  I just know it!', True, (255, 235, 235), (30, 20, 0))
        screen.blit(text, ((pygame.Surface.get_width(screen) - pygame.Surface.get_width(text))/2,(pygame.Surface.get_height(screen)/2)+130))
    
        if countdown <= framerate * 3:
            bar_color = (255, 46, 31)
        elif countdown <= framerate * 9:
            bar_color = (255, 159, 5)
        else:
            bar_color = (35, 212, 4)
        pygame.draw.rect(screen, bar_color, pygame.Rect(0, 0, pygame.Surface.get_width(screen) * (countdown/(framerate * 15)), 20))

        if countdown <= 0:
            game_state = 4
            pygame.mixer.init()
            os.rename('./Save-Mem/File_1.txt', './Save-Mem/File_1.wav')
            pygame.mixer.music.load('./Save-Mem/File_1.wav')
            pygame.mixer.music.play(loops = -1)

        else:
            countdown -= 1

    if game_state == 2:
        #win
        screen.fill([30, 20, 0])

        text = instruction_font.render('Wow!  Those photos look great!', True, (255, 255, 245), (30, 20, 0))
        screen.blit(text, ((pygame.Surface.get_width(screen) - pygame.Surface.get_width(text))/2,(pygame.Surface.get_height(screen)/2)-140))

        text = instruction_font.render('They\'ve been put in a folder called \"Your_Photos\".', True, (255, 255, 245), (30, 20, 0))
        screen.blit(text, ((pygame.Surface.get_width(screen) - pygame.Surface.get_width(text))/2,(pygame.Surface.get_height(screen)/2)-60))

        text = instruction_font.render('To see them, just click anywhere.', True, (255, 255, 245), (30, 20, 0))
        screen.blit(text, ((pygame.Surface.get_width(screen) - pygame.Surface.get_width(text))/2,(pygame.Surface.get_height(screen)/2)+20))
    
    if game_state == 1:
        #Game
        screen.fill((0,0,0))
        
        photo_center = list(pygame.mouse.get_pos())
        
        photo_width = pygame.Surface.get_width(screen) * screen_fraction
        photo_height = pygame.Surface.get_height(screen) * screen_fraction

        if photo_center[0] < photo_width / 2:
            photo_center[0] = photo_width / 2
        if photo_center[0] > pygame.Surface.get_width(screen)  - photo_width / 2:
            photo_center[0] = pygame.Surface.get_width(screen)  - photo_width / 2
        if photo_center[1] < photo_height / 2:
            photo_center[1] = photo_height / 2
        if photo_center[1] > pygame.Surface.get_height(screen) - photo_height / 2:
            photo_center[1] = pygame.Surface.get_height(screen) - photo_height / 2

        if flash > 0:
            img_scaled.fill((255, 255, 235))
            flash -= 1

        photo_area = pygame.Rect(photo_center[0] - photo_width/2, photo_center[1] - photo_height/2, photo_width, photo_height)
        screen.blit(img_scaled, (photo_center[0] - photo_width/2, photo_center[1] - photo_height/2), photo_area)

        if countdown <= framerate:
            bar_color = (255, 46, 31)
        elif countdown <= framerate * 3:
            bar_color = (255, 159, 5)
        else:
            bar_color = (35, 212, 4)
        pygame.draw.rect(screen, bar_color, pygame.Rect(0, 0, pygame.Surface.get_width(screen) * (countdown/(framerate * 5)), 20))

        if photos_taken >= 5 and flash == 0:
            game_state = 2
        elif countdown <= 0:
            game_state = 3
            shutil.rmtree(newpath)
            countdown = framerate * 15
        else:
            countdown -= 1
    
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

    for event in events:
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            #code go here
            pass

        if game_state == 4:
            #4 - Post Lose
            pass

        if game_state == 3:
            #3 - Lose
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_state = 1
                countdown = framerate * 5
                if os.path.exists(newpath):
                    shutil.rmtree(newpath)
                os.mkdir(newpath)
                photos_taken = 0


        if game_state == 2:
            #2 - Win
            pass

        if game_state == 1:
            #1 - Game
            if event.type == pygame.MOUSEBUTTONDOWN and countdown != framerate*5:
                photos_taken += 1
                flash = 7
                photo = pygame.Surface((photo_width, photo_height))
                photo.blit(img_scaled, (0,0), photo_area)
                pygame.image.save(photo, './Your_Photos/Photo_'+str(photos_taken)+'.png')

        if game_state == 0:
            #0 - Instructions
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_state = 1
    
        #X button
        if event.type == pygame.QUIT or (event.type == pygame.MOUSEBUTTONDOWN and (game_state == 2 or game_state == 4)):
            pygame.display.quit()
            break

    else:
        pygame.display.flip()  #updates the screen
        continue  # Continue if the inner loop wasn't broken.
    break  # Inner loop was broken, break the outer.

if pygame.mixer.get_init():
    pygame.mixer.stop()
    pygame.mixer.quit()
if os.path.exists('./Save-Mem/File_1.wav'):
    os.rename('./Save-Mem/File_1.wav', './Save-Mem/File_1.txt')

if game_state == 0 or game_state == 1:
    shutil.rmtree(newpath)

if game_state == 4 or game_state == 2:
    shutil.rmtree('./Save-Mem')
    subprocess.Popen("python -c \"import os, time; time.sleep(1); os.remove('{}');\"".format(sys.argv[0]))
    sys.exit(0)