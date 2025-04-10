import random as rd
import pygame as pg
import pygame_gui
from pygame_gui.elements import UILabel,UIButton
import sys

def creat_pwd(n_letter, n_number, n_cs):
    number = [n_letter, n_number, n_cs]
    cara = ["abcdefgijklmnopqrstuvwxyz","0123456789","*-/+%$#_"]
    index = 0
    c = []
    for i in cara:
        for n in range(number[index]):
            c.append(rd.choice(list(i)))
        index += 0
    rd.shuffle(c)
    return "".join(c)

class App:
    def __init__(self):
        pg.init()
        self.size = (1000,800)
        self.screen = pg.display.set_mode(self.size)
        self.UImanager = pygame_gui.UIManager(self.size)
        self.UI_n_letter_place = [800,350]
        self.n_letter = 0
        self.UI_n_letter = [UILabel(relative_rect= pg.Rect(self.UI_n_letter_place[0],self.UI_n_letter_place[1],50,50),text = str(self.n_letter),manager= self.UImanager),
                            UIButton(relative_rect= pg.Rect(self.UI_n_letter_place[0]+50,self.UI_n_letter_place[1],50,25),text = "UP",manager= self.UImanager),
                            UIButton(relative_rect= pg.Rect(self.UI_n_letter_place[0]+50,self.UI_n_letter_place[1]+25,50,25),text = "DOWN",manager= self.UImanager)
                            ]

    def run(self):
        clock = pg.time.Clock()
        while True:
            time_delta = clock.tick(20)
            pg.draw.rect(self.screen, (0,0,0), pg.Rect(0, 0, self.size[0], self.size[1]))
            pg.draw.rect(self.screen, (200,50,0), pg.Rect(700, 0, 300, self.size[1]))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()

                if not self.UImanager.process_events(event):
                    if event.type == pygame_gui.UI_BUTTON_PRESSED:
                        if event.ui_element is self.UI_n_letter[1]:
                            self.n_letter += 1
                            self.UI_n_letter[0].set_text(str(self.n_letter))
                        if event.ui_element is self.UI_n_letter[2]:
                            if self.n_letter > 0:
                                self.n_letter -= 1
                            self.UI_n_letter[0].set_text(str(self.n_letter))

            self.UImanager.update(time_delta/1000)
            self.UImanager.draw_ui(self.screen)

            pg.display.flip()

App().run()
    
        



