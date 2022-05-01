from sys import exit
from os import listdir
from os.path import isfile, join, abspath, basename


from adaptateur.oradad_adaptateur   import OradadAdaptateur   as OradadAdaptateur
from adaptateur.csv_adaptateur      import CSVAdaptateur      as CSVAdaptateur
from adaptateur.database_adaptateur import DatabaseAdaptateur as DatabaseAdaptateur
from adaptateur.config_adaptateur   import ConfigAdaptateur   as ConfigAdaptateur
from adaptateur.adaptateur          import Adaptateur         as Adaptateur

# Classe RSV.
# Middleware, qui se connecte à la base de données et gère les commandes des 
# adaptateurs.
class Pomme:

  KEY_PATH_DATA = "data_repository"
  KEY_PATH_DATA_PROCESSED = "data_processed_repository"

  #############################################################################
  ########################     Variables Statiques     ########################
  #############################################################################
    
    
    
    
  #############################################################################
  ##########################     Private methods     ##########################
  #############################################################################
    


  # Constructeur
  def __init__(self, config_file = ""):
    print("Pomme - Init - Begin")
    
    
    self.adaptateur_config = ConfigAdaptateur(config_file)
    
    
    self.adaptateur_DB = DatabaseAdaptateur(
      self.adaptateur_config.traitement_fichier(
        [
          DatabaseAdaptateur.KEY_SERVER,
          DatabaseAdaptateur.KEY_DATABASE,
          DatabaseAdaptateur.KEY_USERNAME,
          DatabaseAdaptateur.KEY_PASSWORD
        ]
      ),
      self.adaptateur_config.traitement_fichier(
        [
          DatabaseAdaptateur.KEY_TABLE_K6,
          DatabaseAdaptateur.KEY_TABLE_PRIMARY
        ]
      )
    )
    self.adaptateur_CSV = CSVAdaptateur()
    
    
    
    self.dossier_data = self.adaptateur_config.traitement_fichier(
      [
        Pomme.KEY_PATH_DATA,
        Pomme.KEY_PATH_DATA_PROCESSED
      ]
    )
    
    
    
    
    self.adaptateur = []
    self.adaptateur += [OradadAdaptateur(self.adaptateur_CSV)]
    
    
    
    
    print("Pomme - Init - End")
    
    
    
    
    
  #############################################################################
  ##########################     Public methods      ##########################
  #############################################################################
  
  
  def start(self): 
    
    fichiers_data = [
      join(abspath(self.dossier_data[Pomme.KEY_PATH_DATA]), fichier) 
        for fichier in listdir(self.dossier_data[Pomme.KEY_PATH_DATA]) 
          if isfile(join(self.dossier_data[Pomme.KEY_PATH_DATA], fichier))
    ]
    
    for fichier in fichiers_data:
      if Adaptateur.SOURCE_ORADAD in fichier:
        self.adaptateur[0].traitement_fichier(
          fichier,
          abspath(self.dossier_data[Pomme.KEY_PATH_DATA_PROCESSED])
          + "/"
          + Adaptateur.TRAITEMENT_PREFIX 
          + basename(fichier)
          + Adaptateur.TRAITEMENT_SUFIX
          + CSVAdaptateur.EXTENTION_FICHIER
        )
  
  
  
  
  
  
  
  
  
    fichiers_csv = [
      join(abspath(self.dossier_data[Pomme.KEY_PATH_DATA_PROCESSED]), fichier) 
        for fichier in listdir(self.dossier_data[Pomme.KEY_PATH_DATA_PROCESSED]) 
          if isfile(join(self.dossier_data[Pomme.KEY_PATH_DATA_PROCESSED], fichier))
    ]
    
    for fichier in fichiers_csv:
      resultats = self.adaptateur_CSV.traitement_fichier(fichier)
      
      for resultat in resultats:
        self.adaptateur_DB.traitement_fichier(
          DatabaseAdaptateur.KEY_TABLE_PRIMARY, 
          resultat
        )
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
