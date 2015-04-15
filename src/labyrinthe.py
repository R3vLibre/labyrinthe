# -*- coding: utf-8 -*-

import laby_moteur
import laby_interface
# import laby_monde
# import laby_elements_jeu

def main():
    print "Bienvenu sur notre super jeu de la mort qui tue."
    # laby_monde.init() # initialisé par le moteur
    # laby_elements_jeu.init() # initialisé par le moteur
    laby_moteur.Moteur()
    laby_interface.Interface_Entrees()

    laby_interface.Interface_Sorties()

if __name__ == '__main__':
    main()
