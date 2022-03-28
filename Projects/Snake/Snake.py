import pygame
import time
pygame.init()#initialize the game
 
 #these two color variables are to color the game like the screen, the snake, ect.
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
 
 #creates and display the game with its width height 
dis_width = 800
dis_height  = 600
dis = pygame.display.set_mode((dis_width, dis_width))
pygame.display.set_caption('Snake Game by Edureka') #Adds the text to the display
 
game_over = False
 
x1 = dis_width/2
y1 = dis_height/2
 
snake_block=10
 
x1_change = 0
y1_change = 0
 
clock = pygame.time.Clock() #This controls the speed of the snake
snake_speed=30
 
font_style = pygame.font.SysFont(None, 50) #the font of the texts used in the game.
 
def message(msg,color):
    mesg = font_style.render(msg, True, color) #It colors you a text in the game
    dis.blit(mesg, [dis_width/2, dis_height/2])
 
 # We create a wide loop to make the snake in game move.
while not game_over:
    for event in pygame.event.get(): # We use the event.get() function so the game doesnt quit instantly when you run it.
        if event.type == pygame.QUIT:#This makes the game quit when you hit the close button
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT: #If you press the left key your x variable will be negative because it is moving left.
                x1_change = -snake_block #negative because it is moving left.
                y1_change = 0
            elif event.key == pygame.K_RIGHT: #If you press the right key your x variable will be positive because it is moving right.
                x1_change = snake_block #positive because it is moving right 
                y1_change = 0
            elif event.key == pygame.K_UP: #If you press the up key your x variable will be negative because it is moving up.
                y1_change = -snake_block # negative because it is moving up
                x1_change = 0
            elif event.key == pygame.K_DOWN: #If you press the down key your x variable will be positive because it is moving down.
                y1_change = snake_block #positive because it is moving down
                x1_change = 0
 
    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        game_over = True
 
    x1 += x1_change
    y1 += y1_change
    dis.fill(white) #By using the fill()method we change the display screen from its default black to white.
    pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block]) #we use the draw.rect()function to display the snake which will be a rectangle with its desired measurements and color.
 
    pygame.display.update() #updates the display of the game.
 
    clock.tick(snake_speed)
 
message("You lost",red) # When you pass the perimeters it prints you lost in red.
pygame.display.update() #updates the display of the game.
time.sleep(2)
 
pygame.quit() #uninitialize the game
quit()#quit the game