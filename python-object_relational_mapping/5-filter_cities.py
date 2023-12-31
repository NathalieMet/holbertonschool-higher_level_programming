#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from sys import argv


def list_states():
    """lists all states from the database hbtn_0e_0_usa"""

    username, password, database, search = argv[1], argv[2], argv[3], argv[4]
    # Établir une connexion à la base de données
    connexion = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database)
    # Créer un objet cur pour exécuter des requêtes SQL
    cur = connexion.cursor()
    # Exécuter une requête SQL
    query = "SELECT cities.name " \
        "FROM cities JOIN states ON cities.state_id = states.id " \
        "WHERE states.name = %s ORDER BY cities.id ASC"
    cur.execute(query, (search,))
    # Récupérer les résultats
    query_rows = cur.fetchall()
    cities_list = ', '.join(row[0] for row in query_rows)
    print(cities_list)
    # Fermer le cur et la connexion
    cur.close()
    connexion.close()


if __name__ == "__main__":
    """The code will not be executed when imported"""

    list_states()
