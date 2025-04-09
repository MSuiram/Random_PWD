import random as rd
import pygame as pg
import sys

def creat_pwd(n_letter, n_number, n_cs):
    number = [n_letter, n_number, n_cs]
    cara = ["abcdefgijklmnopqrstuvwxyz","0123456789","*-/+%$#_"]
    index = 0
    c = []
    for i in cara:
        for n in range(number[index]):
            c.append(rd.choice(list(i)))
        index += 1
    rd.shuffle(c)
    return "".join(c)

class App:
    def __init__(self):
        pg.init()
        self.size = (1200,900)
        self.screen = pg.display.set_mode(self.size)

    def run(self):
        clock = pg.time.Clock()
        while True:
            clock.tick(20)
            pg.draw.rect(self.screen, (rd.randint(0,255),rd.randint(0,255),rd.randint(0,255)), pg.Rect(0, 0, self.size[0], self.size[1]))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

            pg.display.flip()

App().run()
    
        



