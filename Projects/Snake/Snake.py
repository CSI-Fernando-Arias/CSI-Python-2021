import pygame
pygame.init()#initialize the game
dis=pygame.display.set_mode((400,300)) #creates and display the game
pygame.display.update()#updates the display of the game.
pygame.display.set_caption('Snake game by Edureka')#Adds the text to the display
game_over=False #If the game doesnt end it continues.
while not game_over:
    for event in pygame.event.get(): # We use the event.get() function so the game doesnt quit instantly when you run it.
        if event.type==pygame.QUIT: #This makes the game quit when you hit the close button
            game_over=True 
 
pygame.quit() #uninitialize the game
quit()