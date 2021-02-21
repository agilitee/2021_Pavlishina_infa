import pygame
import math
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((800, 800))
x1 = 30
y1 = 30
l = 60
h = 160
polygon(screen, (229, 75, 87), [(x1 + 0.3*l, y1 + 1*h), (x1 + 0.9*l, y1 + 1*h), (x1 + 0.8*l, y1 + 2*h), (x1 + 1.6*l, y1 + 2.18*h), (x1+ 0.6*l, y1 + 2.18*h), (x1 + 0.5*l, y1 + 1.18*h)])

FPS = 30

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
