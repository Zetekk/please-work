import sys
import pygame, os
import game_module as gm

os.environ['SDL_VIDEO_CENTERED'] = '1'          #centrowanie okna
pygame.init()

from pygame.locals import *
pygame.init()

pygame.display.set_caption('game base')

screen = pygame.display.set_mode(gm.SIZESCREEN)

clock = pygame.time.Clock()


#we need:
#character
#gamepad movement



pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())

my_square = pygame.Rect(50, 50, 50, 50)
my_square_color = 0
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
motion = [0, 0]

while True:

    screen.fill((0, 0, 0))

    pygame.draw.rect(screen, colors[my_square_color], my_square)
    if abs(motion[0]) < 0.1:
        motion[0] = 0
    if abs(motion[1]) < 0.1:
        motion[1] = 0
    my_square.x += motion[0] * 10
    my_square.y += motion[1] * 10

    for event in pygame.event.get():
        if event.type == JOYBUTTONDOWN:
            print(event)
            if event.button == 0:
                my_square_color = (my_square_color + 1) % len(colors)
        if event.type == JOYBUTTONUP:
            print(event)
        if event.type == JOYAXISMOTION:
            print(event)
            if event.axis < 2:
                motion[event.axis] = event.value
        if event.type == JOYHATMOTION:
            print(event)
        if event.type == JOYDEVICEADDED:
            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
            for joystick in joysticks:
                print(joystick.get_name())
        if event.type == JOYDEVICEREMOVED:
            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.update()
    clock.tick(60)
#gamepad movement end


    #sprites
    #movement
    #guns and bullets
#rocks
    #how they die
#big head
    #how it acts
#ui
#g??owna p??tla gra
window_open = True
while window_open:
    #screen.fill(gm.LIGHTBLUE)
    screen.blit(gm.BACKGROUND, (0,0))
    #p??tla zdarze??
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window_open = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                window_open = False

        player.get_event(event)
    #pionts
