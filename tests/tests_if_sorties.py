#!/usr/bin/env python
# -*- coding: utf-8 -*-


import sys, os
print sys.path[0]
sys.path.append(os.path.join(sys.path[0], "../src/"))
print sys.path
import laby_interface_sorties as if_sorties
import pygame.locals as locals
import time
import pygame

def main():
    print "Mise en marche du module de teste"
    teste_if = if_sorties.Interface_Sorties()
    jeu_actif = True

    while (jeu_actif):
        time.sleep(0.100)

        # Gestion des évènments

        for evt in pygame.event.get():
            if evt.type == locals.QUIT:
                jeu_actif = False
            elif evt.type == locals.KEYDOWN and evt.key == locals.K_ESCAPE:
                jeu_actif = False
            continue
    return

if __name__ == '__main__':
    main()