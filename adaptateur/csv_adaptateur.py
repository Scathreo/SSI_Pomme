from .adaptateur      import Adaptateur     as Adaptateur



# Classe OradadAdaptateur.
# Adaptateur entre le RSV (Middleware) et les exports Oradad.
# Objectif, traiter les rapports Oradad et transmettre les données sous un 
# format standardisé vers le RSV.
class CSVAdaptateur(Adaptateur):

  #############################################################################
  ########################     Variables Statiques     ########################
  #############################################################################

  SOURCE = Adaptateur.SOURCE_CSV
  
  
  
  DELIMITEUR_CSV = ";"
  
  EXTENTION_FICHIER = ".csv"
  
                      
                      
                    
    
    
    
    
  #############################################################################
  ##########################     Private methods     ##########################
  #############################################################################
  
  
  
  # Constructeur
  def __init__(self):
    super().__init__("")
    print("CSVAdaptateur - Init - Begin")
    
    print("CSVAdaptateur - Init - End")
  
  
    
  
    
    
    
    
  #############################################################################
  ##########################     Public methods      ##########################
  #############################################################################
  
  
    
    
  # Ecrit dans le fichier, les champs fournit en paramètre.
  # Le fichier doit être ouvert en ecriture.
  def __ecrit_donnees__(self, 
    fichier, 
    source, 
    technologie, 
    label, 
    horodatage_trouve, 
    horodatage_RSV,
    commentaire = ""
  ):
  
    try:
      print("Writing in file " + fichier.name + "...")
      
      texte = (
        source                        + CSVAdaptateur.DELIMITEUR_CSV
        + technologie                 + CSVAdaptateur.DELIMITEUR_CSV
        + label                       + CSVAdaptateur.DELIMITEUR_CSV
        + horodatage_trouve           + CSVAdaptateur.DELIMITEUR_CSV
        + horodatage_RSV              + CSVAdaptateur.DELIMITEUR_CSV
        + commentaire
        + "\n"
      )
                   
      fichier.write(texte)
      
    except:
      raise Exception("Error while writing in file " + fichier.name + ".")
    
    else:
      print("Line wrote in file " + fichier.name + ".")
    

    
  
    
    
  # Ecrit dans le fichier, les champs fournit en paramètre.
  # Le fichier doit être ouvert en ecriture.
  def __ecrit_donnees_from_array__(self, 
    fichier, 
    array
  ):
  
    texte = ""
  
    try:
      print("Writing in file " + fichier.name + "...")
      
      for element in array:
        texte = texte + str(element) + CSVAdaptateur.DELIMITEUR_CSV
        
      texte = texte[
                      0
                      :
                      len(texte) - len(CSVAdaptateur.DELIMITEUR_CSV)
                    ]
                    
      texte = texte + "\n"
                   
      fichier.write(texte)
      
    except:
      raise Exception("Error while writing in file " + fichier.name + ".")
    
    else:
      print("Line wrote in file " + fichier.name + ".")
    

    
    
    
    
    
    
  def traitement_fichier(self, path_data):
  
    fichier_open = self.__open_file__(path_data, "r")
    
    
    
    resultats = []    
    
    for ligne in fichier_open:
      resultats += [ligne.split(CSVAdaptateur.DELIMITEUR_CSV)]
        
    
    self.__close_file__(fichier_open)
    
    return resultats
