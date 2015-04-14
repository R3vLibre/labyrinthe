# -*- coding: utf-8 -*-
import pygame
import pygame.locals as locals #raccourcis

#pygame.init()
#ecran = pygame.display.set_mode((800,600))
#liste_actions = ["gauche","droite","haut","bas","quitter"]


class Interface_Entrees(object):
  def __init__(self):
    self.action = []

  def reception_evenements(self):
    self.action = []
    for evt in pygame.event.get():
      print evt
      if evt.type == locals.QUIT:
        self.action.append["quitter"]
        
      elif evt.type == locals.KEYDOWN:
        if evt.key == locals.K_ESCAPE:
          self.action.append["quitter"]
        if evt.type == locals.K_UP:
          self.action.append["haut"]
        if evt.type == locals.K_DOWN:
          self.action.append["bas"]
        if evt.type == locals.K_LEFT:
          self.action.append["gauche"]
        if evt.type == locals.K_RIGHT:
          self.action.append["droite"]