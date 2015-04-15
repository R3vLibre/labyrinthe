# -*- coding: utf-8 -*-

class Element_Jeu(object):
  def __init__(self,curMap,posTabX,posTabY):
    self.mobile = False
    self.x = posTabX
    self.y = posTabY
    self.curMap = curMap

  def deplacer(self,direction):
    print("impossible de se déplacer vers la/le "+direction)

 
class Heros(Element_Jeu):
  def __init__(self,curMap,posTabX,posTabY):
    super(Heros,self).__init__(curMap,posTabX,posTabY)
    self.mobile = True

  def deplacer(self,direction):
    # rechercher la position de la nouvelle case
    if direction == "droite":
      self.x = self.x+1
    if direction == "gauche":
      self.x = self.x-1   
    if direction == "haut":
      self.y = self.y-1
    if direction == "bas":
      self.y = self.y+1

class Mur(Element_Jeu):
  def __init__(self,curMap,posTabX,posTabY):
    super(Mur,self).__init__(curMap,posTabX,posTabY)
    return
    
