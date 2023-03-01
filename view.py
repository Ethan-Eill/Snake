import pygame
import random
import time

#initial function call to setup the game window
def init():

    #define global variables
    global width, height
    global game_screen
    global background_color
    global font

    #create display
    width, height = 400, 400
    game_screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Snake")
    background_color = (0,0,0)
    font = pygame.font.SysFont("Calibri", 25)

#general display updates to do during the game loop
def update_snake(food_x, food_y, snake_list, length):

    global score

    #fill in the space behind the snake with background_color
    game_screen.fill(background_color)

    #update score
    score = font.render("Score: " + length, True, (255,255,255))
    game_screen.blit(score, [0,0])

    #draw food into game at random position
    pygame.draw.rect(game_screen, (255,0,0), [food_x, food_y, 10,10])

    #iterate through the tuple of snake body and draw to screen
    for (i,j) in snake_list:
        pygame.draw.rect(game_screen, (0,255,0), [i,j,10,10])
    
    pygame.display.update()


#to display a game over message for 4 seconds
def game_over_message():
    game_screen.fill((0,0,0))
    game_screen.blit(score, [0,0])
    msg = font.render("GAME OVER", True, (255,0,0))
    game_screen.blit(msg, [width/3, height/3])
    pygame.display.update()
    time.sleep(4)