# -*- coding: utf-8 -*-
import laby_elements_jeu

# resolution de 800*600
# cases de 50*50

# 0 = Nothing
# 1 = Wall
# 2 = HERO #1
# 3 = Ennemi #1

#tab_static -


class Monde():
  def __init__(self):
    self.heros = laby_elements_jeu.Heros(0,11,11)
    self.curMap = 0
    self.hauteur = len(map_initiale)
    self.largeur = len(map_initiale[0])
    self.elements_a_afficher = []
   
    l=0
    for ligne in map_initiale:
      c=0
      for elem_col in ligne:
        print elem_col
        print str(l)+"   "+str(c)
        if elem_col == 1:
          element = laby_elements_jeu.Mur(self.curMap,l,c)
          self.elements_a_afficher.append(element)
        elif elem_col == 2:
          element = laby_elements_jeu.Heros(self.curMap,l,c)
          self.elements_a_afficher.append(element)
        c=c+1
      l=l+1

map_initiale =\
[
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
  [1,0,0,0,0,0,0,1,0,1,1,0,0,0,0,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,1,1,0,1,0,0,0,1,1,1,1,1,0,1],
  [1,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1],
  [1,0,0,1,1,0,1,1,0,1,0,1,0,1,0,0],
  [1,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0],
  [1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1],
  [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
  [1,0,1,1,1,1,0,1,1,0,1,1,0,2,0,1],
  [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

