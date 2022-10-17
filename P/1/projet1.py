from random import randint, seed
from messages import *

""" Functions """
def range_ask(prompt, min, max):
    """
    Fonction utilitaire pour faciliter l'épuration de l'entrée pour être comprise dans une borne donnée

    :param prompt: La sequence qui va être imprimée lors de la demande (formattée avec min et max)
    :param min: Borne minimum pour l'entrée
    :param max: Borne maximum pour l'entrée
    :return: l'entrée utilisateur comprise entre min et max inclus
    """
    while True:
        try:
            while not min <= (num := int(input(prompt.format(min = min, max = max)))) <= max:
                print(f"Veuillez entrez un nombre entre {min} et {max}!")
            return num
        except ValueError:
            print(f"Veuillez entrez un nombre valide!")

def ai_turn(billes_sac):
    """
    Retourne le nombre de billes que l'IA choisira
    Si le nombre de billes peut être remit sur un multiple de 5 moins un, l'IA mettra en priorité ce choix
    Sinon l'IA prendra entre 1 et 2 billes aléatoirement (30%)

    :param billes_sac: Billes restantes dans le sac
    :return: Billes prises
    """
    return (billes_sac - 1) % 5 or 1 + (7 <= billes_sac and 70 < randint(1, 100))

""" Settings """
min_billes_sac = 6
max_billes_sac = 40

min_billes_turn = 1
max_billes_turn = 4

""" Bienvenue """
print(message_1)

""" UPyLab Setup """
upylab = True

if upylab:
    import sys

    sys.path.append("/pub/code")
    seed(int(input(entree_1)))

""" Game Classes """

class Player:
    """
    Classe pour les messages et fonctions tirages pour le joueur
    """
    turn_greet = message_4 # A toi de jouer, n billes
    take_turn = lambda billes_sac: range_ask(entree_3, min_billes_turn, min(billes_sac, max_billes_turn)) # "Retirez entre {min} et {max} billes: "
    turn_summary = None
    next_turn = message_5 # Il reste n billes
    lose = message_9 # Une seule bille, perdu
    suicide = "Si pres du but, pourtant vous aviez perdu" # :(

class Robot:
    """
        Classe pour les messages et fonctions tirages de l'IA
    """
    turn_greet = message_6 # Tour de l'IA
    take_turn = ai_turn # Logique IA
    turn_summary = message_7 # n billes retirées par l'IA
    next_turn = None
    lose = message_8 # Une seule bille, gagné
    suicide = "Les robots sont encore et toujours aussi bêtes" # Impossible

""" Main Loop """

while True:
    print(message_2) # Rappel des Regles

    billes_sac = range_ask(entree_2, min_billes_sac, max_billes_sac) # "Billes dans le sac [{min}; {max}]: "

    print(message_3) # Partie commence

    while True:
        for player in [Player, Robot]: # Alterner entre jouer et robot

            if billes_sac == 1: # Si on se retrouve a devoir piocher une bille, on a forcément perdu
                print(player.lose)
                break

            print(player.turn_greet.format(billes_sac))

            retirees = player.take_turn(billes_sac)
            billes_sac -= retirees

            if player.turn_summary: print(player.turn_summary.format(retirees))

            if billes_sac == 1: continue
            elif billes_sac <= 0: # si pour une raison vous décidez de vous suicider avec moins de 5 billes
                print(player.suicide)
                break

            if player.next_turn: print(player.next_turn.format(billes_sac))

        else: continue; break

    if input(entree_4).lower() != "oui": break # OUI Oui oUi ouI OUi OuI oUI oui
