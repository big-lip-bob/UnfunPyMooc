"""
Project 1: Jeu labyrinthe
Kovalskiy Yan (570217)
"""

from ast import literal_eval as eval
import turtle # Let me drown
import CONFIGS

"""
Classe d'aide pour représenter les divers types de cases
"""
class Cell:
    Vide, Mur, Sortie, Porte, Item, Visitee = 0, 1, 2, 3, 4, 5

    def __init__(self, kind):
        if kind not in [Cell.Vide, Cell.Mur, Cell.Sortie, Cell.Porte, Cell.Item]: raise "Invalid cell kind"
        self.kind = kind

    def passable(self): return self.kind not in [Cell.Mur, Cell.Porte]
    def visit(self): self.kind = Cell.Visitee

"""
Classe représentant le chateau ainsi que les fonctionnalités
Elle assume le chargement et la creation du plan et aussi le jeu en lui meme
"""
class MazeGame:
    """
    Constructeur principal
    Depuis la configuration fournie, initialise le jeu
    Charge la carte, les objects et portes
    Setup les différents turtles (Plateau, inventaire, annonces)
    """
    def __init__(self, config = CONFIGS):
        self.cfg = config

        # Window Setup
        (self.winW, self.winH) = (480, 480)
        turtle.tracer(0) # Instant drawing
        turtle.setup(self.winW * 1.1, self.winH * 1.1, 0, 0)
        turtle.screensize(self.winW, self.winH, self.cfg.COULEUR_EXTERIEUR)
        turtle.title("Labyrinthe Trivia Python")

        # Different turtle per parts, for easy undo and tracking
        self.castleGfx = MazeGame.makeTurtle()

        self.announcementGfx = MazeGame.makeTurtle()
        self.announcementGfx.goto(self.cfg.POINT_AFFICHAGE_ANNONCES)

        self.inventoryGfx = MazeGame.makeTurtle()
        self.inventoryGfx.setheading(-90)
        self.inventoryGfx.goto(self.cfg.POINT_AFFICHAGE_INVENTAIRE)

        # Game Values
        self.fontKinds = [("Arial", 10, "normal"), ("Arial", 12, "normal"), ("Arial", 14, "bold")]
        self.inventory = []

        # Map & Square Size
        self.map, self.mapW, self.mapH = MazeGame.loadCastle(self.cfg.fichier_plan)

        (minX, minY), (maxX, maxY) = self.cfg.ZONE_PLAN_MINI, self.cfg.ZONE_PLAN_MAXI
        (dtX, dtY) = (maxX - minX, maxY - minY)
        self.cellRatio = min(dtX / self.mapW, dtY / self.mapH)

        self.player = self.cfg.POSITION_DEPART

        # Inventory & Doors
        self.clues = MazeGame.loadTupleRest(self.cfg.fichier_objets)
        self.doors = MazeGame.loadTupleRest(self.cfg.fichier_questions)


    """ Méthode pour créer des turtles prêts """
    @staticmethod
    def makeTurtle():
        drawer = turtle.Turtle()
        drawer.speed("fastest")
        drawer.hideturtle()
        drawer.penup()
        return drawer


    """ Méthode pour charger le plan du chateau """
    @staticmethod
    def loadCastle(file):

        map, w, h = [], None, None
        with open(file, 'r', encoding = "UTF8") as file:
            for line in file:
                row = [Cell(int(cell)) for cell in line.strip().split(' ')]
                if not w: w = len(row)
                elif w != len(row): raise "Uneven map"
                map.append(row)
        h = len(map)

        return (map, w, h)


    """ Méthode pour charger les fichiers objects et portes """
    @staticmethod
    def loadTupleRest(file):
        dico = {}
        with open(file, 'r', encoding = "UTF8") as file:
            for line in file:
                # eval est une tres mauvaise idée dans des fichiers lambda
                (y, x), reste = eval(line)
                dico[(x, y)] = reste
        return dico


    """ Méthode pour obtenir une case en (x, y) """
    def getCell(self, x, y): return self.map[y][x]
    """ Méthode pour vérifier si une coordonée (x, y) fait partie du plan """
    def inBounds(self, x, y): return 0 <= x < self.mapW and 0 <= y < self.mapH


    """ Méthode qui gère les déplacements du joueur (et qui appelle les fonctions items / portes si nécessaire) """
    def movePlayer(self, dx, dy):
        (py, px) = self.player
        (nx, ny) = (px + dx, py - dy)

        if not self.inBounds(nx, ny): return
        cell = self.getCell(nx, ny)

        if cell.passable():
            self.getCell(px, py).visit()
            self.drawSquare(px, py)

            self.player = (ny, nx)
            self.drawPlayer()

            if cell.kind == Cell.Item:
                self.pickUp()

            elif cell.kind == Cell.Sortie:
                self.drawAnnouncements("Bravo, vous avez résolu le labyrinthe", 2)
                self.addItem("Les clés du chateau :)")

        elif cell.kind == Cell.Porte:
            self.tryDoor(nx, ny)


    """ Méthode qui ajoute un item dans l'inventaire """
    def addItem(self, item):
        self.inventory.append(item)
        self.inventoryGfx.forward(24) # 18pt
        self.inventoryGfx.write(self.inventory[-1], font = self.fontKinds[0])


    """ Méthode qui prend un item depuis le plan et l'annonce """
    def pickUp(self):
        (y, x) = self.player
        item = self.clues[(x, y)]
        self.addItem(item)
        self.drawAnnouncements(f"Vous avez trouver un indice: {item}", 1)


    """ Méthode qui dessine une annonce """
    def drawAnnouncements(self, text, fontType):
        self.announcementGfx.clear()
        self.announcementGfx.write(text, font = self.fontKinds[fontType])


    """ Méthode qui gère une porte, l'ouvre si la réponse est bonne, sinon rien """
    def tryDoor(self, dx, dy):
        self.drawAnnouncements("La porte est fermée", 1)
        (question, answer) = self.doors[(dx, dy)]
        attempt = turtle.textinput("Pour m'ouvrir, résout l'énigme", question)
        if attempt and attempt == answer: # .strip() ?
            self.drawAnnouncements("Shazam, ouvre toi!", 1)
            self.getCell(dx, dy).kind = Cell.Vide
            self.drawSquare(dx, dy)
        else:
            self.drawAnnouncements("Mauvaise réponse", 1)
        turtle.listen()


    """ Méthode qui associe les différents controles """
    def bindControls(self):
        turtle.onkeypress(lambda: self.movePlayer( 0,  1), "Up"   )
        turtle.onkeypress(lambda: self.movePlayer( 1,  0), "Right")
        turtle.onkeypress(lambda: self.movePlayer( 0, -1), "Down" )
        turtle.onkeypress(lambda: self.movePlayer(-1,  0), "Left" )


    """ Méthode qui déplace le turtle du plan à la case spécifiée """
    def drawGoto(self, x, y):
        (ox, oy) = self.cfg.ZONE_PLAN_MAXI
        self.castleGfx.goto(ox - (self.mapW - (x + .5)) * self.cellRatio, oy - (y - .5) * self.cellRatio)


    """ Méthode qui dessine la case en (x, y) """
    def drawSquare(self, x, y):
        self.drawGoto(x, y)

        self.castleGfx.shape("square")
        self.castleGfx.shapesize(self.cellRatio / 20)
        self.castleGfx.pencolor(self.cfg.COULEUR_EXTERIEUR)
        self.castleGfx.fillcolor(self.cfg.COULEURS[self.getCell(x, y).kind])
        self.castleGfx.stamp()


    """ Méthode qui dessine l'entièreté du plan """
    def drawMaze(self):
        for y in range(self.mapH):
            for x in range(self.mapW):
                self.drawSquare(x, y)


    """ Méthode qui dessine le joueur """
    def drawPlayer(self):
        self.drawGoto(*reversed(self.player))

        self.castleGfx.shape("circle")
        self.castleGfx.pencolor("black")
        self.castleGfx.shapesize(self.cellRatio * self.cfg.RATIO_PERSONNAGE / 20)
        self.castleGfx.fillcolor(self.cfg.COULEUR_PERSONNAGE)
        self.castleGfx.stamp()


    """ Méthode qui effectue le premier dessin (plan, joueur, annonces, inventaire) """
    def drawInit(self):
        self.drawAnnouncements("Bienvenu dans le Labyrinthe Python", 2)
        self.inventoryGfx.write("Inventaire", font = self.fontKinds[1])
        self.drawMaze()
        self.drawPlayer()


    """ Méthode qui dessine le chateau dans un fichier post-script """
    def render(self): # Niveau 1
        self.drawMaze()
        turtle.getcanvas().postscript(file = "chateau.eps")


    """ Méthode qui fait jouer le jeu """
    def play(self): # Niveau 4
        self.drawInit()
        self.bindControls()
        turtle.listen()
        turtle.mainloop()


MazeGame().play()