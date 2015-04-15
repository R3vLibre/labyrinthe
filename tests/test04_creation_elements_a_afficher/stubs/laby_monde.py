# -*- coding: utf-8 -*-
# Module de test

import sys 
import imp

imp.load_source("REAL_Monde","../../src/laby_monde.py")
from REAL_Monde import *


class MondeTest(Monde):
  def __init__(self):
    self.heros = laby_elements_jeu.HerosTest(0,11,11)