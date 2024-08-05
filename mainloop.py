import pygame

pygame.init()

#define screen size
screen_h = 720
screen_w = 1080

#create window
screen = pygame.display.set_mode ((screen_w,screen_h))

#import background image
bg = pygame.image.load('data/mega_bg_demo.png')


#main game loop
run = True
while run:

    screen.blit(bg, (0,0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()