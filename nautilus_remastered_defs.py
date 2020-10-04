import pygame as pg
from pygame.draw import *
import numpy as np

'''Colours'''
bright_yellow = (255, 255, 0)
sandy_yellow = (243, 233, 21)
brown = (183, 86, 17)
light_brown = (226, 127, 7)
dark_pink = (252, 93, 93)
white = (255, 255, 255)
grey_1 = (155, 166, 155)
blue = (149, 224, 243)
dark_blue = (67, 54, 229)
grey_2 = (61, 61, 61)
purple = (131, 95, 204)
beige = (225, 188, 141)
grey_3 = (63, 71, 32)
grey_4 = (64, 63, 62)
black = (0, 0, 0)

pg.init()

FPS = 30
screen = pg.display.set_mode((600, 400))


'''Background'''

rect(screen, blue, (0, 0, 5000, 170), 0)
rect(screen, dark_blue, (0, 170, 5000, 100), 0)
rect(screen, sandy_yellow, (0, 270, 5000, 150), 0)

'''Stars'''


def star(number_of_rays, r_1, r_2, x_star_0, y_star_0):
    angle = 0
    list_of_star = []
    for i in range(number_of_rays):
        x_star = x_star_0 + r_2 * np.cos(angle)
        y_star = y_star_0 - r_2 * np.sin(angle)
        list_of_star.append((round(x_star), round(y_star)))
        x_star = x_star_0 + r_1 * np.cos(angle + np.pi / number_of_rays)
        y_star = y_star_0 - r_1 * np.sin(angle + np.pi / number_of_rays)
        list_of_star.append((round(x_star), round(y_star)))
        angle += 2 * np.pi / number_of_rays
    polygon(screen, bright_yellow, list_of_star, 0)


star(31, 50, 70, 500, 70)
'''Coast'''
a = []
for i in range(0, 600):
    a.append((i, 260 + 10 * np.sin(i * np.pi / 60)))
a.append((600, 290))
a.append((0, 290))
polygon(screen, sandy_yellow, a, 0)
'''Clouds'''


def cloud(x_cloud, y_cloud, x_cloud_size, y_cloud_size):
    ellipse(screen, white, (x_cloud, y_cloud, 55 * x_cloud_size, 35 * y_cloud_size), 0)
    ellipse(screen, grey_1, (x_cloud, y_cloud, 55 * x_cloud_size, 35 * y_cloud_size), 1)
    ellipse(screen, white, (x_cloud + 40 * x_cloud_size, y_cloud, 55 * x_cloud_size, 35 * y_cloud_size), 0)
    ellipse(screen, grey_1, (x_cloud + 40 * x_cloud_size, y_cloud, 55 * x_cloud_size, 35 * y_cloud_size), 1)
    ellipse(screen, white, (x_cloud - 30 * x_cloud_size, y_cloud + 15 * y_cloud_size,
                            55 * x_cloud_size, 35 * y_cloud_size), 0)
    ellipse(screen, grey_1, (x_cloud - 30 * x_cloud_size, y_cloud + 15 * y_cloud_size,
                             55 * x_cloud_size, 35 * y_cloud_size), 1)
    ellipse(screen, white, (x_cloud + 10 * x_cloud_size, y_cloud + 15 * y_cloud_size,
            55 * x_cloud_size, 35 * y_cloud_size), 0)
    ellipse(screen, grey_1, (x_cloud + 10 * x_cloud_size, y_cloud + 15 * y_cloud_size, 55 * x_cloud_size,
            35 * y_cloud_size), 1)
    ellipse(screen, white, (x_cloud + 55 * x_cloud_size, y_cloud + 15 * y_cloud_size,
            55 * x_cloud_size, 35 * y_cloud_size), 0)
    ellipse(screen, grey_1, (x_cloud + 55 * x_cloud_size, y_cloud + 15 * y_cloud_size, 55 * x_cloud_size,
            35 * y_cloud_size), 1)
    ellipse(screen, white, (x_cloud + 85 * x_cloud_size, y_cloud, 55 * x_cloud_size, 35 * y_cloud_size), 0)
    ellipse(screen, grey_1, (x_cloud + 85 * x_cloud_size, y_cloud, 55 * x_cloud_size, 35 * y_cloud_size), 1)
    ellipse(screen, white, (x_cloud + 100 * x_cloud_size, y_cloud + 15 * y_cloud_size,
                            55 * x_cloud_size, 35 * y_cloud_size), 0)
    ellipse(screen, grey_1, (x_cloud + 100 * x_cloud_size, y_cloud + 15 * y_cloud_size,
                             55 * x_cloud_size, 35 * y_cloud_size), 1)


cloud(60, 95, 1, 1)
cloud(100, 40, 7/11, 1)
cloud(260, 20, 1, 11/7)


def ship(ship_size, x_ship, y_ship):
    ship_body = [(x_ship + 110 * ship_size, y_ship),
                 (x_ship + 85 * ship_size, y_ship + 14 * ship_size)]
    for i in range(100):
        ship_body.append((round(x_ship - 14 * ship_size * np.sin(i*np.pi/(2*100))),
                          round(y_ship + 14 * ship_size * np.cos(i*np.pi/(2*100)))))
    polygon(screen, brown, ship_body, 0)
    polygon(screen, grey_3, [(x_ship, y_ship + 14 * ship_size),
                             (x_ship, y_ship),
                             (x_ship + ship_size, y_ship),
                             (x_ship + ship_size, y_ship + 14 * ship_size)], 0)
    polygon(screen, grey_3, [(x_ship + 85 * ship_size, y_ship + 14 * ship_size),
                             (x_ship + 85 * ship_size, y_ship),
                             (x_ship + 86 * ship_size, y_ship),
                             (x_ship + 86 * ship_size, y_ship + 14 * ship_size)], 0)
    '''Mast'''
    rect(screen, black, (x_ship + 35 * ship_size,
                         y_ship - 35 * ship_size,
                         3 * ship_size,
                         35 * ship_size), 0)
    '''Sail'''
    polygon(screen, beige, [(x_ship + 38 * ship_size, y_ship - 35 * ship_size),
                            (x_ship + 58 * ship_size, y_ship - 18 * ship_size),
                            (x_ship + 43 * ship_size, y_ship - 18 * ship_size)], 0)
    polygon(screen, beige, [(x_ship + 38 * ship_size, y_ship),
                            (x_ship + 58 * ship_size, y_ship - 18 * ship_size),
                            (x_ship + 43 * ship_size, y_ship - 18 * ship_size)], 0)
    polygon(screen, grey_4, [(x_ship + 38 * ship_size, y_ship - 35 * ship_size),
                             (x_ship + 58 * ship_size, y_ship - 18 * ship_size),
                             (x_ship + 43 * ship_size, y_ship - 18 * ship_size)],
            ship_size)
    polygon(screen, grey_4, [(x_ship + 38 * ship_size, y_ship),
                             (x_ship + 58 * ship_size, y_ship - 18 * ship_size),
                             (x_ship + 43 * ship_size, y_ship - 18 * ship_size)],
            ship_size)
    '''Porthole'''
    circle(screen, white,
           (x_ship + 91 * ship_size, y_ship + 5 * ship_size),
           3 * ship_size, 0)
    circle(screen, black, (x_ship + 91 * ship_size,
                           y_ship + 5 * ship_size),
           4 * ship_size,
           ship_size)


ship(1, 165, 180)
ship(2, 330, 200)
'''Umbrellas'''


def umbrella(x_umb_size_1, x_umb_size_2, y_umb_size, x_umb, y_umb):
    rect(screen, light_brown, (x_umb, y_umb, 4 * x_umb_size_1, 110 * y_umb_size))
    polygon(screen, dark_pink, [(x_umb, y_umb),
                                (x_umb - 24 * x_umb_size_2, y_umb + 20 * y_umb_size),
                                (x_umb + + 4 * x_umb_size_1 + 24 * x_umb_size_2, y_umb + 20 * y_umb_size),
                                (x_umb + 4 * x_umb_size_1, y_umb)], 0)
    polygon(screen, grey_2, [(x_umb, y_umb),
                             (x_umb - 18 * x_umb_size_2, y_umb + 20 * y_umb_size),
                             (x_umb - 12 * x_umb_size_2, y_umb + 20 * y_umb_size),
                             (x_umb, y_umb)], 1)
    polygon(screen, grey_2, [(x_umb, y_umb),
                             (x_umb - 12 * x_umb_size_2, y_umb + 20 * y_umb_size),
                             (x_umb - 6 * x_umb_size_2, y_umb + 20 * y_umb_size),
                             (x_umb, y_umb)], 1)
    polygon(screen, grey_2, [(x_umb + 4 * x_umb_size_1, y_umb),
                             (x_umb + 6 * x_umb_size_2 + 4 * x_umb_size_1, y_umb + 20 * y_umb_size),
                             (x_umb + 12 * x_umb_size_2 + 4 * x_umb_size_1, y_umb + 20 * y_umb_size),
                             (x_umb + 4 * x_umb_size_1, y_umb)], 1)
    polygon(screen, grey_2, [(x_umb + 4 * x_umb_size_1, y_umb),
                             (x_umb + 12 * x_umb_size_2 + 4 * x_umb_size_1, y_umb + 20 * y_umb_size),
                             (x_umb + 18 * x_umb_size_2 + 4 * x_umb_size_1, y_umb + 20 * y_umb_size),
                             (x_umb + 4 * x_umb_size_1, y_umb)], 1)
    rect(screen, purple, (x_umb, y_umb, 4 * x_umb_size_1, 22 * y_umb_size), 1)
    polygon(screen, light_brown, [(x_umb - 24 * x_umb_size_2, y_umb + 20 * y_umb_size),
                                  (x_umb + 4 * x_umb_size_1 + 6 * x_umb_size_2, y_umb + 20 * y_umb_size),
                                  (x_umb + 24 * x_umb_size_2 + 4 * x_umb_size_1, y_umb + 20 * y_umb_size),
                                  (x_umb - 24 * x_umb_size_2, y_umb + 20 * y_umb_size)], 0)


umbrella(1, 1, 1, 230, 260)
umbrella(2, 3, 1.5, 100, 230)

pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()
