import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Circle')

x,y = 300, 300
radius = 25
speed = 20

done = True
while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and x - radius - speed >= 0:  
            x -= speed
        if keys[pygame.K_d] and x + radius + speed <= 600:  
            x += speed
        if keys[pygame.K_w] and y - radius - speed >= 0: 
            y -= speed
        if keys[pygame.K_s] and y + radius + speed <= 600:  
            y += speed

   
    screen.fill((255, 255, 255))  
    pygame.draw.circle(screen, (255, 0 , 0), (x, y), radius)  
    pygame.display.update()

pygame.quit()
sys.exit()