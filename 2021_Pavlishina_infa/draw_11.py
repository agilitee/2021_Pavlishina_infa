import pygame
import math
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((700, 1000))


def yourta(x1, y1, l, h):
    '''
    функция рисует юрту заданных размеров в заданном месте
    :param x1: координата по х верхнего левого угла прямоугольника, в который будет вписана юрта
    :param y1: координата по у верхнего левого угла прямоугольника, в который будет вписана юрта
    :param l: ширина юрты
    :param h: высота юрты, умноженная на 2
    :return: функция ничего не возвращает
    '''
    ellipse(screen, (230, 230, 230), (x1, y1, l, h))
    arc(screen, (0, 0, 0), (x1, y1, l, h), math.pi * 2, math.pi, 3)
    rect(screen, (255, 255, 255), (x1, y1 + h / 2, l, h / 2))
    line(screen, (0, 0, 0), (x1, y1 + h / 2), (x1 + l, y1 + h / 2), 1)
    x2 = x1 + l / 8
    xx2 = x2 - x1 - l / 2
    l2 = l / 2
    y2 = -(h / 2) * math.sqrt(1 - (xx2 ** 2) / (l2 ** 2)) + y1 + h / 2
    arc(screen, (0, 0, 0), (x2, y2 - 5, 0.75 * l, 10), math.pi, math.pi * 2, 2)
    x3 = x1 + l / 32
    xx3 = x3 - x1 - l / 2
    y3 = -(h / 2) * math.sqrt(1 - (xx3 ** 2) / (l2 ** 2)) + y1 + h / 2
    arc(screen, (0, 0, 0), (x3, y3 - 5, 0.9375 * l, 10), math.pi, math.pi * 2, 2)
    x4 = x1 + l / 4
    xx4 = x4 - x1 - l / 2
    y4 = -(h / 2) * math.sqrt(1 - (xx4 ** 2) / (l2 ** 2)) + y1 + h / 2
    arc(screen, (0, 0, 0), (x4, y4 - 5, 0.5 * l, 10), math.pi, math.pi * 2, 2)
    line(screen, (0, 0, 0), (x3 + l / 5, y3), (x1 + l / 5, y1 + h / 2), 1)
    line(screen, (0, 0, 0), (x3 + 2 * l / 5, y3), (x1 + 3 * l / 7, y1 + h / 2), 1)
    line(screen, (0, 0, 0), (x3 + 3 * l / 5, y3), (x1 + 4 * l / 6, y1 + h / 2), 1)
    line(screen, (0, 0, 0), (x3 + 4 * l / 5, y3), (x1 + 7 * l / 8, y1 + h / 2), 1)
    line(screen, (0, 0, 0), (x2 + l / 4, y2), (x3 + 2 * l / 7, y3 + 5), 1)
    line(screen, (0, 0, 0), (x2 + 4 * l / 7, y2), (x3 + 5 * l / 7, y3 + 5), 1)
    line(screen, (0, 0, 0), (x4 + l / 10, y4), (x2 + l / 8, y2 + 5), 1)
    line(screen, (0, 0, 0), (x4 + l / 4, y4), (x2 + 3 * l / 7, y2 + 5), 1)
    line(screen, (0, 0, 0), (x4 + 5 * l / 11, y4), (x2 + 8 * l / 12, y2 + 5), 1)
    line(screen, (0, 0, 0), (x1 + l / 2, y1), (x4 + 4 * l / 12, y4 + 5), 1)


def esquimos(x1, y1, l, h, lr):
    if lr == 0:
        ellipse(screen, (149, 124, 110), (x1 - 0.3 * l, y1 + h, 0.55 * l, 0.25 * h))
        line(screen, (0, 0, 0), (x1 - 0.25 * l, y1), (x1 - 0.25 * l, y1 + 2 * h), 1)
        tale = pygame.Surface((0.55 * l, 0.25 * h))
        tale.set_colorkey('BLACK')
        ellipse(tale, (149, 124, 110), (0, 0, 0.5 * l, 0.25 * h))
        tale2 = pygame.transform.rotate(tale, 330)
        screen.blit(tale2, (x1 + 0.78 * l, y1 + 0.91 * h))
    else:
        ellipse(screen, (149, 124, 110), (x1 + 0.78 * l, y1 + 0.91 * h, 0.55 * l, 0.25 * h))
        line(screen, (0, 0, 0), (x1 + 1.2 * l, y1), (x1 + 1.2 * l, y1 + 2 * h), 1)
        tale = pygame.Surface((0.55 * l, 0.25 * h))
        tale.set_colorkey('BLACK')
        ellipse(tale, (149, 124, 110), (0, 0, 0.5 * l, 0.25 * h))
        tale2 = pygame.transform.rotate(tale, 30)
        screen.blit(tale2, (x1 - 0.3 * l, y1 + 0.9 * h))
    ellipse(screen, (228, 222, 219), (x1, y1, l, h))
    ellipse(screen, (149, 124, 110), (x1 - 0.1 * l, y1 + h / 2, 1.2 * l, 3 * h))
    rect(screen, (255, 255, 255), (x1 - 0.1 * l, y1 + h * 2, 1.2 * l, 2 * h))
    rect(screen, (111, 92, 82), (x1 + 0.35 * l, y1 + h / 2, 0.3 * l, 1.5 * h))
    ellipse(screen, (149, 124, 110), (x1 + 0.12 * l, y1 + 1.85 * h, 0.25 * l, 0.5 * h))
    ellipse(screen, (149, 124, 110), (x1 + 0.62 * l, y1 + 1.85 * h, 0.25 * l, 0.5 * h))
    ellipse(screen, (149, 124, 110), (x1, y1 + 1.8 * h + 0.4 * h, 0.35 * l, 0.2 * h))
    ellipse(screen, (149, 124, 110), (x1 + 0.62 * l, y1 + 2.2 * h, 0.35 * l, 0.2 * h))
    ellipse(screen, (175, 157, 146), (x1 + 0.1 * l, y1 + 0.1 * h, 0.8 * l, 0.8 * h))
    ellipse(screen, (229, 218, 219), (x1 + 0.2 * l, y1 + 0.2 * h, 0.6 * l, 0.6 * h))
    line(screen, (0, 0, 0), (x1 + 0.32 * l, y1 + 0.35 * h), (x1 + 0.42 * l, y1 + 0.4 * h), 2)
    line(screen, (0, 0, 0), (x1 + 0.64 * l, y1 + 0.35 * h), (x1 + 0.54 * l, y1 + 0.4 * h), 2)
    arc(screen, (0, 0, 0), (x1 + 0.3 * l, y1 + 0.5 * h, 0.4 * l, 0.4 * h), math.pi * 0.3, math.pi * 0.7, 2)
    rect(screen, (111, 92, 82), (x1 - 0.1 * l, y1 + 1.8 * h, 1.2 * l, 0.2 * l))


def puts(x1, y1, l, h, u):
    tale = pygame.Surface((l, h))
    tale.set_colorkey('BLACK')
    ellipse(tale, (204, 204, 204), (0, 0, l, h))
    tale2 = pygame.transform.rotate(tale, u)
    screen.blit(tale2, (x1, y1))


def fish(x1, y1, l, h):
    polygon(screen, (229, 75, 87), [(x1 + 0.6 * l, y1 + 1.05 * h), (x1 + 0.9 * l, y1 + 1.05 * h), (x1 + 0.8 * l, y1 + 1.45 * h),
                                    (x1 + 0.9 * l, y1 + 1.6 * h), (x1 + 0.55 * l, y1 + 1.45 * h),
                                    (x1 + 0.65 * l, y1 + 1.18 * h)])

    tale = pygame.Surface((2 * l, 2 * h))
    tale.set_colorkey('BLACK')
    a = []
    b = []
    g = int(l)
    for i in range(g):
        a.append((i, l + h - math.sqrt((h ** 2 / 4 + l ** 2 / 4) ** 1 - (l / 2 - i) ** 2)))
        b.append((l - i, l + math.sqrt((h ** 2 / 4 + l ** 2 / 4) ** 1 - (l / 2 - i) ** 2)))
    c = a + b
    polygon(tale, (140, 175, 168), c)
    tale2 = pygame.transform.rotate(tale, 335)
    screen.blit(tale2, (x1, y1))
    polygon(screen, (140, 175, 168),
            [(x1 + 1.25 * l, y1 + 1.47 * h), (x1 + 1.65 * l, y1 + 1.47 * h), (x1 + 1.45 * l, y1 + 1.72 * h)])
    circle(screen, (103, 9, 251), (x1 + 0.559 * l, y1 + 1.218 * h), 0.08 * l)
    circle(screen, (0, 0, 0), (x1 + 0.559 * l, y1 + 1.21 * h), 0.04 * l)

def cat(x1, y1, l, h):
    puts(x1 - 0.5 * l, y1 + 0.15 * h, 0.85 * l, 0.37 * h, 10)
    puts(x1 - 0.4 * l, y1 + 0.4 * h, 0.85 * l, 0.37 * h, 15)
    puts(x1 + 0.65 * l, y1 + 0.1 * h, 0.85 * l, 0.37 * h, 335)
    puts(x1 + 0.55 * l, y1 + 0.15 * h, 0.85 * l, 0.37 * h, 320)
    puts(x1 + 0.8 * l, y1 - 0.55 * h, 0.9 * l, 0.4 * h, 20)
    ellipse(screen, (204, 204, 204), (x1, y1, l, h))
    fish(x1 - 0.5 * l, y1 - 1.5 * h, 0.4 * l, 1.3 * h)
    ellipse(screen, (204, 204, 204), (x1 - 0.2 * l, y1 - 0.6 * h, 0.5 * l, 0.9 * h))
    ellipse(screen, (255, 255, 255), (x1 - 0.16 * l, y1 - 0.37 * h, 0.09 * l, 0.199 * h))
    ellipse(screen, (0, 0, 0), (x1 - 0.12 * l, y1 - 0.335 * h, 0.05 * l, 0.05 * l))
    ellipse(screen, (255, 255, 255), (x1 + 0.02 * l, y1 - 0.33 * h, 0.09 * l, 0.199 * h))
    ellipse(screen, (0, 0, 0), (x1 + 0.024 * l, y1 - 0.31 * h, 0.05 * l, 0.05 * l))
    polygon(screen, (204, 204, 204),
            [(x1 - 0.02 * l, y1 - 0.8 * h), (x1 - 0.09 * l, y1 - 0.55 * h), (x1 + 0.07 * l, y1 - 0.5 * h)])
    polygon(screen, (204, 204, 204),
            [(x1 + 0.17 * l, y1 - 0.8 * h), (x1 + 0.06 * l, y1 - 0.55 * h), (x1 + 0.2 * l, y1 - 0.5 * h)])
    circle(screen, (0, 0, 0), (x1 - 0.04 * l, y1 - 0.03 * h), 0.025 * l)
    polygon(screen, (255, 255, 255),
            [(x1 - 0.16 * l, y1 + 0.11 * h), (x1 - 0.13 * l, y1 + 0.15 * h), (x1 - 0.15 * l, y1 + 0.19 * h)])
    polygon(screen, (255, 255, 255),
            [(x1 - 0.07 * l, y1 + 0.238 * h), (x1 - 0.04 * l, y1 + 0.25 * h), (x1 - 0.065 * l, y1 + 0.3 * h)])


FPS = 30

screen.fill("white")
rect(screen, (220, 220, 220), (0, 0, 700, 500))

yourta(50, 450, 400, 350)
esquimos(500, 600, 150, 120, 0)
cat(150, 800, 120, 48)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
