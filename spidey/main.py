import pygame, sys
from pygame.locals import *
from spider import Spider

pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)

pygame.display.set_caption('Spider-Man')

clock = pygame.time.Clock()

spiderman = Spider(screen, (200, 200), (50, 50))
while True:
    # gestione inputs
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            spiderman.move_right()
        else:

            spiderman.stop_move_right()
        if keys[K_LEFT]:
    
            spiderman.move_left()
        else:
    
            spiderman.stop_move_left()
        if keys[K_UP]:
    
            spiderman.move_up()
        else:
    
            spiderman.stop_move_up()
        if keys[K_DOWN]:
    
            spiderman.move_down()
        else:
    
            spiderman.stop_move_down()


    screen.fill((146,244,255))
    spiderman.update(0.15)
    spiderman.muovi()
    spiderman.draw()

    pygame.display.flip()
    clock.tick(60)