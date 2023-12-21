import pygame
import sys
import os
from classe import *
import pygame.mixer

# Initialisation de Pygame
pygame.init()
jeu = True

# Définition des dimensions de la fenêtre
largeur = 1280
hauteur = 720

# Couleurs
blanc = (255, 255, 255)
noir = (0, 0, 0)
couleur_bouton_normale = (224, 224, 224)
couleur_bouton_active = (106, 106, 106)

# Dimensions des boutons
largeur_bouton = largeur // 9
hauteur_bouton = 150

# Création de la fenêtre
fenetre = pygame.display.set_mode((largeur, hauteur))
image = loadify("image/fond.png")

pygame.display.set_caption("Piano Game")

# Liste des touches associées aux boutons
touches = ['q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']

# Chargement des sons
sons = {touche: pygame.mixer.Sound(f"son/{touche}.wav") for touche in touches}

# Création des objets Bouton
boutons = [
    Bouton(fenetre, (i * largeur_bouton, hauteur - hauteur_bouton),
           (largeur_bouton, hauteur_bouton), couleur_bouton_normale,
           couleur_bouton_active, touche) for i, touche in enumerate(touches)
]
compteurs_touches = {touche: 0 for touche in touches}
notes = [Note(fenetre, touche, positions_y) for touche in touches]


open_csv_music()
open_csv_note()
open_csv_pos()

# Boucle principale du programme
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

    # compteurs des touches enfoncées
    elif event.type == pygame.KEYDOWN:
      for bouton in boutons:
        if event.unicode == bouton.touche:
          bouton.activer()
          compteurs_touches[event.unicode] += 1
          print(
              f"Touche {event.unicode} entrée ({compteurs_touches[event.unicode]} fois)"
          )
          # Lecture du son correspondant
          sons[event.unicode].play()

    # Gestion des touches relâchées
    elif event.type == pygame.KEYUP:
      for bouton in boutons:
        if event.unicode == bouton.touche:
          bouton.desactiver()

  # Effacer l'écran avec une couleur blanche
  fenetre.fill(blanc)

  # Blitter l'image du fond sur toute la surface
  fenetre.blit(pygame.transform.scale(image, (largeur, hauteur)), (0, 0))
  pygame.draw.line(fenetre, blanc, (600, 0), (600, hauteur), 2)
  music(fenetre)

  # Dessiner les boutons
  for bouton in boutons:
    bouton.dessiner()

  # Ajouter des lignes blanche horizontales
  for y in range(50, 250, 40):
    pygame.draw.line(fenetre, blanc, (0, y), (largeur, y), 2)

  # Dessiner les notes
  for note in musique:
    note.draw()

  # Mettre à jour l'affichage
  pygame.display.flip()

  # Contrôler le nombre d'images par seconde
  pygame.time.Clock().tick(50)

