import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 1.2
screen = pygame.display.set_mode((1200, 900))
font = pygame.font.Font(None, 50)

# color palette
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 245)
GREY = (150, 150, 150)
MAROON = (128, 0, 0)
OLIVE = (0, 128, 128)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

score = 0
counter = 0  # variable for counting time
(x, y, r) = (0, 0, 0)

screen.fill(BLACK)
rect(screen, WHITE, (0, 0, 1200, 70))  # line for score

text0 = font.render("SCORE:", True, MAROON)
screen.blit(text0, (100, 25))

str_format_speed = "Speed:   " + str(FPS) + " FPS"
text1 = font.render(str_format_speed, True, GREY)
screen.blit(text1, (900, 25))


def new_ball():
    '''
    function draws new ball
    '''
    global x, y, r
    x = randint(70, 1130)
    y = randint(150, 830)
    r = randint(20, 80)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    counter += 1
    time_passed = int(counter * FPS)
    if time_passed < 60:
        str_format_time = "Time:  " + str(time_passed) + "s"
    else:
        str_format_time = "Time:  " + str(int(time_passed / 60)) + "m  " + \
            str(time_passed // 60) + "s"
    text2 = font.render(str_format_time, True, OLIVE)
    rect(screen, WHITE, (600, 0, 200, 70))
    screen.blit(text2, (500, 25))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            (event.x, event.y) = event.pos
            radius = ((event.x - x) ** 2 + (event.y - y) ** 2) ** 0.5
            if radius <= r:
                score += 1
                rect(screen, WHITE, (240, 0, 100, 70))
                str_format_score = str(score)
                text3 = font.render(str_format_score, True, MAROON)
                screen.blit(text3, (250, 25))
    new_ball()
    pygame.display.update()
    rect(screen, BLACK, (0, 70, 1200, 830))

pygame.quit()
