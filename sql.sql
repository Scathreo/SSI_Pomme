DROP DATABASE test_bm;
CREATE DATABASE test_bm CHARACTER SET utf8 COLLATE utf8_general_ci;

USE test_bm;





CREATE TABLE vulnerabilites_obsolescence (

  id                    INT NOT NULL AUTO_INCREMENT,
  source                VARCHAR(50),
  technologie           VARCHAR(100),
  label                 VARCHAR(255),
  horodatage_trouve     DATETIME,
  horodatage_RSV        DATETIME,
  commentaire           VARCHAR(255),
  
  CONSTRAINT PK_id PRIMARY KEY (id),
  CONSTRAINT UC_vulnerabilites_obsolescence UNIQUE (
    technologie,
    label, 
    commentaire
  )
  
);




CREATE TABLE cassis_technologies (

  nom                       VARCHAR(50),
  type                      VARCHAR(100),
  norme_entreprise          VARCHAR(50),
  fin_support               DATE,
  alerte_support            VARCHAR(100),
  portefeuille              VARCHAR(50),
  
  CONSTRAINT PK_id PRIMARY KEY (nom)
  
);




CREATE TABLE cassis_applications (

  nom                       VARCHAR(50),
  nom_usage                 VARCHAR(50),
  identifiant_unique        VARCHAR(20),
  etat_courant              VARCHAR(50),
  conformite_technologique  VARCHAR(50),
  direction_mon             VARCHAR(10),
  description               VARCHAR(255),
  
  CONSTRAINT PK_id PRIMARY KEY (identifiant_unique)
  
);

