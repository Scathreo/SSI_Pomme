from os.path import basename

from abc import ABC, abstractmethod

# Classe Adaptateur.
# Adaptateur entre le RSV (Middleware) et les exports.
# Objectif, traiter les rapports et transmettre les données sous un format 
# standardisé vers le RSV.
class Adaptateur(ABC):

  #############################################################################
  ########################     Variables Statiques     ########################
  #############################################################################
  
  FORMAT_DATE_HEURE = "%Y-%m-%d %H:%M:%S"
  TRAITEMENT_PREFIX = "traite_"
  TRAITEMENT_SUFIX = ""

  SOURCE_ORADAD = "Oradad"
  SOURCE_CSV    = "CSV"
  SOURCE_DB     = "DB"
  SOURCE_CONFIG = "config"
  SOURCE_CASSIS = "CASSIS"
    
    
    
    
  #############################################################################
  ##########################     Private methods     ##########################
  #############################################################################
  
  
  
  # Constructeur
  def __init__(self, adaptateur_CSV):
    print("Adaptateur - Init - Begin")
    
    self.adaptateur_CSV = adaptateur_CSV
    
    print("Adaptateur - Init - End")
    
    
  
  # Ouvre un fichier (rapport).
  # (Si erreur) Retourne -1 ;
  # (Sinon) Retourne le fichier ouvert.
  def __open_file__(self, path, mode):
  
    try:
      print("Opening file " + path + "...")
      open_file = open(path, mode)
      
    except:
      raise Exception("Error while opening file " + path)
    else:
      print("File " + path + " opened.")
      return open_file
      
  
  
  # Ferme un fichier (rapport).
  # (Si erreur) Retourne -1 ;
  # (Sinon) Retourne 0.
  def __close_file__(self, open_file):
  
    try:
      print("Closing file " + open_file.name + "...")
      open_file.close()
      
    except:
      raise Exception("Error while closing file " + open_file.name)
      
    else:
      print("File " + open_file.name +" closed.")
    
    
    
  # Obtient le nom du fichier à partir de son chemin complet.
  def __get_path_basename__(self, path):
    return basename(path)
      
      
      
      
      
      
      
  # Trouve l'index du debut du bloc et celui de la fin du bloc
  # retourne index_debut_bloc, index_fin_bloc
  # Renvoi -1 si erreur
  def __trouve_debut_fin_bloc__(self, 
    texte, 
    delemiteur_bloc_begin, 
    delemiteur_bloc_end, 
    index_debut=0, 
    index_fin=-1
  ):
  
  
    if index_fin < 0: index_fin = len(texte)
    
    index_debut_bloc        = 0
    index_fin_bloc          = 0
    
    compteur_ouverture_bloc = 0
    index                   = index_debut
    
    
    
    while index < index_fin:
      if texte[index] == delemiteur_bloc_begin:
        compteur_ouverture_bloc = 1
        index_debut_bloc = index
        break
      else:
        # Avance l'index tampon
        index = index + 1
      
    
    
    
    # Tant que des blocs sont ouverts
    while compteur_ouverture_bloc > 0 and index < index_fin:
      
      # Avance l'index tampon
      index = index + 1
      
      if texte[index] == delemiteur_bloc_begin:
        compteur_ouverture_bloc = compteur_ouverture_bloc + 1
      elif texte[index] == delemiteur_bloc_end:
        compteur_ouverture_bloc = compteur_ouverture_bloc - 1
        
    if index >= index_fin: index_fin_bloc = -1
    
    index_fin_bloc = index + 1
    
    return index_debut_bloc, index_fin_bloc
    
    
    
    
    
  #############################################################################
  ##########################     Public methods      ##########################
  #############################################################################
  
  # Méthode abstraite.
  # Traite les rapports pour transmettre les données sous un fomat standardisé 
  # vers le RSV.
  @abstractmethod
  def traitement_fichier(self):
    pass
    
  
