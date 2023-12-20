import pygame
import sys
import os
import csv
blanc = (255, 255, 255)
noir = (0, 0, 0)
list_position = [-500, 70, 90, 110, 130, 150, 190, 210, 230, 500]
touches = ['q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
musique = []

# Création d'un dictionnaire associant chaque touche à sa position y
liste_positions = []
position_initiale = -183

for _ in range(10):
  liste_positions.append(position_initiale)
  position_initiale += 20
# Création des objets Note
positions_y = {touche: y for touche, y in zip(touches, liste_positions)}


# Affichage du dictionnaire
class Bouton:

  def __init__(self, fenetre, position, dimensions, couleur_normale,
               couleur_active, touche):
    """
        Initialise un objet Bouton.
        """
    self.fenetre = fenetre
    self.position = position
    self.dimensions = dimensions
    self.couleur_normale = couleur_normale
    self.couleur_active = couleur_active
    self.touche = touche
    self.actif = False

    # Créer l'attribut rect pour les interactions avec la souris
    self.rect = pygame.Rect(self.position, self.dimensions)

  def dessiner(self):
    """
        Dessine le bouton sur la fenêtre Pygame.
        """
    # Utiliser la couleur appropriée en fonction de l'état actif
    couleur = self.couleur_active if self.actif else self.couleur_normale

    # Dessiner le bouton avec la méthode pygame.draw.rect
    pygame.draw.rect(self.fenetre, couleur, self.rect)
    pygame.draw.rect(self.fenetre, noir, self.rect, 2)

    # Dessiner un texte sur la touche (utilisez une police de caractères si nécessaire)
    font = pygame.font.Font(None, 36)
    text = font.render(self.touche, True, blanc if self.actif else noir)
    text_rect = text.get_rect(center=self.rect.center)
    self.fenetre.blit(text, text_rect)
  def activer(self):
    """
        Active le bouton.
        """
    self.actif = True

  def desactiver(self):
    """
        Désactive le bouton.
        """
    self.actif = False


class Note:

  def __init__(self, fenetre, touche, positions_y):
    """
        Initialise un objet Note.
        """
    self.fenetre = fenetre
    self.touche = touche
    self.position_x = 1000  # Initialiser la position en (0, y)
    self.position_y = positions_y[touche]

    # Construire le chemin du fichier image en fonction de la touche
    image_path = os.path.join("image", "note", f"{touche}.png")

    # Charger l'image de la note
    # aggrandi un peu la note 
    self.image = pygame.image.load(image_path).convert_alpha()
    self.image = pygame.transform.scale(self.image, (100, 100))

  def t(self):
    return self.touche

  def draw(self):
    if self.position_x < 320 :
      image_path = os.path.join("image", "note", f"{self.touche}-red.png")
      self.image = pygame.image.load(image_path).convert_alpha()
      # Blitter l'image de la note sur la fenêtre à la position spécifiée
      y_note = self.position_y
      self.position_x = self.position_x - 1
      self.fenetre.blit(self.image, (self.position_x, y_note))
      
    else:
      image_path = os.path.join("image", "note", f"{self.touche}.png")
      self.image = pygame.image.load(image_path).convert_alpha()

      # fait en sorte que la touche se suprimer si elle est en dehors de l'ecran avec une animation qui rapeticie la touche
    if self.position_x < 0:
      musique.remove(self)



    """
        Dessine la note sur l'écran.
        """
    # Blitter l'image de la note sur la fenêtre à la position spécifiée
    y_note = self.position_y
    self.position_x = self.position_x - 5
    self.fenetre.blit(self.image, (self.position_x, y_note))


 
dictmusic = {}

def open_csv_music():
  global dictmusic
  f = open("partition1.csv")
  myReader = csv.reader(f)
  for row in myReader:
    dictmusic[row[0]] = row[1]
  print(dictmusic)

dictnote = {}

def open_csv_note():
  global dictnote
  f = open("partition.csv")
  myReader = csv.reader(f)
  for row in myReader:
    dictnote[row[1]] = row[0]
  print(dictnote)
  
dictpos = {}

def open_csv_pos():
  global dictpos
  f = open("partition.csv")
  myReader = csv.reader(f)
  for row in myReader:
    dictpos[row[0]] = row[2]
  print(dictpos)
  print(dictpos["d"])

jeu = True

positions_y = {touche: y for touche, y in zip(touches, liste_positions)}
x = 20
note = 1
n = 1
def music(fenetre):
  global jeu
  global musique
  global x
  global n 
  if jeu == True:
    # faire que si n > 61 alors le jeu s'arrete
    if n > 61:
      jeu = False
      pass
    else:
      if x < 20 :
        x += 1
      else:
        x = 0 
        n += 1
        #  si la note = "oo" alors ne rien afficher faire une pause
        # arreter la 
        if dictmusic[str(n)] == "oo":
          x = 10
          print("pause")
        else:

            
          touche = dictnote[dictmusic[str(n)]]
          print(touche)
          note = Note(fenetre, touche, positions_y)
          musique.append(note)
          print(dictmusic)
    
open_csv_pos()
print(f'position y ) {positions_y}')