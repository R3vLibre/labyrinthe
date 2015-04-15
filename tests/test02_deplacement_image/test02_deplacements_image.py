# -*- coding: utf-8 -*-
import sys, os
print sys.path[0]
sys.path.append(os.path.join(sys.path[0], "../../src/"))
print sys.path
import laby_interface as interface
import time

def main():
    print "mise en marche du module de test : simulation du moteur"

    print "Appelle de l'interface d'entrée :"
    teste_if_entree = interface.Interface_Entrees()
    print "test d'élément de jeu, appelle de l'interface de sortie :"
    teste_if_sortie = interface.Interface_Sorties()
    jeu_actif = True
    print "je suis ici"

    while (jeu_actif):
        time.sleep(0.100)
        actions = teste_if_entree.reception_evenements()
        print actions

        for evt in actions:
            print "jeu_actif d = " + str(jeu_actif)
            if evt == "quitter":
                jeu_actif = False
            if evt == "haut":
                print "haut"
                #deplacement du joueur vers le haut
            if evt == "bas":
                print "bas"
                #deplacement du joueur vers le bas
            if evt == "gauche":
                print "gauche"
                #deplacement du joueur vers la gauche
            if evt == "droite":
                print "droite"
                #deplacement du joueur vers la droite
            print "jeu_actif f = " + str(jeu_actif)
    return

class Element_Jeu(object):
    def __init__(self, nom, position):
        self.categorie = None
        self.nom = nom
        self.position = position
        return

class Joueur(Element_Jeu):
    def __init__(self, nom, position):
        super(Joueur,self).__init__(nom)
        self.categorie = "Joueur"

class Mur(Element_Jeu):
    def __init__(self, nom, position):
        super(Mur,self).__init__(nom)
        self.categorie = "Mur"

class Ennemi(Element_Jeu):
    def __init__(self, nom, position):
        super(Ennemi,self).__init__(nom)
        self.categorie = "Mur"

joueur = Joueur("The Hero", (4,3))
ennemi = Ennemi("Predator", (8,9))
mur1 = Mur("Mur brique", (6,9))
mur2 = Mur("Palissade bois", (7,9))

liste_elements = [joueur, ennemi, mur1, mur2]

#   def
#        test_element = interface.Interface_Sorties()
#        test_sortie_element = test_element.receptionner_element()
#        test_receptionner = test_element.positionner_element()
#   return

if __name__ == '__main__':
    main()