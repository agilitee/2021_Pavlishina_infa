import pygame
from pygame.draw import circle
from pygame.draw import rect
from random import randint
import math

print("Nickname: ")
nickname = input()

pygame.init()
FPS = 30
# params of screen
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

# colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

score = 0
# массив шариков
balls_pos = []
square_pos = []


def click(event):
    """
    Функция возвращает координаты щелчка мыши
    :param event: событие - щелчок мыши
    """
    (x, y) = event.pos
    return [x, y]


def score_show(score):
    """
    функция выводит количество очков на экран
    :param score: текущее количество очков
    """
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('Score: ' + str(score), True, (180, 0, 0))
    screen.blit(text1, (10, 50))


def new_ball():
    """
    Функция создает новый шарик случайного радиуса, случайного цвета.
    :return: возвращает координаты по x, y центра шара, его радиус r и изменения координат dx и
    dy для перемещения шарика
    """
    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    dx = randint(-10, 10)
    dy = randint(-10, 10)
    return [x, y, r, color, dx, dy]


def new_square():
    """
    Функция создает новый квадрат случайного цвета со случайной стороной
    :return: возвращает координаты по x, y верхнего левого угла квадрата , длину его стороны,
    его цвет, изменения координат dx и dy для перемещения квадрта
    """
    x = randint(100, 700)
    y = randint(100, 500)
    a = randint(60, 100)
    color = COLORS[randint(0, 5)]
    rect(screen, color, (x, y, a, a))
    dx = randint(-10, 10)
    dy = randint(-50, 50)
    return [x, y, a, color, dx, dy]


# создаем массив шариков
for i in range(10):
    balls_pos.append(new_ball())
# создаем массив квадратов
for i in range(2):
    square_pos.append(new_square())


def catch_ball(func_click, balls_pos):
    """
    Функция проверяет, был ли клик внутри шара, если да, то прибавляет 1 очко
    :param func_click: координаты х и у щелчка мыши
    :param balls_pos: массив шариков
    """
    global score
    for i in range(len(balls_pos)):
        if math.sqrt((func_click[0] - balls_pos[i][0]) ** 2 + (func_click[1] - balls_pos[i][1]) ** 2) <= balls_pos[i][
            2]:
            del balls_pos[i]
            balls_pos.append(new_ball())
            score += 1


def catch_square(func_click, square_pos):
    """
    Функция проверяет, был ли клик внутри квадрата, если да, то прибавляет 3 очка
    :param func_click: координаты клика
    :param square_pos: координаты верхнего левого угла квадрата
    """
    global score
    for i in range(len(square_pos)):
        if 0 < (func_click[0] - square_pos[i][0]) < square_pos[i][2]:
            if 0 < (func_click[1] - square_pos[i][1]) < square_pos[i][2]:
                del square_pos[i]
                square_pos.append(new_square())
                score += 3


def move_balls(balls_pos):
    """
    Функция перемещает шары в соответствии с их параметрами из массива.
    Если шар касается границы экрана, он отскакивает от него.
    :param balls_pos: массив шаров
    """
    for i in range(len(balls_pos)):
        balls_pos[i][0] += balls_pos[i][4]
        balls_pos[i][1] += balls_pos[i][5]

        if balls_pos[i][0] + balls_pos[i][2] >= screen_width:
            balls_pos[i][4] = -balls_pos[i][4] / balls_pos[i][4] * randint(1, 10)

        if balls_pos[i][0] - balls_pos[i][2] <= 0:
            balls_pos[i][4] = balls_pos[i][4] / balls_pos[i][4] * randint(1, 10)

        if balls_pos[i][1] + balls_pos[i][2] >= screen_height:
            balls_pos[i][5] = -balls_pos[i][5] / balls_pos[i][5] * randint(1, 10)

        if balls_pos[i][1] - balls_pos[i][2] <= 0:
            balls_pos[i][5] = balls_pos[i][5] / balls_pos[i][5] * randint(1, 10)

        circle(screen, balls_pos[i][3], (balls_pos[i][0], balls_pos[i][1]), balls_pos[i][2])


def move_squares(square_pos):
    """
    Функция перемещает квадраты в соответствии с их параметрами из массива.
    :param square_pos: массив квадратов
    """
    for i in range(len(square_pos)):
        square_pos[i][0] += square_pos[i][4]
        square_pos[i][1] += square_pos[i][5]

        if square_pos[i][0] + square_pos[i][2] >= screen_width:
            square_pos[i][0] -= square_pos[i][4]
            square_pos[i][4] = - square_pos[i][4]

        if square_pos[i][0] <= 0:
            square_pos[i][0] -= square_pos[i][4]
            square_pos[i][4] = - square_pos[i][4]

        if square_pos[i][1] + square_pos[i][2] >= screen_height:
            square_pos[i][1] -= square_pos[i][5]
            square_pos[i][5] = - square_pos[i][5]
            square_pos[i][5] -= square_pos[i][5] * 0.2 - 0.01

        if square_pos[i][1] <= 0:
            square_pos[i][1] -= square_pos[i][5]
            square_pos[i][5] = - square_pos[i][5]
            square_pos[i][5] += square_pos[i][5] * 0.2 - 0.01

        rect(screen, square_pos[i][3], (square_pos[i][0], square_pos[i][1], square_pos[i][2], square_pos[i][2]))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

file = open("top.txt", 'a')

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            catch_ball(click(event), balls_pos)
            catch_square(click(event), square_pos)
        if event.type == pygame.QUIT:
            finished = True
    score_show(score)
    move_balls(balls_pos)
    move_squares(square_pos)
    pygame.display.update()
    screen.fill(BLACK)

if score > 10:  # условие, чтобы игрок попал в топ
    file.write(nickname + " " + str(score) + '\n')
file.close()
pygame.quit()
