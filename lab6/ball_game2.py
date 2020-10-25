import pygame
from pygame.draw import *
from random import randint
from random import randrange

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption('THE BALL GAME')
font = pygame.font.Font(None, 50)
score = 0

# color palette, ball colors:
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 128, 0)
MAGENTA = (180, 0, 255)
CYAN = (0, 255, 255)
LIME = (128, 255, 0)
PINK = (255, 100, 180)
# star colors
ORANGE = (255, 160, 0)
YELLOW = (255, 240, 0)
# background
NAVY_BLUE = (0, 0, 128)
MAROON = (128, 0, 0)
OLIVE = (0, 128, 128)
WHITE = (255, 255, 245)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, LIME, GREEN, MAGENTA, CYAN, PINK, YELLOW]


def menu_intro():
    screen.fill(MAROON)
    font1 = pygame.font.Font(None, 100)
    text = font1.render("THE BALL GAME", True, NAVY_BLUE)
    text_rect = text.get_rect()
    text_rect.center = (600, 300)
    rect(screen, WHITE, (200, 200, 800, 500))
    screen.blit(text, text_rect)

    font2 = pygame.font.Font(None, 35)
    text = font2.render(
        "Please enter your name (max 10 letters) and press enter",
        True, OLIVE)
    text_rect = text.get_rect()
    text_rect.center = (600, 500)
    line(screen, BLACK, (500, 600), (700, 600), 5)
    screen.blit(text, text_rect)


class Ball:
    def __init__(self):
        self.color = COLORS[randint(0, 7)]
        self.coords = [randint(70, 1130), randint(150, 830)]
        self.radius = randint(30, 80)
        self.speed = [randint(-15, 15), randint(-15, 15)]

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
            self.color = COLORS[randint(0, 7)]
            self.coords = [randint(70, 1130), randint(150, 830)]
            self.radius = randint(30, 80)
            self.speed = [randint(-15, 15), randint(-15, 15)]
            self.paint()
            pygame.display.update()
            return 1
        else:
            return 0


class Star:
    def __init__(self):
        self.coords = [randint(70, 1130), randint(150, 830)]
        self.radius = randint(40, 80)
        self.speed = [randrange(-1, 1, 2) * randint(2, 15),
                      randint(2, 15)]

    def paint(self):
        a = 0
        for radius in range(self.radius, 10, -8):
            if a % 2 == 0:
                color = ORANGE
            else:
                color = WHITE
            circle(screen, color, self.coords, radius)
            a += 1

    def glow(self, time):
        if time % 10 >= 6:
            circle(screen, BLACK, self.coords, self.radius)
        else:
            Star.paint(self)

    def moved(self):
        a = 0
        if -100 < self.coords[0] < 1300:
            self.coords[0] = self.coords[0] + self.speed[0]
        else:
            a = 1
        if -100 < self.coords[1] < 1000:
            self.coords[1] = self.coords[1] + self.speed[1]
        else:
            a = 1
        if a == 1:
            return 0
        else:
            return 1

    def mouse_click(self, xy):
        (event.x, event.y) = xy
        (x, y) = self.coords
        distance = ((event.x - x) ** 2 + (event.y - y) ** 2) ** 0.5
        if distance <= self.radius:
            circle(screen, BLACK, self.coords, self.radius)
            pygame.display.update()
            return 0, 5
        else:
            return 1, 0
    # 1st number in return defines star's existence, 2nd number - score


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


menu_intro()
finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == 13:
                finished = True

screen.fill(BLACK)
rect(screen, WHITE, (0, 0, 1200, 70))  # draws white line for score
text0 = font.render("SCORE:", True, MAROON)
screen.blit(text0, (100, 25))
str_format_speed = str(FPS) + " FPS"
text1 = font.render(str_format_speed, True, NAVY_BLUE)
screen.blit(text1, (900, 25))

number_of_balls = 10
balls_list = [Ball() for k in range(number_of_balls)]
for ball in balls_list:
    ball.paint()
pygame.display.update()
clock = pygame.time.Clock()
finished = False
counter = 0  # variable for counting time
star_criteria = 100  # period of time when 1 star is spawned
star_existence = 0  # checks the star's existence (1 = true)

while not finished:
    clock.tick(FPS)
    ball_number = 0
    counter += 1
    clock_renewal(counter)
    rect(screen, BLACK, (0, 70, 1200, 830))  # resets the screen
    if counter % (10 * FPS) == 0:
        star_criteria = randint(100, 300)
    if counter % star_criteria == 0:  # spawns star every 3-10s
        star = Star()
        star.paint()
        star_existence = 1
    for ball in balls_list:
        ball.moved()
        ball.paint()
    if star_existence == 1:
        star.moved()
        star.glow(counter)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls_list:
                score += ball.mouse_click(event.pos)
            if star_existence == 1:
                score += star.mouse_click(event.pos)[1]
                star_existence *= star.mouse_click(event.pos)[0]
            score_renewal(score)
    pygame.display.update()

print("SCORE:  " + str(score))
print("TIME:  " + str(int(counter / FPS)))
pygame.quit()
