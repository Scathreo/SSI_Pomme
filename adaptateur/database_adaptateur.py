from .adaptateur      import Adaptateur     as Adaptateur


import mysql.connector as db_connector



# Classe OradadAdaptateur.
# Adaptateur entre le RSV (Middleware) et les exports Oradad.
# Objectif, traiter les rapports Oradad et transmettre les données sous un 
# format standardisé vers le RSV.
class DatabaseAdaptateur(Adaptateur):

  #############################################################################
  ########################     Variables Statiques     ########################
  #############################################################################

  SOURCE = Adaptateur.SOURCE_DB
  
  
  KEY_SERVER   = "database_server"
  KEY_DATABASE = "database_database"
  KEY_USERNAME = "database_username"
  KEY_PASSWORD = "database_password"
  
  KEY_TABLE_K6      = "database_table_k6"
  KEY_TABLE_PRIMARY = "database_table_vulnerabilites_obsolescence"
                      
                      

                      
                    
    
    
    
    
  #############################################################################
  ##########################     Private methods     ##########################
  #############################################################################
  
  
  
  # Constructeur
  def __init__(self, 
    database_info,
    database_table
  ):
    super().__init__("")
    print("DatabaseAdaptateur - Init - Begin")
    
    
    self.connected  = False
    
    
    self.database_info = database_info
    
    
    
    self.database_tables = database_table

    
    
    self.connexion  = self.__connect_to_db__()
    self.cursor     = self.connexion.cursor()
    
    
    
    self.headers_primary = self.__get_headers__(
      self.database_tables[DatabaseAdaptateur.KEY_TABLE_PRIMARY],
      [0]
    )
    
    
    
    print("DatabaseAdaptateur - Init - End")
    
    
    
    
    
  def __get_headers__(self, table, ignore_elements = []):
  
    tuple_db = (table, self.database_info[DatabaseAdaptateur.KEY_DATABASE])
    
    index = 0
    resultats = []
  
    sql = (
      "SELECT column_name"
      + " FROM information_schema.columns"
      + " WHERE table_name = %s AND table_schema = %s;"
    )
        
    self.cursor.execute(sql, tuple_db)
    resultat_fetchall = self.cursor.fetchall()
    
    while index < len(resultat_fetchall):
      if not index in ignore_elements:
        resultats += resultat_fetchall[index]
      index = index + 1
    
    return resultats
    
    
  # Connexion à la base de données.
  # (Si erreur) Retourne 0 ;
  # (Sinon) Retourne la connexion à la base de données.
  def __connect_to_db__(self):
    
    # Essai de se connecter à la BDD.
    try:
      print(
        "Connecting to DB " 
        + self.database_info[DatabaseAdaptateur.KEY_DATABASE] 
        + "..."
      )
      connexion = db_connector.connect(
          user      = self.database_info[DatabaseAdaptateur.KEY_USERNAME], 
          password  = self.database_info[DatabaseAdaptateur.KEY_PASSWORD],
          host      = self.database_info[DatabaseAdaptateur.KEY_SERVER],
          database  = self.database_info[DatabaseAdaptateur.KEY_DATABASE]
      )
      
    # Si erreur, lors de la connexion, renvoi 0.
    except:
        raise Exception(
          "Error while connecting from DB "
          + self.database_info[DatabaseAdaptateur.KEY_DATABASE] 
          + "."
        )
      
    # Si pas erreur, renvoi la connexion.
    else:
      print(
        "Connected to DB "
        + self.database_info[DatabaseAdaptateur.KEY_DATABASE] 
        + "."
      )
      self.connected  = True
      return connexion
    
    
    
  # Déconnexion à la base de données.
  # (Si erreur) Retourne -1 ;
  # (Sinon) Retourne 0.
  def __disconnect_to_db__(self):
    
    if self.connected:
      # Essai de se déconnecter à la BDD.
      try:
        print(
          "Disconnecting from DB "
          + self.database_info[DatabaseAdaptateur.KEY_DATABASE] 
          + "..."
        )
        self.cursor.close()
        self.connexion.close()
        
      except:
        raise Exception(
          "Error while disconnecting from DB "
          + self.database_info[DatabaseAdaptateur.KEY_DATABASE] 
          + "."
        )
        
      else:
        print(
          "Disconnected from DB "
          + self.database_info[DatabaseAdaptateur.KEY_DATABASE] 
          + "."
        )
        self.connected  = False
        
      
      
  # Destructeur
  def __del__(self):
    self.__disconnect_to_db__()
    del self
  
  
  
  
  def __insert_into_db__(self, table, resultats):
    
    ignore_headers = []
    ignore_headers_on_duplicate = []
    
    if table == DatabaseAdaptateur.KEY_TABLE_PRIMARY : 
      ignore_headers = [0]
      ignore_headers_on_duplicate = [4, 5]
    
    
    headers = self.__get_headers__(
      self.database_tables[table], 
      ignore_headers
    )
    headers_on_duplicate = self.__get_headers__(
      self.database_tables[table], 
      ignore_headers_on_duplicate
    )
    
    
    
    sql = (
      "INSERT INTO "
      + self.database_info[DatabaseAdaptateur.KEY_DATABASE]
      + "."
      + self.database_tables[table]
      + " ("
    )
    
    for header in headers:
      sql = sql + header + ", "
    
    sql = sql[0 : len(sql) - 2] + ") VALUES ("
    
    for header in headers:
      sql = sql + "%s, "
    
    sql = (
      sql[0 : len(sql) - 2] 
      + ")"
      + " ON DUPLICATE KEY UPDATE "
    )
    
    for header in headers_on_duplicate:
      sql = sql + header + "=" + header + ", "
      
    sql = sql[ 0 : len(sql) - 2 ] + ";"
    
    
        
    self.cursor.execute(sql, resultats)
    print("Record inserted")
    # the connection is not auto committed by default, so we must commit to save our changes
    self.connexion.commit()
  
  
    
  
    
    
    
    
  #############################################################################
  ##########################     Public methods      ##########################
  #############################################################################
      
      
      
  
  
    
  def traitement_fichier(self, table, resultats): 
    self.__insert_into_db__(table, resultats)
    
    
    
    
    
