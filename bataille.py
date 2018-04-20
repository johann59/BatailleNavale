import curses

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
        begin_x = 20; begin_y = 7
        height = 5; width = 40
        win = curses.newwin(height, width, begin_y, begin_x)

        win.refresh()

grille = Grille('test')
grille.afficher_grille()
#grille.init_grille()