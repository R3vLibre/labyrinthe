# -*- coding: utf-8 -*-

import sys 
import imp

imp.load_source("REAL_ej","../../src/laby_elements_jeu.py")
import REAL_ej

# Module de test
#---------------------------------------------------------------------------------------------------------#

class HerosTest(REAL_ej.Heros):
  def __init__(self,curMap,posTabX,posTabY):
    super(HerosTest,self).__init__(curMap,posTabX,posTabY)
    return

  def deplacer(self,direction):
    print "HerosTest avant depl: (x=" + str(self.x) + ", y="+ str(self.y) + ")"
    print "déplacement vers la/le '" + str(direction) + "'"
    super(HerosTest,self).deplacer(direction) #super(HerosTest) vient chercher le parent du HerosTest pour pointer sur la fonction déplacer()
    print "HerosTest après depl: (x=" + str(self.x) + ", y="+ str(self.y) + ")"
