import pygame
from sys import exit                           #for exit screen without error
pygame.init()                                  #for image and sound rendering
screen=pygame.display.set_mode((1280,720))     #for screen (width,height)
pygame.display.set_caption("MaZe")
# above code only create a screen and then immediately closes it to tackle it we use while true:
color=(128,128,128)
screen.fill(color)
while True:
  for event in pygame.event.get(): #to extract any action done by user on screen 
   if(event.type==pygame.QUIT):
        pygame.quit()
        exit()



   pygame.display.update()