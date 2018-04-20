import curses
import math
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

class Navires:
    """Classe de navires"""

    def __init__(self, name):
        self.name = name
        self.navires = []
        self.etat = ['T', 'C', 'R', 'G']

    #Récupère tous les navires du fichier txt
    def init_navires(self, fichier):
        f = open(fichier, 'r')
        self.navires = [line.rstrip() for line in f]
        print(self.navires)
        f.close()


nav = Navires('test')
nav.init_navires('navires.txt')

class Grille:
    """Grille de Jeu"""
    
    def __init__(self, name):
        self.name = name
        self.x = ['A','B','C','D','E','F','G','H','I','J']
        self.y = ['1','2','3','4','5','6','7','8','9','10']
    
    #def init_grille():
    #    for index,lettre in enumerate(self.x)
    #        self.coordX.append(tuple(lettre,index))
    #    print(coordX)

    def afficher_grille(self):

        curses.initscr()
        win = curses.newwin(23, 41, 0, 0)
        win.keypad(1)
        win.border(0)
        win.nodelay(1)


        win2 = curses.newwin(23, 41, 0, 60)
        win2.keypad(1)
        win2.border(0)
        win2.nodelay(1)

        curses.noecho()
        curses.curs_set(0)

        key = KEY_RIGHT  

        while key != 27:               # While Esc key is not pressed
            win.border(0)              # Printing 'Score' and
            win.addstr(0, 16, ' GENTIL ')  

            #Grille
            for y in range(0, 20, 2):
                for x in range(0, 40, 4):
                    if x > 0 :
                        win.addstr(y+2, x, '|')
                        if y < 20 and y > 0:
                            win.addstr(y+1, x-1, '---')

            #Bateau
            for y in range(0, 20, 2):
                for x in range(0, 40, 4):
                        win.addch(y+2, x+2, '~')


            win2.border(0)             
            win2.addstr(0, 16, ' MECHANT')  

            #Grille
            for y in range(0, 20, 2):
                for x in range(0, 40, 4):
                    if x > 0 :
                        win2.addstr(y+2, x, '|')
                        if y < 20 and y > 0:
                            win2.addstr(y+1, x-1, '---')

            #Bateau
            for y in range(0, 20, 2):
                for x in range(0, 40, 4):
                        win2.addch(y+2, x+2, '~')


            prevKey = key                                                  # Previous key pressed
            event = win.getch()
            event2 = win2.getch()
            key = key if event == -1 else event 
            key = key if event2 == -1 else event2 

        curses.endwin()

grille = Grille('test')
grille.afficher_grille()