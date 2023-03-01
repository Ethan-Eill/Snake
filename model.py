import pygame
import time
import random
import view

#initial setup of all the variables
def init():

    #global variables
    global x, y
    global delta_x, delta_y
    global food_x, food_y
    global snake_list
    global clock
    global game_over

    #position variable
    x,y = 200,200
    delta_x,delta_y = 10,0

    #food position variables
    food_x, food_y = random.randrange(0,view.width)//10*10, random.randrange(0,view.height)//10*10

    #snake list to hold all positions of snake
    snake_list = [(x,y)]

    #time object
    clock = pygame.time.Clock()

    #keep track of if game is over
    game_over = False


#update snake position and draw to screen
def draw_snake():
    #make sure x and y are used as global varaiables
    #then update position
    global x,y, food_x, food_y
    global snake_list
    global game_over
    #'%' used to make sure snake doesnt go out of screen
    x = (x + delta_x)%view.width
    y = (y + delta_y)%view.height

    #if head of snake hits its body then game over
    if((x,y) in snake_list):
        game_over = True
        return

    #append the changed x and y values to snake_list
    snake_list.append((x,y))

    #if snake hits food then change food coordinate
    if(food_x == x and food_y == y):
        while((food_x,food_y) in snake_list):
            food_x, food_y = random.randrange(0,view.width)//10*10, random.randrange(0,view.height)//10*10
    #if doesnt hit food then delete the previous x and y value from snake_list
    else:
        del snake_list[0]

    #update display of snake
    view.update_snake(food_x, food_y, snake_list, str(len(snake_list)))