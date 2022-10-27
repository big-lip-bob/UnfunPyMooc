import ast
import turtle # Let me drown
import CONFIGS

class Cell:
    Vide, Mur, Sortie, Porte, Item, Visitee = 0, 1, 2, 3, 4, 5

    def __init__(self, kind):
        if kind not in [Cell.Vide, Cell.Mur, Cell.Sortie, Cell.Porte, Cell.Item]: raise "Invalid cell kind"
        self.kind = kind

    def passable(self): return self.kind not in [Cell.Mur, Cell.Porte]
    def visit(self): self.kind = self.Visitee

class MazeGame:
    def __init__(self, config = CONFIGS):
        self.cfg = config

        # Window Setup
        (self.winW, self.winH) = (480, 480)
        turtle.tracer(0) # Instant drawing
        turtle.setup(self.winW * 1.1, self.winH * 1.1, 0, 0)
        turtle.screensize(self.winW, self.winH, self.cfg.COULEUR_EXTERIEUR)
        turtle.title("Labyrinthe Trivia Python")

        # Turtle Setups
        self.bindControls()

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
        (dX, dY) = (maxX - minX, maxY - minY)
        self.cellRatio = min(dX / self.mapW, dY / self.mapH)

        self.player = self.cfg.POSITION_DEPART

        # Inventory & Doors
        self.clues = MazeGame.loadObjects(self.cfg.fichier_objets)
        self.doors = MazeGame.loadDoors(self.cfg.fichier_questions)

    @staticmethod
    def makeTurtle():
        drawer = turtle.Turtle()
        drawer.speed("fastest")
        drawer.hideturtle()
        drawer.penup()
        return drawer

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

    @staticmethod
    def loadObjects(file):
        dico = {}
        with open(file, 'r', encoding = "UTF8") as file:
            for line in file:
                # eval est une tres mauvaise idée dans des fichiers lambda
                (y, x), indice = ast.literal_eval(line)
                dico[(x, y)] = indice
        return dico

    @staticmethod
    def loadDoors(file):
        dico = {}
        with open(file, 'r', encoding="UTF8") as file:
            for line in file:
                # eval est une tres mauvaise idée dans des fichiers lambda
                (y, x), (question, reponse) = ast.literal_eval(line)
                dico[(x, y)] = (question, reponse)
        return dico

    def movePlayer(self, dx, dy):
        (py, px) = self.player
        (nx, ny) = (px + dy, py - dx)

        if self.inBounds(nx, ny):
            cell = self.getCell(nx, ny)

            if cell.passable():
                self.getCell(px, py).visit()
                self.drawSquare(px, py)

                self.player = (ny, nx)
                self.drawPlayer()

                if cell.kind == Cell.Item:
                    self.pickUp()

                elif cell.kind == Cell.Sortie:
                    self.drawAnnouncements("Bravo, vouz avez résolu le labyrinthe", 2)
                    self.addItem("Les clés du chateau :)")

            elif cell.kind == Cell.Porte:
                self.tryDoor(nx, ny)

    def addItem(self, item):
        self.inventory.append(item)
        self.inventoryGfx.forward(24) # 9pt
        self.inventoryGfx.write(self.inventory[-1], font=self.fontKinds[0])

    def pickUp(self):
        (y, x) = self.player
        item = self.clues[(x, y)]
        self.addItem(item)
        self.drawAnnouncements(f"Vous avez trouver un indice: {item}", 1)


    def tryDoor(self, dx, dy):
        self.drawAnnouncements("La porte est fermée", 1)
        (question, answer) = self.doors[(dx, dy)]
        attempt = turtle.textinput("Pour m'ouvrir, résout l'énigme", question)
        if attempt and attempt.strip() == answer:
            self.drawAnnouncements("Shazam, ouvre toi!", 1)
            self.getCell(dx, dy).kind = Cell.Vide
            self.drawSquare(dx, dy)
        else:
            self.drawAnnouncements("Mauvaise réponse", 1)

        turtle.listen()


    def bindControls(self):
        # for i in range(4): (dx, dy) = (-dy, dx) # Python qui n'a pas la notion de scopes autre que les fonctions?!?!
        #   turtle.onkeypress(lambda: self.movePlayer(dx, dy), ("Down", "Right", "Up", "Left")[i])
        turtle.onkeypress(lambda: self.movePlayer( 1,  0), "Up"   )
        turtle.onkeypress(lambda: self.movePlayer( 0,  1), "Right")
        turtle.onkeypress(lambda: self.movePlayer(-1,  0), "Down" )
        turtle.onkeypress(lambda: self.movePlayer( 0, -1), "Left" )

    def getCell(self, x, y): return self.map[y][x]
    def inBounds(self, x, y): return 0 <= x < self.mapW and 0 <= y < self.mapH

    def drawGoto(self, x, y):
        (ox, oy) = self.cfg.ZONE_PLAN_MAXI
        self.castleGfx.goto(ox - (self.mapW - (x + .5)) * self.cellRatio, oy - (y - .5) * self.cellRatio)

    def drawSquare(self, x, y):
        self.drawGoto(x, y)

        self.castleGfx.shape("square")
        self.castleGfx.pencolor(self.cfg.COULEUR_EXTERIEUR)
        self.castleGfx.shapesize(self.cellRatio / 20)
        self.castleGfx.fillcolor(self.cfg.COULEURS[self.getCell(x, y).kind])
        self.castleGfx.stamp()

    def drawPlayer(self):
        self.drawGoto(*reversed(self.player))

        self.castleGfx.shape("circle")
        self.castleGfx.pencolor("black")
        self.castleGfx.shapesize(self.cellRatio * self.cfg.RATIO_PERSONNAGE / 20)
        self.castleGfx.fillcolor(self.cfg.COULEUR_PERSONNAGE)
        self.castleGfx.stamp()

    def drawMaze(self):
        for y in range(self.mapH):
            for x in range(self.mapW):
                self.drawSquare(x, y)

    def drawAnnouncements(self, text, fontType):
        self.announcementGfx.undo()
        self.announcementGfx.write(text, font = self.fontKinds[fontType])

    def drawInit(self):
        self.announcementGfx.write("Bienvenu dans le Labyrinthe Python", font = self.fontKinds[2])
        self.inventoryGfx.write("Inventaire", font = self.fontKinds[1])
        self.drawMaze()
        self.drawPlayer()

    def render(self): # Niveau 1
        self.drawMaze()
        turtle.getcanvas().postscript(file = "chateau.eps")

    def play(self): # Niveau 4
        self.drawInit()
        turtle.listen()
        turtle.mainloop()

MazeGame().play()