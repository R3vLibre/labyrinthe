#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

class Spec_Ecran(object):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def resolution(self):
        return (self.largeur, self.hauteur)

    def print_spec(self):
        print "largeur=" + str(self.largeur)
        print "hauteur=" + str(self.hauteur)
        print "resolution=" + str(self.resolution())

def_ecran = Spec_Ecran(800, 600)
def_ecran.print_spec()

class Interface_Sorties(object):
    def __init__(self):
        pygame.init()
        ecran = pygame.display.set_mode(def_ecran.resolution())
        fond = pygame.Surface(ecran.get_size())
        image_fond = pygame.image.load("../assets/ground.png")
        image_fond.convert()

        ecran.blit(image_fond, (0,0))
        pygame.display.flip()

