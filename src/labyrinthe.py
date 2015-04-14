#!/usr/bin/env python
# -*- coding: utf-8 -*-

import laby_moteur
import laby_interface_entrees
import laby_interface_sorties
# import laby_monde
# import laby_elements_jeu

def main():
    print "Bienvenu sur notre super jeu de la mort qui tue."
    # laby_monde.init() # initialisé par le moteur
    # laby_elements_jeu.init() # initialisé par le moteur
    laby_moteur.init()
    laby_interface_entrees.init()
    laby_interface_sorties.init()




if __name__ == '__main__':
    main()
