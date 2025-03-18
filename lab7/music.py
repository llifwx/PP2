import pygame 
import sys

pygame.init()

screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('music player')


songs = [
    'music/Arctic Monkeys - Do I Wanna Know.mp3',
    'music/Chase Atlantic - Consume (feat. Goon Des Garcons).mp3',
    'music/LiL Peep - Star Shopping.mp3',
    'music/The Neighbourhood - Sweater Weather.mp3',
    'music/The Weeknd - Save your tears.mp3'
]


index_of_the_song = 0 
def play_song(index):
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()

play_song(index_of_the_song)

paused = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                index_of_the_song = (index_of_the_song + 1) % len(songs)
                play_song(index_of_the_song)


            if event.key == pygame.K_LEFT:
                index_of_the_song = (index_of_the_song - 1) % len(songs)
                play_song(index_of_the_song)


            if event.key == pygame.K_SPACE:  
                global _paused
                if paused:
                    pygame.mixer.music.unpause() 
                else:
                    pygame.mixer.music.pause() 
                paused = not paused  


    screen.fill((255, 255, 255))
    pygame.display.update()


pygame.mixer.music.stop()
pygame.quit()
sys.exit()