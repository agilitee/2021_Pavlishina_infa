import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill("white")
circle(screen, (255, 255, 0), (200, 200), 170)
circle(screen, (255, 0, 0), (110, 150), 30)
circle(screen, (255, 0, 0), (290, 150), 20)
circle(screen, (0, 0, 0), (110, 150), 10)
circle(screen, (0, 0, 0), (290, 150), 7)
rect(screen, (0, 0, 0), (110, 300, 180, 30))
polygon(screen, (0, 0, 0), [(25, 30), (170, 145), (165, 155), (20, 40)])
polygon(screen, (0, 0, 0), [(230, 145), (375, 50), (380, 60), (240, 155)])

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
