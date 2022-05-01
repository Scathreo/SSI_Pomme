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




CREATE TABLE CASSIS (

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

