#Ethan Eill, Justin Tran
#CPSC 4160
#Mar 1 2023
#Snake game using Model View Controller and pygame

import pygame
import random
import time
import model
import view

#setup pygame, view and model
pygame.init()
view.init()
model.init()

#game loop
while True:
    #if game is over then display the gameover screen
    if(model.game_over):
        view.game_over_message()
        pygame.quit()
        quit()
    events = pygame.event.get()
    for event in events:
        #if player quits then exit game
        if(event.type == pygame.QUIT):
            pygame.quit()
            quit()
        #check to see which direction player wants to go
        elif(event.type == pygame.KEYDOWN):
            #to go to the left
            if(event.key == pygame.K_a):
                #make sure not going to the right
                if(model.delta_x != 10):
                    model.delta_x = -10
                    model.delta_y = 0
            #to go to the right
            elif(event.key == pygame.K_d):
                #make sure not going to the left
                if(model.delta_x != -10):
                    model.delta_x = 10
                    model.delta_y = 0
            #to go down
            elif(event.key == pygame.K_s):
                #make sure not going up
                if(model.delta_y != -10):
                    model.delta_x = 0
                    model.delta_y = 10
            #to go up
            elif(event.key == pygame.K_w):
                #make sure not going down
                if(model.delta_y != 10):
                    model.delta_x = 0
                    model.delta_y = -10
            else:
                continue
            model.draw_snake()
    #if there is no key press, make sure snake
    #is still moving in same direction
    if(not events):
        model.draw_snake()

    #create framerate
    model.clock.tick(15)