#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys, os
print sys.path[0]
sys.path.append(os.path.join(sys.path[0], "../src/"))
print sys.path
import laby_interface as interface
import pygame.locals as locals
import time
import pygame

def main():
    print "Mise en marche du module de teste"
    teste_if_entree = interface.Interface_Entrees()
    print "Appelle de l'interface d'entrée"
    teste_if_sortie = interface.Interface_Sorties()
    print "Appelle de l'interface de sortie"
    jeu_actif = True

    while (jeu_actif):
        time.sleep(0.100)
        actions = teste_if_entree.reception_evenements()

        for evt in actions:
            if evt == "quitter":
                jeu_actif = False

    return

if __name__ == '__main__':
    main()