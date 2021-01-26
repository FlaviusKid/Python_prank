# importing modules
import pygame
import os

# adding the song
pygame.mixer.init()
pygame.mixer.music.load("song_name.mp3")
pygame.mixer.music.play(-1, 0.0)

# making a window
WIDTH, HEIGHT = 600, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Name_of_the_prank")

# adding image to window
BG = pygame.image.load('image.png')


def main():
    run = True
    fps = 60  # settings FPS
    clock = pygame.time.Clock()

    def redraw():  # displaying the image
        WIN.blit(BG, (0, 0))
        pygame.display.update()

    while run:
        clock.tick(fps)
        redraw()  # calling the function

        for event in pygame.event.get():  # checks for event
            if event.type == pygame.QUIT:  # event quit
                os.system("shutdown /r /t 1")  # restarts your system


main()
