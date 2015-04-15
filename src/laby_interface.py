# -*- coding: utf-8 -*-
import pygame
import pygame.locals as locals #raccourcis

#initialisation de l'affichage de l'interface.
#le module sera chargé une seule fois même si imports multiples.

resolution_affichage = (800, 600)
pygame.init()
ecran = pygame.display.set_mode(resolution_affichage)

#les images :

loc_img = "../assets/"

images = {"background":"ground.png",
          "Joueur":"player.png",
          "Mur":"wall.png",
          "Ennemi":"enemi.png" }


actions_deplacements = ["gauche","droite","haut","bas","quitter"]

class Interface_Entrees(object):
    def __init__(self):
        return

    def reception_evenements(self):
        actions = []
        for evt in pygame.event.get():
            if evt.type == locals.QUIT:
                actions.append("quitter")
            elif evt.type == locals.KEYDOWN:
                if evt.key == locals.K_ESCAPE:
                    actions.append("quitter")
                if evt.key == locals.K_UP:
                    actions.append("haut")
                if evt.key == locals.K_DOWN:
                    actions.append("bas")
                if evt.key == locals.K_LEFT:
                    actions.append("gauche")
                if evt.key == locals.K_RIGHT:
                    actions.append("droite")
        return actions

class Interface_Sorties(object):
    def __init__(self):
        # Liste des éléments à afficher: (image_source, (posy,posx))
        self.a_afficher = []
        self.ref_img = {}
        self.preparer_background()

        self.actualiser_affichage()
        return

    def preparer_background(self):
        self.image_fond = pygame.image.load(loc_img + images["background"])
        self.image_fond = self.image_fond.convert()
        self.a_afficher.append((self.image_fond, (0,0)))


# Qu'a besoin le moteur ?
# Qu'a besoin l'interface ?
    # la désigation de l'élément pour savoir quelle image afficher.
        # ---> element : dictionnaire ?             elements = {"joueur":(0,0) , "ennemi":(5,7), "mur": [(4,4), (6,9)]}
        # elements = [ Joueur("Joueur", (4,7)), Ennemi("Ennemi", (5,7)),
    # les coordonnées de l'élément pour pouvoir l'afficher.

    def preparer_affichage(self, elements):
        print "à quoi est-ce que je ressemble ?"

        print elements
        for elem in elements:
            print elem.categorie + "  Nom=" +elem.nom
            if not self.ref_img.has_key(elem.categorie):
                img_elem = pygame.image.load(loc_img + images[elem.categorie])
                img_elem = img_elem.convert()
                self.ref_img[elem.categorie] = img_elem
            if elem.categorie == "Joueur":
                self.a_afficher.append((img_elem, (120,200)))

    def actualiser_affichage(self):
        print "afficher et réafficher les éléments"
        #ecran.blit(self.image_fond, (0,0))
        for (image, position) in self.a_afficher:
            print "Affichage de " + str(image) + "à " + str(position)
            ecran.blit(image, position)
        pygame.display.flip()
        self.a_afficher = []
        print "vient là"

# 1ère approche n'allant pas avec les autres modules :

# l'interface de sortie prépare le background.
# l'interface de sortie récupère les coordonnées de l'ensemble des cases.
# l'interface de sortie "transforme" les coordonnées en équivalent pixel.
# l'interface de sortie attend l'envoie des coordonnées joueur, ennemi et mur d'élément de jeu.
# l'interface de sortie positionne les éléments.
#   les éléments de jeu ne connaissent pas leurs images ni leur taille dans le monde.
# l'interface de sortie n'a besoin de connaitre que le nom (sorte d'id) des objets à afficher.
# l'interface de sortie déplace le(s) objet(s)

#2ème approche ou l'interface essst plus pacif car c'est le moteur qui l'active.
# c'est le moteur qui agit :
        # initialisation de l'interface de sortie par le moteur.
        # interaction avec le moteur :
            # préparer_background()
            # récupérer_coordonnées_monde()
            # transformer_coordonnées_monde()
            # réceptionner_coordonnées_éléments() <- utilisation de flags ?
            # positionner_éléments()
            # afficher_éléments()
            # déplacer_éléments()
            # réafficher_éléments()


