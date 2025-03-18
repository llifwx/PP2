import pygame
import sys
import time

pygame.init()


screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Clock")
clockk = pygame.time.Clock()


def blitRotate2(surf, image, topleft, angle):
    scaled =pygame.transform.scale_by(image, 0.7)
    rotated_image = pygame.transform.rotate(scaled, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)
    surf.blit(rotated_image, new_rect.topleft)


clock = pygame.image.load('images/clock.png')
min_hand = pygame.image.load("images/min_hand.png")
sec_hand = pygame.image.load('images/sec_hand.png')


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min

    sec_angle = -seconds * 6  
    min_angle = -minutes * 6 - (seconds / 60) * 6

    pos = (-188, -140)

    screen.fill((0, 0, 0))  
    screen.blit(clock, (0, 0))
    blitRotate2(screen, sec_hand, pos, sec_angle)
    blitRotate2(screen, min_hand, pos, min_angle)


    pygame.display.flip()
    clockk.tick(30)

pygame.quit()
sys.exit()
