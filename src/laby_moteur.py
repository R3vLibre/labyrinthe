# -*- coding: utf-8 -*-
#demande les entrees qui ont été maintenues

import laby_interface_entrees as ie
import laby_interface_sorties
import laby_elements_jeu
import laby_monde
import labyrinthe
import time
 
class Moteur(object):
  def __init__(self):
    self.jeu_actif=True

  def commencer(self):
    while (self.jeu_actif):
      time.sleep(0.100)
      action = entrees.reception_evenements()

      if action == "quitter":
        self.jeu_actif = False
#      if action == "haut":
        #deplacement du joueur vers le haut
#      if action == "bas":
        #deplacement du joueur vers le bas
#      if action == "gauche":
        #deplacement du joueur vers la gauche
#      if action == "droite":
        #deplacement du joueur vers la droite


#moteur_jeu = Moteur()
#entrees = ie.Interface_Entrees()
#moteur_jeu.commencer()