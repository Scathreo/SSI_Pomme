import sys
import mysql.connector

from pyope.ope import OPE

#
# On ne nettoie pas notre curseur après utilisation
# Donc les résultats sont surement accessible dans un contexte 
# que l'on ne voudrait pas
#

def get_max_id(cursor):
    cursor.execute('SELECT MAX(id) FROM chiffre')
    return cursor.fetchone()[0]


def sum_two_data(cursor, id1, id2):
    somme = 0
    cursor.execute('SELECT entier FROM chiffre WHERE id=' + str(id1))
    somme = somme + create_cipher().decrypt(cursor.fetchone()[0]) 
    # Optimisation possible plutot que de d'ouvrir a chaque fois le fichier
    # avec la clé
    cursor.execute('SELECT entier FROM chiffre WHERE id=' + str(id2))
    somme = somme + create_cipher().decrypt(cursor.fetchone()[0]) 
    # Optimisation possible plutot que de d'ouvrir a chaque fois le fichier
    # avec la clé
    return somme


def compare_two_data(cursor, id1, id2):
    tmp = 0
    cursor.execute('SELECT entier FROM chiffre WHERE id=' + str(id1))
    tmp = cursor.fetchone()[0]
    # Optimisation possible plutot que de d'ouvrir a chaque fois le fichier
    # avec la clé
    cursor.execute('SELECT entier FROM chiffre WHERE id=' + str(id2))
    # Optimisation possible plutot que de d'ouvrir a chaque fois le fichier
    # avec la clé
    return tmp == cursor.fetchone()[0]
    

def put_data_into_sql(connexion, cursor, data):
    data = create_cipher().encrypt(data)
    # Optimisation possible plutot que de d'ouvrir a chaque fois le fichier
    # avec la clé
    cursor.execute('INSERT INTO chiffre (entier) VALUES (' + str(data) + ')')
    connexion.commit()
    print("Data inserted")


def get_data_from_sql(cursor, identifier):
    cursor.execute('SELECT entier FROM chiffre WHERE id=' + str(identifier))
    return create_cipher().decrypt(cursor.fetchone()[0]) 
    # Optimisation possible plutot que de d'ouvrir a chaque fois le fichier
    # avec la clé


def __connect_to_sql():
    server   = 'localhost' 
    database = 'tp_secu_chiff' 
    username = 'root' 
    password = '' 
    connexion = mysql.connector.connect(
        user='user', 
        password='',
        host='127.0.0.1',
        database='tp_secu_chiff'
    )
    print("Connected to DB")
    return connexion


def init_sql():
    connexion = __connect_to_sql()
    return connexion, connexion.cursor()
    
    
def exit_sql(connexion, cursor):
    cursor.close()
    connexion.close()
    print("Exited DB")
    
    
def create_cipher():
    f = open("/tmp/random_key_tp_bdd", "rb")
    cipher = OPE(f.read())
    f.close()
    return cipher
    
    
def __create_key(): 
    # On update pas la BDD après, donc on ne pourra pas déchiffrer 
    # l'information ensuite.
    # Génèrera des erreurs
    f = open("/tmp/random_key_tp_bdd", "w")
    f.write(str(OPE.generate_key()))
    f.close()
    print("Key created")
    
  
def __wipe_db():
    connexion = __connect_to_sql()
    cursor = connexion.cursor()
    f = open("/home/test/Q31-SQL", "r")
    cursor.execute(f.read())
    print("DB wiped")
    f.close()
    exit_sql(connexion, cursor)
    
      
def __init_admin():
    __create_key()
    #__connect_to_sql()
    






if __name__ == '__main__':
    for arg in sys.argv:
        if arg == "admin":
            __init_admin()
            exit()
        if arg == "wipe":
            __wipe_db()
            exit()
            


    # TESTS
    connexion, cursor = init_sql()


    put_data_into_sql(connexion, cursor, 10)
    print("Data : " + str(get_data_from_sql(cursor, 1)))


    exit_sql(connexion, cursor)
