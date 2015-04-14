# -*- coding: utf-8 -*-
import pygame
import pygame.locals as locals #raccourcis

#initialisation de l'affichage de l'interface.
#le module sera chargé une seule fois même si imports multiples.

resolution_affichage = (800, 600)
pygame.init()
ecran = pygame.display.set_mode(resolution_affichage)

#background :

loc_img = "../assets/"

images = {"background":"ground.png",
          "joueur":"imagedujoueur.png",
          "mur":"imagedemur.png",
          "ennemi":"ennemi.png" }


#liste_actions = ["gauche","droite","haut","bas","quitter"]

class Interface_Entrees(object):
    def __init__(self):
        self.actions = []

    def reception_evenements(self):
        for evt in pygame.event.get():
            print evt
            if evt.type == locals.QUIT:
                self.actions.append("quitter")
            elif evt.type == locals.KEYDOWN:
                if evt.key == locals.K_ESCAPE:
                    self.actions.append("quitter")
                if evt.type == locals.K_UP:
                    self.actions.append("haut")
                if evt.type == locals.K_DOWN:
                    self.actions.append("bas")
                if evt.type == locals.K_LEFT:
                    self.actions.append("gauche")
                if evt.type == locals.K_RIGHT:
                    self.actions.append("droite")
        return self.actions

class Interface_Sorties(object):
    def __init__(self):
        image_fond = pygame.image.load(loc_img + images["background"])
        image_fond.convert()

        ecran.blit(image_fond, (0,0))


        pygame.display.flip()