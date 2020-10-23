import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption('THE BALL GAME')
font = pygame.font.Font(None, 50)
score = 0

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

screen.fill(BLACK)
rect(screen, WHITE, (0, 0, 1200, 70))  # draws white line for score

text0 = font.render("SCORE:", True, MAROON)
screen.blit(text0, (100, 25))

str_format_speed = str(FPS) + " FPS"
text1 = font.render(str_format_speed, True, GREY)
screen.blit(text1, (900, 25))


class Ball:
    def __init__(self):
        self.color = COLORS[randint(0, 5)]
        self.coords = [randint(70, 1130), randint(150, 830)]
        self.radius = randint(20, 80)
        self.speed = [randint(-10, 10), randint(-20, 20)]

    def paint(self):
        circle(screen, self.color, self.coords, self.radius)

    def moved(self):
        a = (0 + self.radius, 70 + self.radius)
        b = (1200 - self.radius, 900 - self.radius)
        for i in (0, 1):
            if a[i] < self.coords[i] + self.speed[i] < b[i]:
                pass
            else:
                self.speed[i] = (-1) * self.speed[i]
            self.coords[i] = self.coords[i] + self.speed[i]

    def mouse_click(self, xy):
        (event.x, event.y) = xy
        (x, y) = self.coords
        distance = ((event.x - x) ** 2 + (event.y - y) ** 2) ** 0.5
        if distance <= self.radius:
            circle(screen, BLACK, self.coords, self.radius)
            self.color = COLORS[randint(0, 5)]
            self.coords = [randint(70, 1130), randint(150, 830)]
            self.radius = randint(20, 80)
            self.speed = [randint(-10, 10), randint(-10, 10)]
            self.paint()
            pygame.display.update()
            return 1
        else:
            return 0


def clock_renewal(j):
    time_passed = int(j / FPS)
    if time_passed < 60:
        str_format_time = "Time:  " + str(time_passed) + "s"
    else:
        str_format_time = "Time:  " + str(time_passed // 60) + "m  " + \
                          str(time_passed % 60) + "s"
    text2 = font.render(str_format_time, True, OLIVE)
    rect(screen, WHITE, (600, 0, 200, 70))
    screen.blit(text2, (500, 25))


def score_renewal(s):
    rect(screen, WHITE, (240, 0, 100, 70))
    str_format_score = str(s)
    text3 = font.render(str_format_score, True, MAROON)
    screen.blit(text3, (250, 25))


balls_list = [Ball() for k in range(12)]
for ball in balls_list:
    ball.paint()
pygame.display.update()
clock = pygame.time.Clock()
finished = False
counter = 0  # variable for counting time

while not finished:
    clock.tick(FPS)
    ball_number = 0
    counter += 1
    clock_renewal(counter)
    rect(screen, BLACK, (0, 70, 1200, 830))
    for ball in balls_list:
        ball.moved()
        ball.paint()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls_list:
                score += ball.mouse_click(event.pos)
            score_renewal(score)
    pygame.display.update()

pygame.quit()
