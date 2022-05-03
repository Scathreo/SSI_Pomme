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
  
  
  BORNE_CHAMPS_DEBUT = "<td> "
  BORNE_CHAMPS_FIN   = "&nbsp;</td>"
  
  
  
  FORMAT_DATE_HEURE = "%d/%m/%Y"
                      
                      
                    
    
    
    
    
  #############################################################################
  ##########################     Private methods     ##########################
  #############################################################################
  
  
  
  # Constructeur
  def __init__(self, adaptateur_CSV):
    super().__init__(adaptateur_CSV)
    print("CassisAdaptateur - Init - Begin")
    
    print("CassisAdaptateur - Init - End")
  
  
  
  
  
  
  def __import_technologies__(self, path_data, path_csv):
  
    # Ouvertures fichiers
    origine_data_file = self.__open_file__(path_data, "r")
    traited_data_file = self.__open_file__(path_csv, "w")
    
    
    texte = origine_data_file.read()  # Lecture fichier données
    
    
    compteur_champs  = 0
    
    index_debut_bloc = 0
    index_fin_bloc   = 0 - len(CassisAdaptateur.BORNE_CHAMPS_FIN)
    
    resultats = CassisAdaptateur.TECHNOLOGIES_HEADERS
    
    
    while not index_debut_bloc == -1 and not index_fin_bloc == -1:
    
    
      index_debut_bloc, index_fin_bloc =  self.__trouve_debut_fin_bloc_find__(
        texte, 
        CassisAdaptateur.BORNE_CHAMPS_DEBUT,
        CassisAdaptateur.BORNE_CHAMPS_FIN,
        index_fin_bloc + len(CassisAdaptateur.BORNE_CHAMPS_FIN)
      )
      
      resultats[compteur_champs] = texte[
        index_debut_bloc + len(CassisAdaptateur.BORNE_CHAMPS_DEBUT)
        : 
        index_fin_bloc
      ].replace("\n","\\n")

      compteur_champs = compteur_champs + 1
      
      
      if compteur_champs == len(CassisAdaptateur.TECHNOLOGIES_HEADERS) - 1:
        self.adaptateur_CSV.__ecrit_donnees_from_array__(
          traited_data_file,
          resultats
        )
        compteur_champs = 0
        
    if compteur_champs > 0:
      self.adaptateur_CSV.__ecrit_donnees_from_array__(
        traited_data_file,
        resultats
      )
    

    
    self.__close_file__(origine_data_file)
    self.__close_file__(traited_data_file)
    
    
    
    
    
  def __import_applications__(self, path_data, path_csv):
  
    # Ouvertures fichiers
    origine_data_file = self.__open_file__(path_data, "r")
    traited_data_file = self.__open_file__(path_csv, "w")
    
    
    texte = origine_data_file.read()  # Lecture fichier données
    
    
    compteur_champs  = 0
    
    index_debut_bloc = 0
    index_fin_bloc   = 0 - len(CassisAdaptateur.BORNE_CHAMPS_FIN)
    
    resultats = CassisAdaptateur.APPLICATIONS_HEADERS
    
    
    while not index_debut_bloc == -1 and not index_fin_bloc == -1:
    
    
      index_debut_bloc, index_fin_bloc =  self.__trouve_debut_fin_bloc_find__(
        texte, 
        CassisAdaptateur.BORNE_CHAMPS_DEBUT,
        CassisAdaptateur.BORNE_CHAMPS_FIN,
        index_fin_bloc + len(CassisAdaptateur.BORNE_CHAMPS_FIN)
      )
      
      resultats[compteur_champs] = texte[
        index_debut_bloc + len(CassisAdaptateur.BORNE_CHAMPS_DEBUT)
        : 
        index_fin_bloc
      ].replace("\n","\\n")

      compteur_champs = compteur_champs + 1
      
      
      if compteur_champs == len(CassisAdaptateur.TECHNOLOGIES_HEADERS) - 1:
        self.adaptateur_CSV.__ecrit_donnees_from_array__(
          traited_data_file,
          resultats
        )
        compteur_champs = 0
        
    if compteur_champs > 0:
      self.adaptateur_CSV.__ecrit_donnees_from_array__(
        traited_data_file,
        resultats
      )
    

    
    self.__close_file__(origine_data_file)
    self.__close_file__(traited_data_file)
    
    
    
    
  #############################################################################
  ##########################     Public methods      ##########################
  #############################################################################
    
  def traitement_fichier(self, path_data, path_csv):
  
    if CassisAdaptateur.TECHNOLOGIES_NAME_FILE in path_data:
      self.__import_technologies__(path_data, path_csv)
      
    if CassisAdaptateur.APPLICATIONS_NAME_FILE in path_data:
      self.__import_applications__(path_data, path_csv)
    
    
