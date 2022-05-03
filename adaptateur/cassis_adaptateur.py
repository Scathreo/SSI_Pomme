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
    "Direction MON",
    "Description"
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
    pass
    
    
