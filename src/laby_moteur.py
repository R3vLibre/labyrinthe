# -*- coding: utf-8 -*-
#demande les entrees qui ont été maintenues
import time

import laby_interface as i_f
import laby_elements_jeu
import laby_monde

class Moteur(object):
  def __init__(self, entrees):
    self.jeu_actif = True
    self.monde = laby_monde.Monde()
    # entrees clavier
    self.entrees = entrees

  def commencer(self):
    while (self.jeu_actif):
      time.sleep(0.100)
      actions = self.entrees.reception_evenements()
      print actions
      
      for act in actions:

        if act == "quitter":
          self.jeu_actif = False
        elif act in i_f.actions_deplacements:
          print(act)
          self.monde.heros.deplacer(act)
