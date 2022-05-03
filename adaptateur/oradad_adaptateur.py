from .adaptateur      import Adaptateur     as Adaptateur

from datetime import datetime



# Classe OradadAdaptateur.
# Adaptateur entre le RSV (Middleware) et les exports Oradad.
# Objectif, traiter les rapports Oradad et transmettre les données sous un 
# format standardisé vers le RSV.
class OradadAdaptateur(Adaptateur):

  #############################################################################
  ########################     Variables Statiques     ########################
  #############################################################################

  SOURCE = Adaptateur.SOURCE_ORADAD
  
  
  BLOCK_RIM_BEGIN = "{"
  BLOCK_RIM_END   = "}"
  DATA_RIM_BEGIN  = "["
  DATA_RIM_END    = "]"
  FIELD_BEGIN     = "\""
  FIELD_END       = "\""
  
  
  
  MODULE_REFS = [
    [
      FIELD_BEGIN 
      + "dont_expire_priv"
      + FIELD_BEGIN, 
      "Comptes privilégiés dont le mot de passe n'expire jamais"
    ],
    [
      FIELD_BEGIN 
      + "password_change_priv"
      + FIELD_BEGIN, 
      "Comptes privilégiés dont le mot de passe est inchangé depuis plus de 3 ans"
    ]
  ]
  
  
  
  CSV             = ( FIELD_BEGIN
                      + "csv"
                      + FIELD_BEGIN )
  CSV_HEADER      = ( FIELD_BEGIN 
                      + "header"                        
                      + FIELD_BEGIN )
                      
  ATTRS           = ( FIELD_BEGIN 
                      + "attrs"                         
                      + FIELD_BEGIN )
  ATTRS_DATA      = ( FIELD_BEGIN 
                      + "data"                          
                      + FIELD_BEGIN )
                      
  DN              = ( FIELD_BEGIN 
                      + "dn"                         
                      + FIELD_BEGIN )
                      
  INSTANCE        = ( FIELD_BEGIN 
                      + "instance"                         
                      + FIELD_BEGIN )
                      
  FOREST          = ( FIELD_BEGIN 
                      + "forest"                         
                      + FIELD_BEGIN )
  
  
  FORMAT_DATE_HEURE = "%Y%m%d-%H%M%S"
                      
                      
                    
    
    
    
    
  #############################################################################
  ##########################     Private methods     ##########################
  #############################################################################
  
  
  
  # Constructeur
  def __init__(self, adaptateur_CSV):
    super().__init__(adaptateur_CSV)
    print("OradadAdaptateur - Init - Begin")
    
    print("OradadAdaptateur - Init - End")
  
  
    
  
    
    
    
    
  #############################################################################
  ##########################     Public methods      ##########################
  #############################################################################
    
  def traitement_fichier(self, path_data, path_csv):
  
    # Ouvertures fichiers
    origine_data_file = self.__open_file__(path_data, "r")
    traited_data_file = self.__open_file__(path_csv, "w")
    
    
    texte = origine_data_file.read()  # Lecture fichier données
    
    
    
          
        
      
    
    
            
    index = texte.find(OradadAdaptateur.INSTANCE)
            
    index_header_file_begin =  texte.find(
      OradadAdaptateur.FIELD_BEGIN,
      index + len(OradadAdaptateur.INSTANCE)
    )
            
    index_header_file_end =  texte.find(
      OradadAdaptateur.FIELD_END,
      index_header_file_begin + len(OradadAdaptateur.FIELD_BEGIN)
    )
    
    
    
    horodatage_trouve = texte[
                          index_header_file_begin + 1
                          :
                          index_header_file_end
                        ]     
    horodatage_trouve = datetime.strptime(
                          horodatage_trouve,
                          OradadAdaptateur.FORMAT_DATE_HEURE
                        ).strftime(Adaptateur.FORMAT_DATE_HEURE)
    
    
    
    
    
    
    index = texte.find(OradadAdaptateur.FOREST)
            
    index_header_file_begin =  texte.find(
      OradadAdaptateur.FIELD_BEGIN,
      index + len(OradadAdaptateur.FOREST)
    )
            
    index_header_file_end =  texte.find(
      OradadAdaptateur.FIELD_END,
      index_header_file_begin + len(OradadAdaptateur.FIELD_BEGIN)
    )
    
    
    
    technologie = texte[
                          index_header_file_begin + 1
                          :
                          index_header_file_end
                        ]     
                        
                        
    
    
    
    
    # Parcours les différents types de vulnérabilités afin de les chercher.
    for module_ref in OradadAdaptateur.MODULE_REFS:
    
      compteur_ouverture_bloc = 1 # Compte le nb d'ouverture de bloc
    
      index = 0             # Index dans String (tampon)
      index_begin_bloc = 0  # Index dans String (début du bloc "{")
      index_end_bloc = 0    # Index dans String (fin du bloc "{")
      index_module_ref = texte.find(module_ref[0]) # Index dans String 
                                                # (place du type de la vuln)
        
      index_csv = 0         # Index dans String (début du bloc csv)
      index_csv_header = 0  # Index dans String (début du bloc header des csv)
      index_attrs = 0       # Index dans String (début du bloc attrs)
      
      index_attrs_data = 0  # Index dans String (début du bloc data des attrs)
      index_attrs_data_begin = 0  # Index dans String (début du bloc des data)
      index_attrs_data_end = 0  # Index dans String (fin du bloc des data)
      index_attrs_data_fields_begin = 0     # Index dans String 
                                            # (début du bloc des data)
      index_attrs_data_fields_end = 0       # Index dans String 
                                            # (fin du bloc des data)
      index_attrs_data_fields_dn_begin = 0  # Index dans String 
                                            # (début du bloc dn des data)
      index_attrs_data_fields_dn_end = 0    # Index dans String 
                                            # (fin du bloc dn des data)
    
    
    
    
      # Tant que on trouve une occurence
      # (la lecture du fichier n'est pas terminé)
      while index_module_ref > -1:
        
        # Trouve la prochaine occurence du type de vuln
        index_module_ref = texte.find(module_ref[0], index_module_ref - 1)
        # Si arriver à la dernière occurence, sort de la boucle
        if index_module_ref < index_begin_bloc: break 
        # Initialise l'index tampon
        index = index_module_ref - 1
        # Tente de trouver le debut du bloc
        index_begin_bloc = texte.find(OradadAdaptateur.BLOCK_RIM_BEGIN, index)
        
        # Tant que le debut du bloc n'est pas le bon
        # (après le debut du type de vuln)
        while index_begin_bloc > index_module_ref:
          
          # Recule l'index tampon
          index = index - 1
          # Tente de trouver le début du bloc
          index_begin_bloc = texte.find(OradadAdaptateur.BLOCK_RIM_BEGIN, index)
        
        
        
        
        index_begin_bloc, index_end_bloc =  self.__trouve_debut_fin_bloc__(
                                              texte, 
                                              OradadAdaptateur.BLOCK_RIM_BEGIN,
                                              OradadAdaptateur.BLOCK_RIM_END,
                                              index
                                            )
          
        
        
        ### Ici ###
        # début du bloc trouvé
        # fin du bloc trouvé
        
        
        index_csv = texte.find(OradadAdaptateur.CSV, index_begin_bloc)
        index_csv_header = texte.find(OradadAdaptateur.CSV_HEADER, index_csv)
        index_attrs = texte.find(OradadAdaptateur.ATTRS, index_csv)
        index_attrs_data = texte.find(OradadAdaptateur.ATTRS_DATA, index_attrs)
        
        if index_csv > index_end_bloc:        index_csv = -1
        if index_csv_header > index_end_bloc: index_csv_header = -1
        if index_attrs > index_end_bloc:      index_attrs = -1
        if index_attrs_data > index_end_bloc: index_attrs_data = -1
        
        
        if index_attrs_data > 0:
          index_attrs_data_begin, index_attrs_data_end = (
            self.__trouve_debut_fin_bloc__(
              texte, 
              OradadAdaptateur.DATA_RIM_BEGIN,
              OradadAdaptateur.DATA_RIM_END,
              index_attrs_data
            )
          )
          
          
          index_attrs_data_fields_begin, index_attrs_data_fields_end = (
            self.__trouve_debut_fin_bloc__(
              texte, 
              OradadAdaptateur.BLOCK_RIM_BEGIN,
              OradadAdaptateur.BLOCK_RIM_END,
              index_attrs_data_begin,
              index_attrs_data_end
            )
          )
          
          while (index_attrs_data_fields_end < index_attrs_data_end
            and index_attrs_data_fields_begin > index_attrs_data_begin
            and index_attrs_data_fields_end > 0
            and index_attrs_data_fields_begin > 0):
            
            index = texte.find(
              OradadAdaptateur.DN,
              index_attrs_data_fields_begin,
              index_attrs_data_fields_end
            )
                    
            index_attrs_data_fields_dn_begin =  texte.find(
              OradadAdaptateur.FIELD_BEGIN,
              index + len(OradadAdaptateur.DN), 
              index_attrs_data_fields_end
            )
                    
            index_attrs_data_fields_dn_end =  texte.find(
              OradadAdaptateur.FIELD_END,
              index_attrs_data_fields_dn_begin 
              + len(OradadAdaptateur.FIELD_BEGIN), 
              index_attrs_data_fields_end
            )
            
            
            
            commentaire = texte[
                            index_attrs_data_fields_dn_begin + 1
                            :
                            index_attrs_data_fields_dn_end
                          ]
        
        
            label             = module_ref[1]
            horodatage_RSV    = datetime.now().strftime(
                                  Adaptateur.FORMAT_DATE_HEURE
                                )
            
            
            self.adaptateur_CSV.__ecrit_donnees__(
              traited_data_file, 
              OradadAdaptateur.SOURCE, 
              technologie, 
              label, 
              horodatage_trouve, 
              horodatage_RSV, 
              commentaire
            )
            
            
            
            
            index_attrs_data_fields_begin, index_attrs_data_fields_end = (
              self.__trouve_debut_fin_bloc__(
                texte, 
                OradadAdaptateur.BLOCK_RIM_BEGIN,
                OradadAdaptateur.BLOCK_RIM_END,
                index_attrs_data_fields_end,
                index_attrs_data_end
              )
            )
        
        index_module_ref = index_module_ref + len(module_ref[0])
    
    
    self.__close_file__(origine_data_file)
    self.__close_file__(traited_data_file)
