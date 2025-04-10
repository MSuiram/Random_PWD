import random as rd
import pygame as pg
import pygame_gui
from pygame_gui.elements import UILabel,UIButton,UITextEntryLine
import sys
import pyperclip

class Choice_number:
    def __init__(self, place : list, UImanager, name : str):
        self.UImanager = UImanager
        self.place = place
        self.name = name
        self.n = 0
        self.UI = [UILabel(relative_rect= pg.Rect(self.place[0]+50,self.place[1]+50,50,50),text = str(self.n),manager= self.UImanager),
                   UIButton(relative_rect= pg.Rect(self.place[0]+100,self.place[1]+50,50,25),text = "UP",manager= self.UImanager),
                   UIButton(relative_rect= pg.Rect(self.place[0]+100,self.place[1]+75,50,25),text = "DOWN",manager= self.UImanager),
                   UILabel(relative_rect= pg.Rect(self.place[0],self.place[1],200,50),text = self.name,manager= self.UImanager)
                   ]
    
    def number(self):
        return self.n
    
    def Up(self):
        self.n += 1
        self.UI[0].set_text(str(self.n))
    
    def Down(self):
        if self.n > 0:
            self.n -= 1
        self.UI[0].set_text(str(self.n))

class App:
    def __init__(self):
        pg.init()
        self.pwd = ""
        self.size = (1000,600)
        self.screen = pg.display.set_mode(self.size)
        self.UImanager = pygame_gui.UIManager(self.size)
        self.UIChoice_number = [Choice_number([750,50],self.UImanager,"Nombre de lettre"),Choice_number([750,200],self.UImanager,"Nombre de chiffre"),Choice_number([750,350],self.UImanager,"Nombre de caractère spécial")]
        self.UIButton = UIButton(relative_rect = pg.Rect(750,500,200,50), text = "Générer", manager= self.UImanager)
        self.UILabel = UITextEntryLine(relative_rect = pg.Rect(150,150,400,100), initial_text= "Clicer sur Générer", manager= self.UImanager)
        self.UIPaperclip = UIButton(relative_rect = pg.Rect(150,350,400,100), text= "Copier dans le presse papier", manager= self.UImanager)

    def creat_pwd(self, n_letter, n_number, n_cs):
        number = [n_letter, n_number, n_cs]
        cara = ["abcdefgijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ","0123456789","*-/+%$#_"]
        index = 0
        c = []
        for i in cara:
            for n in range(number[index]):
                c.append(rd.choice(list(i)))
            index += 1
        rd.shuffle(c)
        return "".join(c)

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
                        for i in range(len(self.UIChoice_number)):
                            if event.ui_element is self.UIChoice_number[i].UI[1]:
                                self.UIChoice_number[i].Up()
                            if event.ui_element is self.UIChoice_number[i].UI[2]:
                                self.UIChoice_number[i].Down()
                        
                        if event.ui_element is self.UIButton:
                            self.pwd = str(self.creat_pwd(self.UIChoice_number[0].n,self.UIChoice_number[1].n,self.UIChoice_number[2].n))
                            self.UILabel.set_text(self.pwd)
                        if event.ui_element is self.UIPaperclip:
                            pyperclip.copy(self.pwd)

            self.UImanager.update(time_delta/1000)
            self.UImanager.draw_ui(self.screen)

            pg.display.flip()

App().run()
    
        



