from .adaptateur      import Adaptateur     as Adaptateur



# Classe OradadAdaptateur.
# Adaptateur entre le RSV (Middleware) et les exports Oradad.
# Objectif, traiter les rapports Oradad et transmettre les données sous un 
# format standardisé vers le RSV.
class ConfigAdaptateur(Adaptateur):

  #############################################################################
  ########################     Variables Statiques     ########################
  #############################################################################

  SOURCE = Adaptateur.SOURCE_CONFIG
                      
                      
                      
  DELIMITEUR_CHAMPS = "\""
                      
                    
    
    
    
    
  #############################################################################
  ##########################     Private methods     ##########################
  #############################################################################
  
  
  
  # Constructeur
  def __init__(self, config_file):
    super().__init__("")
    print("ConfigAdaptateur - Init - Begin")
    
    self.config_file = config_file
    
    print("ConfigAdaptateur - Init - End")
    
    
    
    
  
    
    
    
    
  #############################################################################
  ##########################     Public methods      ##########################
  #############################################################################
    
  
  def traitement_fichier(self, champs):
    
    index = 0
  
    file_open = self.__open_file__(self.config_file, "r")
    
    
    dictionnaire = {}
    
    for element in champs:
      dictionnaire[element] = ""
    
    for line in file_open:
    
      for key in dictionnaire:
      
        index = line.find(key, 0, len(key))
        
        if index >= 0:
        
          dictionnaire[key] = line[
            index + len(key) 
            : 
            len(line)
          ].split(ConfigAdaptateur.DELIMITEUR_CHAMPS)[1]
          
          break;
          
    
    
    self.__close_file__(file_open)
    
    
    return dictionnaire
    
    
