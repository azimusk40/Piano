import pygame
import sys


class Bouton:

  def __init__(self, fenetre, position, dimensions, couleur_normale,couleur_active, touche):
    """ Classe représentant un bouton """
    self.fenetre = fenetre
    self.position = position
    self.dimensions = dimensions
    self.couleur_normale = couleur_normale
    self.couleur_active = couleur_active
    self.touche = touche
    self.actif = False

  def dessiner(self):
    """dessine le bouton"""
    if self.actif:
      pygame.draw.rect(self.fenetre, self.couleur_active,
                       (*self.position, *self.dimensions))
    else:
      pygame.draw.rect(self.fenetre, self.couleur_normale,
                       (*self.position, *self.dimensions))

  def activer(self):
    self.actif = True

  def desactiver(self):
    self.actif = False

# Initialisation de Pygame
pygame.init()

# Définition des dimensions de la fenêtre
largeur = 800
hauteur = 700

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
couleur_bouton_normale = (200, 200, 200)
couleur_bouton_active = (100, 100, 100)

# Dimensions des boutons
largeur_bouton = largeur // 6
hauteur_bouton = 1000

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption(
    "Six Boutons avec Touches 'q', 's', 'd', 'f', 'g', 'h'")

# Liste des touches associées aux boutons
touches = ['q', 's', 'd', 'f', 'g', 'h']

# Création des objets Bouton
boutons = [
    Bouton(fenetre, (i * largeur_bouton, 600),
           (largeur_bouton, hauteur_bouton), couleur_bouton_normale,
           couleur_bouton_active, touche) for i, touche in enumerate(touches)
]

# Boucle principale du programme
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    # Gestion des touches enfoncées
    elif event.type == pygame.KEYDOWN:
      for bouton in boutons:
        if event.unicode == bouton.touche:
          bouton.activer()

    # Gestion des touches relâchées
    elif event.type == pygame.KEYUP:
      for bouton in boutons:
        if event.unicode == bouton.touche:
          bouton.desactiver()

  # Effacer l'écran avec une couleur blanche
  fenetre.fill(blanc)

  # Dessiner les boutons
  for bouton in boutons:
    bouton.dessiner()

  # Mettre à jour l'affichage
  pygame.display.flip()

  #control le nombre d'image pas seconde
  pygame.time.Clock().tick(30)
