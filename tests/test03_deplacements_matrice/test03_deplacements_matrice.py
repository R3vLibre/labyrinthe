# -*- coding: utf-8 -*-
# Module de test

import sys
import os

# sys.path[0] -> chemin d'ou le fichier main est lancé
sys.path.append(os.path.join(sys.path[0],"stubs"))
sys.path.append(os.path.join(sys.path[0],"../../src/"))

import pygame

import laby_interface_entrees as i_e
import laby_interface_sorties as i_s
import laby_moteur



def main():
  
  #-----init-ecran-et-pygame-----#

  pygame.init()
  ecran = pygame.display.set_mode((800,600))

  #----------START test avec stubs ----------#

  entrees = i_e.Interface_Entrees()
  moteur_jeu = laby_moteur.Moteur(entrees)
  moteur_jeu.commencer()

if(__name__ == "__main__"):
  main()