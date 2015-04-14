#demande les entrees qui ont été maintenues
 
def moteur():
  def (self):
    self.jeu_actif=True
    
  
  
  print "Démarrage de notre démo"
  jeu_actif = True
  pygame.init()
  ecran = pygame.display.set_mode(resolution_ecran)

  fond = pygame.Surface(ecran.get_size())
  fond = fond.convert() #le stockage interne des donnes graphiques de l'image corresponde au stockage des donnes graphiques de la fennetre
  #fond.fill((55,150,200))
  image_fond = pygame.image.load("./assets/fond.jpg")
  fond = image_fond.convert()
  
  ecran.blit(fond,(0,0)) # positionner l'image
  pygame.display.flip()

  while (self.jeu_actif):
    time.sleep(0.100)

    for evt in pygame.event.get():
      if evt.type == locals.QUIT:
	self.jeu_actif = False
      elif evt.type == locals.KEYDOWN and evt.key == locals.K_ESCAPE:
	self.jeu_actif = False
    continue # revient au debout de le boucle (for, while, repeat)
  
  return
