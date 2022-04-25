import pygame
from pygame.locals import *

pygame.init()
size = (width,height) = (pygame.display.Info().current_h,pygame.display.Info().current_h)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
bg_color = (0,102,0)

def main():
    global screen
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_f:
                    screen = pygame.display.set_mode(size,FULLSCREEN)
                elif event.key == K_ESCAPE:
                    screen = pygame.display.set_mode(size)
        screen.fill(bg_color)
        pygame.display.flip()

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
