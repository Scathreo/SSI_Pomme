from .adaptateur      import Adaptateur     as Adaptateur

from datetime import datetime



# Classe OradadAdaptateur.
# Adaptateur entre le RSV (Middleware) et les exports Oradad.
# Objectif, traiter les rapports Oradad et transmettre les données sous un 
# format standardisé vers le RSV.
class CassisAdaptateur(Adaptateur):

  #############################################################################
  ########################     Variables Statiques     ########################
  #############################################################################

  SOURCE = Adaptateur.SOURCE_CASSIS
  
  APPLICATIONS_NAME_FILE = "Applications"
  TECHNOLOGIES_NAME_FILE = "Technologies"
  
  
  APPLICATIONS_HEADERS = [
    "Nom",
    "Nom d'usage",
    "Identifiant unique",
    "Etat courant",
    "Conformité technologique",
    "Direction MON"
  ]
  
  
  TECHNOLOGIES_HEADERS = [
    "Nom",
    "Type", 
    "Norme d'entreprise", 
    "Fin de support", 
    "Alerte de Support", 
    "Portefeuille"
  ]
  
  
  
  FORMAT_DATE_HEURE = "%d/%m/%Y"
                      
                      
                    
    
    
    
    
  #############################################################################
  ##########################     Private methods     ##########################
  #############################################################################
  
  
  
  # Constructeur
  def __init__(self, adaptateur_CSV):
    super().__init__(adaptateur_CSV)
    print("CassisAdaptateur - Init - Begin")
    
    print("CassisAdaptateur - Init - End")
  
  
  
  
  
  
  def __import_data__(self, path_data, path_csv, mode):
    pass
    
    
    
    
  #############################################################################
  ##########################     Public methods      ##########################
  #############################################################################
    
  def traitement_fichier(self, path_data, path_csv):
  
    # Ouvertures fichiers
    origine_data_file = self.__open_file__(path_data, "r")
    traited_data_file = self.__open_file__(path_csv, "w")
    
    
    texte = origine_data_file.read()  # Lecture fichier données
    
    
    texte = texte.replace(",", ";")
    texte = texte.replace(";;;;;;;", "")
    
    
    
    traited_data_file.write(texte)
    
    
    self.__close_file__(origine_data_file)
    self.__close_file__(traited_data_file)
    
    
