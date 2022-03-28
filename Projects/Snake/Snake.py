import pygame
import time
import random
 
pygame.init() #initialize the game 
 #These are all the color variables for the game
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
 #created and displays the game with its width height
dis_width = 800
dis_height = 600
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka') #Adds the text to the display
 
clock = pygame.time.Clock()
 #Variables for the display of the snake and the velocity of the snake
snake_block = 10
snake_speed = 30
 
font_style = pygame.font.SysFont(None, 30) #the font of the texts used in the game.
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color) #It colors you a text in the game
    dis.blit(mesg, [dis_width/3, dis_height/3])
 
 
def gameLoop():  # creating a function for the game to loop
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 #This spawns the food that the snake need to eat to get bigger and win the game. 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0   #This makes sure that the food is not too big so it fits in the screen.
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
  # We create a wide loop to make the snake in game move.
    while not game_over:
        #This block creates a message so you are able to either quit or play again when you lose the game.
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
 
            for event in pygame.event.get(): # We use the event.get() function so the game doesnt quit instantly when you run it.
                #If you click a key it does its job and makes the game loop
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get(): # We use the event.get() function so the game doesnt quit instantly when you run it.
            if event.type == pygame.QUIT: #This makes the game quit when you hit the close button
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: #If you press the left key your x variable will be negative because it is moving left.
                    x1_change = -snake_block #negative because it is moving left.
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:  #If you press the right key your x variable will be positive because it is moving right.
                    x1_change = snake_block #positive because it is moving right.
                    y1_change = 0
                elif event.key == pygame.K_UP: #If you press the up key your x variable will be negative because it is moving up.
                    y1_change = -snake_block #negative because it is moving up. 
                    x1_change = 0
                elif event.key == pygame.K_DOWN: #If you press the down key your x variable will be positive because it is moving down.
                    y1_change = snake_block #positive because it is moving down
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
 
        x1 += x1_change
        y1 += y1_change
        dis.fill(white)#By using the fill()method we change the display screen from its default black to white.
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])#we use the draw.rect()function to display the snake which will be a rectangle with its desired measurements and color, also to display the width and height of the food.
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])#we use the draw.rect()function to display the snake which will be a rectangle with its desired measurements and color.
        pygame.display.update()#updates the display of the game.
        #the snake collects food ir prints yummy.
        if x1 == foodx and y1 == foody:
            print("Yummy!!")
        clock.tick(snake_speed)
 
    pygame.quit() #uninitialize the game
    quit() #quit the game
 
 
gameLoop() #this loops the game or makes it possible.