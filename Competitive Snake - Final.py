# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 13:05:08 2020

@author: samya
"""

import pygame
import random


class Snake():
    def __init__(self, snake_color, x1, y1, snake_block = 10, snake_speed = 15, Length_of_snake = 1,):
        
        self.snake_block = snake_block # block size
        self.snake_speed = snake_speed # snake speed
        self.Length_of_snake = Length_of_snake # snake length
        self.snake_color = snake_color # snake Color
        
        self.x1 = x1 #X coordinate
        self.y1 = y1 #Y coordinate
        self.x1_change = 0 #Value to update X coordinate
        self.y1_change = 0 #Value to update Y coordinate
        
        self.snake_Head = []#Will contain coordinates of snakehead
        self.snake_list = []#List to contain snake coordinates
        
        
    
    def draw_snake(self):
        for x in self.snake_list:
            pygame.draw.rect(dis,self.snake_color,[x[0],x[1], self.snake_block, self.snake_block])
    
    def update_position(self):
        self.x1 += self.x1_change #Updates x coordinate
        self.y1 += self.y1_change #Updates y coordinate
        
    def update_length(self):
        self.snake_Head = []
        self.snake_Head.append(self.x1)
        self.snake_Head.append(self.y1)
        self.snake_list.append(self.snake_Head)
        
        if len(self.snake_list) > self.Length_of_snake:
            del self.snake_list[0]
                
        self.draw_snake()
        



pygame.init() #Initializes all of the imported Pygame modules (returns a tuple indicating success and failure of initializations)

dis_width = 600
dis_height = 400

dis=pygame.display.set_mode((dis_width,dis_height)) #Takes a tuple or a list as its parameter to create a surface (tuple preferred)
pygame.display.set_caption("Competitive Snake Game") #Will set the caption text on the top of the display screen

clock = pygame.time.Clock()

#Defines colors to be used on the display
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

font_style = pygame.font.SysFont("bahnschrift", 15)
score_font = pygame.font.SysFont("comicsansms", 20)

def high_score(score):
    value = score_font.render("High Score: " + str(score), True, black)
    dis.blit(value, [(dis_width/2)-60,0])


def player1_score(score):
    value = score_font.render("Player 1 Score: " + str(score), True, yellow)
    dis.blit(value, [10,0])
    
def player2_score(score):
    value = score_font.render("Player 2 Score: " + str(score), True, yellow)
    dis.blit(value, [dis_width - 175,0])


def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/4, dis_height/4])



def gameLoop(): #Creating main game loop function

    #Highscore
    try:
        hisc=open("highscore.txt","r")
        highscore=hisc.read()
        hisc.close()
        highscore_int=int(highscore)
    except:
        hisc=open("highscore.txt","w")
        hisc.write(str(0))
        hisc.close()
        highscore_int=int(0)
    
    lastkeypressed_player1 = None
    lastkeypressed_player2 = None
    
    game_over = False   #Set game over condition to false
    game_close = False #Set game ending screen to false

    snake1 = Snake(black, 3*(dis_width/4), dis_height/4) #Initialization of Player Sprite
    snake2 = Snake(white, dis_width/4, (dis_height/4))
    
    foodx = round(random.randrange(0, dis_width - snake1.snake_block) / 10) * 10
    foody = round(random.randrange(0, dis_height - snake1.snake_block) / 10) * 10 
    
    
    
    while not game_over: #Main game loop
        
        while game_close == True: #Game ending screen
            
            dis.fill(blue)
            message("You lost! Press Q to quit or SPACE to play again.", red)
            
            player1_score(snake1.Length_of_snake - 1)
            player2_score(snake2.Length_of_snake - 1)
            high_score(highscore_int)
            
            if snake1.Length_of_snake > snake2.Length_of_snake:
                current_score = snake1.Length_of_snake - 1
            else:
                current_score = snake2.Length_of_snake - 1
            
            if current_score > highscore_int:
                hisc=open("highscore.txt","w")
                hisc.write(str(current_score))
                hisc.close()
                
                highscore_int=current_score
                message("One of you broke the high score!", red)
            high_score(highscore_int)
            
            pygame.display.update()
            
            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  #Exits the game
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_SPACE: #Restarts the games
                        gameLoop()
        
        for event in pygame.event.get(): #Returns list of all events
        
            if event.type == pygame.QUIT: #closes the screen if the exit buttion is pressed
                game_over = True
            
          
            
            if event.type == pygame.KEYDOWN: #Checks for key presses - movement
                if event.key == pygame.K_LEFT and lastkeypressed_player1 != "right": #keyleft
                    snake1.x1_change = -snake1.snake_block
                    snake1.y1_change = 0
                    lastkeypressed_player1 = "left"
                    
                elif event.key == pygame.K_RIGHT and lastkeypressed_player1 != "left": #keyright
                    
                    snake1.x1_change = snake1.snake_block
                    snake1.y1_change = 0
                    lastkeypressed_player1 = "right"
                    
                elif event.key == pygame.K_UP and lastkeypressed_player1 != "down": #keyup
                    snake1.x1_change = 0
                    snake1.y1_change = -snake1.snake_block
                    lastkeypressed_player1 = "up"
                    
                elif event.key == pygame.K_DOWN and lastkeypressed_player1 != "up": #keydown
                    snake1.x1_change = 0
                    snake1.y1_change = snake1.snake_block
                    lastkeypressed_player1 = "down"
                    
                    
                if event.key == pygame.K_a and lastkeypressed_player2 != "right": #keyleft
                    snake2.x1_change = -snake2.snake_block
                    snake2.y1_change = 0
                    lastkeypressed_player2 = "left"
                    
                elif event.key == pygame.K_d and lastkeypressed_player2 != "left": #keyright
                    snake2.x1_change = snake2.snake_block
                    snake2.y1_change = 0
                    lastkeypressed_player2 = "right"
                    
                elif event.key == pygame.K_w and lastkeypressed_player2 != "down": #keyup
                    snake2.x1_change = 0
                    snake2.y1_change = -snake2.snake_block
                    lastkeypressed_player2 = "up"
                    
                elif event.key == pygame.K_s and lastkeypressed_player2 != "up": #keydown
                    snake2.x1_change = 0
                    snake2.y1_change = snake2.snake_block
                    lastkeypressed_player2 = "down"
    
        if snake1.x1 >= dis_width or snake1.x1 < 0 or snake1.y1 >= dis_height or snake1.y1 < 0: #Checks if the player is out of bounds and game overs if they are
            game_close = True
                    
        if snake2.x1 >= dis_width or snake2.x1 < 0 or snake2.y1 >= dis_height or snake2.y1 < 0: #Checks if the player is out of bounds and game overs if they are
            game_close = True
                    
        snake1.update_position()
        snake2.update_position()
        
        dis.fill(blue)
        
        pygame.draw.rect(dis,green,[foodx,foody,snake1.snake_block/2, snake1.snake_block/2]) #Draws food
        
        
        snake1.update_length()
        snake2.update_length()
        
        for x in snake1.snake_list[:-1]: #Checks for snakes collision with self and triggers game over if true
            if x == snake1.snake_Head or x == snake2.snake_Head:
                game_close = True
                pygame.display.update()
                
        for x in snake2.snake_list[:-1]: #Checks for snakes collision with self and triggers game over if true
            if x == snake1.snake_Head or x == snake2.snake_Head:
                game_close = True
                pygame.display.update()
        
        player1_score(snake1.Length_of_snake - 1) #Updates score according to snake length
        player2_score(snake2.Length_of_snake - 1)
        high_score(highscore_int)
        
        pygame.display.update() #Updates the screen
        
        if snake1.x1 == foodx and snake1.y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake1.snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake1.snake_block) / 10.0) * 10.0
            snake1.Length_of_snake += 1
            
        if snake2.x1 == foodx and snake2.y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake1.snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake1.snake_block) / 10.0) * 10.0
            snake2.Length_of_snake += 1
            
        clock.tick(snake1.snake_speed)
        
    
    pygame.quit() # Used to uninitialize everything
    
gameLoop()