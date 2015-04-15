# -*- coding: utf-8 -*-
import pygame
import pygame.locals as locals #raccourcis

actions_deplacements = ["gauche","droite","haut","bas","quitter"]


class Interface_Entrees(object):
  def __init__(self):
    return
  
  def reception_evenements(self):
    actions = []
    for evt in pygame.event.get():
      
      if evt.type == locals.QUIT:
        actions.append("quitter")

      elif evt.type == locals.KEYDOWN:
        if evt.key == locals.K_ESCAPE:
          actions.append("quitter")
        if evt.key == locals.K_UP:
          actions.append("haut")
        if evt.key == locals.K_DOWN:
          actions.append("bas")
        if evt.key == locals.K_LEFT:
          actions.append("gauche")
        if evt.key == locals.K_RIGHT:
          actions.append("droite")
        #print evt.key
    return actions
